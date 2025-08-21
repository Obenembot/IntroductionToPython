import sqlite3
import tkinter as tk
from datetime import datetime, date
from tkinter import ttk, messagebox

try:
    from tkcalendar import DateEntry
except ImportError:
    raise SystemExit(
        "Missing dependency: tkcalendar\nInstall it with: pip install tkcalendar"
    )

DB_FILE: str = "../library.db"
CURRENCY: str = "R"  # South African Currency symbol for fines
FINE_PER_DAY = 5  # R5 per day fine for overdue books


# ---------------------------- Database helpers ---------------------------- #

def get_conn():
    return sqlite3.connect(DB_FILE)


def init_db():
    # Get a connection and to the database
    with get_conn() as conn:
        cur = conn.cursor()
        # CREATE books table IF NOT EXISTS
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS books
                    (
                        id
                        INTEGER
                        PRIMARY
                        KEY
                        AUTOINCREMENT,
                        title
                        TEXT
                        NOT
                        NULL,
                        quantity
                        INTEGER
                        NOT
                        NULL
                    )
                    """)
        # CREATE borrowed_books table IF NOT EXISTS
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS borrowed_books
                    (
                        id
                        INTEGER
                        PRIMARY
                        KEY
                        AUTOINCREMENT,
                        student_name
                        TEXT
                        NOT
                        NULL,
                        book_id
                        INTEGER
                        NOT
                        NULL,
                        borrow_date
                        TEXT
                        NOT
                        NULL,
                        return_date
                        TEXT
                        NOT
                        NULL,
                        fine
                        REAL
                        DEFAULT
                        0,
                        FOREIGN
                        KEY
                    (
                        book_id
                    ) REFERENCES books
                    (
                        id
                    )
                        )
                    """)
        conn.commit()


# Initialize books and borrowed_books tables with sample data
def seed_books(cur):
    cur.execute("SELECT COUNT(*) FROM books")
    if cur.fetchone()[0] == 0:
        books = [
            ("Learn Python", 3),
            ("Database Systems", 2),
            ("Data Structures & Algorithms", 4),
            ("Networking Fundamentals", 1),
            ("Operating Systems", 2),
            ("ABC Mathematics", 2),
        ]
        cur.executemany("INSERT INTO books(title, quantity) VALUES(?,?)", books)


# Initialize borrowed_books tables with sample data
def seed_borrowed_books(cur):
    cur.execute("SELECT COUNT(*) FROM borrowed_books")
    if cur.fetchone()[0] == 0:
        # Use dates relative to today for demonstration
        today = date.today()
        borrowed_books = [
            ("Alan Jackson", 1,
             today.replace(day=max(1, today.day - 20)).strftime("%m/%d/%y"),
             today.replace(day=max(1, today.day - 10)).strftime("%m/%d/%y"), 0.0),
            ("Alan Walker", 1,
             today.replace(day=max(1, today.day - 1)).strftime("%m/%d/%y"),
             today.replace(day=max(1, today.day - 0)).strftime("%m/%d/%y"), 0.0),
            ("Brad Paisley", 3,
             today.replace(day=max(1, today.day - 12)).strftime("%m/%d/%y"),
             today.replace(day=max(1, today.day - 2)).strftime("%m/%d/%y"), 0.0),
            ("Don Williams", 3,
             today.replace(day=max(1, today.day - 1)).strftime("%m/%d/%y"),
             today.replace(day=max(1, today.day - 0)).strftime("%m/%d/%y"), 0.0),
            ("Tatiana Manaois ", 3,
             today.replace(day=max(1, today.day - 18)).strftime("%m/%d/%y"),
             today.replace(day=max(1, today.day - 8)).strftime("%m/%d/%y"), 0.0),
        ]
        cur.executemany("""
                        INSERT INTO borrowed_books(student_name, book_id, borrow_date, return_date, fine)
                        VALUES (?, ?, ?, ?, ?)
                        """, borrowed_books)
        # Reduce quantities accordingly
        for _, book_id, *_ in borrowed_books:
            cur.execute("UPDATE books SET quantity = quantity - 1 WHERE id = ?", (book_id,))


# Insert initial books and a couple of borrowed rows for testing
def seed_data():
    with get_conn() as conn:
        cur = conn.cursor()
        # Seed books only if table is empty
        seed_books(cur)
        # Seed borrowed_books only if empty
        seed_borrowed_books(cur)
        conn.commit()


# Utility queries
def list_books_available():
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, title, quantity FROM books WHERE quantity > 0 ORDER BY title")
        return cur.fetchall()


# Get a list of all borrowed books with optional filtering
def list_all_borrowed(filter_text=""):
    with get_conn() as conn:
        cur = conn.cursor()
        if filter_text:
            like = f"%{filter_text.lower()}%"
            cur.execute("""
                        SELECT b.id, b.student_name, bk.title, b.borrow_date, b.return_date, b.fine
                        FROM borrowed_books b
                                 JOIN books bk ON b.book_id = bk.id
                        WHERE LOWER(b.student_name) LIKE ?
                           OR LOWER(bk.title) LIKE ?
                        ORDER BY b.id ASC
                        """, (like, like))
        else:
            cur.execute("""
                        SELECT b.id, b.student_name, bk.title, b.borrow_date, b.return_date, b.fine
                        FROM borrowed_books b
                                 JOIN books bk ON b.book_id = bk.id
                        ORDER BY b.id ASC
                        """)
        return cur.fetchall()


# Return fine (float) if return date is before today: R5 fine per day late.
def check_for_fine(return_date_str):
    try:
        due = datetime.strptime(return_date_str, "%m/%d/%y").date()
    except ValueError:
        # Fallback to other common date format (e.g., 06/27/2025)
        try:
            due = datetime.strptime(return_date_str, "%m/%d/%Y").date()
        except ValueError:
            return 0.0
    today = date.today()
    if due < today:
        days = (today - due).days
        return float(days * FINE_PER_DAY)
    return 0.0


# Insert a new borrow record and update book quantity
def add_borrow(student_name, book_id, borrow_date_str, return_date_str):
    # Invoke compute fine.
    fine = check_for_fine(return_date_str)
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
                    INSERT INTO borrowed_books(student_name, book_id, borrow_date, return_date, fine)
                    VALUES (?, ?, ?, ?, ?)
                    """, (student_name, book_id, borrow_date_str, return_date_str, fine))
        # Update book quantity
        cur.execute("UPDATE books SET quantity = quantity - 1 WHERE id = ?", (book_id,))
        conn.commit()

# Update an existing borrow record and compute fine
def update_borrow(selected_user_id, student_name, book_id, borrow_date_str, return_date_str):
    # Invoke compute fine.
    fine = check_for_fine(return_date_str)
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
                    UPDATE borrowed_books
                    SET student_name=?, book_id=?, borrow_date=?, return_date=?, fine= ?
                    WHERE id=?
                    """, (student_name, book_id, borrow_date_str, return_date_str, fine, selected_user_id ))
        # Update book quantity
        cur.execute("UPDATE books SET quantity = quantity - 1 WHERE id = ?", (book_id,))
        conn.commit()

# Delete a borrow row and restore quantity by 1 for its book.
def delete_borrow(row_id):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT book_id FROM borrowed_books WHERE id = ?", (row_id,))
        row = cur.fetchone()
        if not row:
            return
        book_id = row[0]
        cur.execute("DELETE FROM borrowed_books WHERE id = ?", (row_id,))
        # Response to deletion: restore book quantity
        cur.execute("UPDATE books SET quantity = quantity + 1 WHERE id = ?", (book_id,))
        conn.commit()


# ******************************************** UI Section ******************************************** #
class StudentBookTracker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Borrow Tracker")
        # approximate style like screenshot
        self.geometry("1400x760")
        self.minsize(1100, 600)
        self.configure(bg="#d9d6cf")  # light beige background

        self._build_styles()
        self._build_left_form()
        self._build_right_panel()

        # initialize books and table
        self.refresh_books()
        self.refresh_table()

    # ---------- Styles ---------- #
    def _build_styles(self):
        style = ttk.Style(self)
        # Use default theme
        try:
            style.theme_use("clam")
        except:
            pass

        style.configure("Left.TLabelframe", background="#d9d6cf")
        style.configure("Left.TLabelframe.Label", font=("Segoe UI", 10, "bold"))
        style.configure("TLabel", background="#d9d6cf", font=("Segoe UI", 10))
        style.configure("TEntry", font=("Segoe UI", 10))
        style.configure("TCombobox", font=("Segoe UI", 10))

        # Buttons
        style.configure("Green.TButton", font=("Segoe UI", 11, "bold"), padding=6, background="#17801c",
                        foreground="white")
        style.map("Green.TButton", background=[("active", "#0f5e14")])
        style.configure("Red.TButton", font=("Segoe UI", 11, "bold"), padding=6, background="#d60c0c",
                        foreground="white")
        style.map("Red.TButton", background=[("active", "#a90a0a")])
        style.configure("Grey.TButton", font=("Segoe UI", 11, "bold"), padding=6, background="#6e6e6e",
                        foreground="white")
        style.map("Grey.TButton", background=[("active", "#555555")])

        # Treeview header: blue background, white bold font
        style.configure("Treeview.Heading", background="#0033cc", foreground="white", font=("Segoe UI", 10, "bold"))
        style.map("Treeview.Heading", background=[("active", "#002b99")])
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=26)

    # ---------- Left form ---------- #
    def _build_left_form(self):
        lf = ttk.LabelFrame(self, text="Borrow Book", style="Left.TLabelframe")
        lf.place(x=15, y=50, width=520, height=660)

        # Student Name
        ttk.Label(lf, text="Student Name:").place(x=20, y=40)
        self.entry_name = ttk.Entry(lf, width=40)
        self.entry_name.place(x=160, y=38)

        # Book combobox
        ttk.Label(lf, text="Book:").place(x=20, y=95)
        self.book_var = tk.StringVar()
        self.combo_books = ttk.Combobox(lf, textvariable=self.book_var, state="readonly", width=37)
        self.combo_books.place(x=160, y=92)

        # Dates
        ttk.Label(lf, text="Borrow Date:").place(x=20, y=150)
        self.borrow_date = DateEntry(lf, width=17, date_pattern="mm/dd/yy")
        self.borrow_date.place(x=160, y=148)

        ttk.Label(lf, text="Return Date:").place(x=20, y=205)
        self.return_date = DateEntry(lf, width=29, date_pattern="mm/dd/yy")
        self.return_date.place(x=160, y=203)

        # Buttons
        self.btn_add = ttk.Button(lf, text="Add / Update", style="Green.TButton", command=self.on_add)
        self.btn_add.place(x=40, y=280, width=120)

        self.btn_delete = ttk.Button(lf, text="Delete", style="Red.TButton", command=self.on_delete)
        self.btn_delete.place(x=200, y=280, width=120)

        self.btn_clear = ttk.Button(lf, text="Clear", style="Grey.TButton", command=self.on_clear)
        self.btn_clear.place(x=360, y=280, width=120)

    # ******************************************** build right panel (search + table + total) ******************************************** #
    def _build_right_panel(self):
        # Search bar
        ttk.Label(self, text="Search:").place(x=560, y=20)
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *_: self.refresh_table())
        self.entry_search = ttk.Entry(self, textvariable=self.search_var, width=40)
        self.entry_search.place(x=615, y=18)

        # Total label
        self.total_label_var = tk.StringVar(value="Total Borrowed Books: 0")
        ttk.Label(self, textvariable=self.total_label_var, font=("Segoe UI", 11, "bold")).place(x=1160, y=18)

        # Treeview with scrollbar
        columns = ("id", "student", "book", "borrow_date", "return_date", "fine")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("student", text="Student")
        self.tree.heading("book", text="Book")
        self.tree.heading("borrow_date", text="Borrow Date")
        self.tree.heading("return_date", text="Return Date")
        self.tree.heading("fine", text="Fine")

        self.tree.column("id", width=60, anchor="center")
        self.tree.column("student", width=180)
        self.tree.column("book", width=180)
        self.tree.column("borrow_date", width=120, anchor="center")
        self.tree.column("return_date", width=120, anchor="center")
        self.tree.column("fine", width=60, anchor="e")

        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)

        # place
        self.tree.place(x=560, y=50, width=800, height=660)
        vsb.place(x=1360, y=50, height=660)

        # Tag for overdue rows (fine > 0)
        self.tree.tag_configure("overdue", background="#ffcccc")

        # Bind selection to fill form (optional for delete convenience)
        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)

    # ******************************************** Utility / refresh ******************************************** #
    def refresh_books(self):
        books = list_books_available()
        self._books_map = {f"{title} (Qty: {qty})": bid for (bid, title, qty) in books}
        display_items = list(self._books_map.keys())
        self.combo_books["values"] = display_items
        # If previously selected book becomes unavailable, clear selection
        if self.book_var.get() not in display_items:
            self.book_var.set("")

    def refresh_table(self):
        # clear
        for row in self.tree.get_children():
            self.tree.delete(row)
        rows = list_all_borrowed(self.search_var.get().strip())
        for rid, student, book, bdate, rdate, fine in rows:
            tags = ("overdue",) if float(fine) > 0 else ()
            self.tree.insert("", "end", iid=str(rid),
                             values=(rid, student, book, bdate, rdate, f"{CURRENCY}{fine:.2f}"), tags=tags)
        self.total_label_var.set(f"Total Borrowed Books: {len(rows)}")

    # ******************************************** Events ******************************************** #
    def on_add(self):
        print('Add USer',self)

        selected = self.tree.selection()  # To Extract the user Id then use to update an entry
        if selected:
            selected_user_id = int(selected[0])
            print('selected',selected_user_id)

        name:str = self.entry_name.get().strip()
        book_display:str = self.book_var.get().strip()
        bdate = self.borrow_date.get_date()
        rdate = self.return_date.get_date()

        # Validation
        if not name:
            messagebox.showerror("Validation", "Student Name is required.")
            return
        if not book_display or book_display not in self._books_map:
            messagebox.showerror("Validation", "Please select a Book with available quantity.")
            return
        today = date.today()
        if bdate < today:
            messagebox.showerror("Validation", "Borrow Date cannot be in the past.")
            return
        if rdate < bdate:
            messagebox.showerror("Validation", "Return Date must not be before the Borrow Date.")
            return

        book_id = self._books_map[book_display]
        if selected_user_id:
            # Update existing borrow record
            update_borrow(selected_user_id, name, book_id, bdate.strftime("%m/%d/%y"), rdate.strftime("%m/%d/%y"))
        else:
           add_borrow(name, book_id, bdate.strftime("%m/%d/%y"), rdate.strftime("%m/%d/%y"))
        self.refresh_books()
        self.refresh_table()
        self.on_clear()
        messagebox.showinfo("Success", "Borrow record added.")

    def on_delete(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Delete", "Please select a row to delete.")
            return
        rid = int(selected[0])
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected record?"):
            delete_borrow(rid)
            self.refresh_books()
            self.refresh_table()
            self.on_clear()

    def on_clear(self):
        self.entry_name.delete(0, tk.END)
        self.book_var.set("")
        self.borrow_date.set_date(date.today())
        self.return_date.set_date(date.today())

    def on_row_select(self, _event=None):
        """Populate form with selected row (for convenience when deleting)."""
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        self.entry_name.delete(0, tk.END)
        self.entry_name.insert(0, values[1])


# ******************************************** Main ******************************************** #
def main():
    init_db()
    seed_data()

    # Update fines Each time the application starts up
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, return_date FROM borrowed_books")
        for row_id, rdate in cur.fetchall():
            fine = check_for_fine(rdate)
            cur.execute("UPDATE borrowed_books SET fine = ? WHERE id = ?", (fine, row_id))
        conn.commit()

    app = StudentBookTracker()
    app.mainloop()


if __name__ == "__main__":
    main()
