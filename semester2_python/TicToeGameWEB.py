from flask import Flask, request, redirect, url_for, render_template_string, session
import random
from dataclasses import dataclass, asdict

app = Flask(__name__)
app.secret_key = "change-me-in-production"  # required for Flask sessions

# ---------- Domain Model (same behavior as your console version) ----------

@dataclass
class Player:
    name: str
    symbol: str
    is_computer: bool = False


class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]
        self.rows = {"A": 0, "B": 1, "C": 2}

    def to_dict(self):
        return {"grid": self.grid}

    @classmethod
    def from_dict(cls, d):
        b = cls()
        b.grid = d["grid"]
        return b

    def is_valid_move(self, position):
        if not position or len(position) != 2:
            return False
        row, col = position[0].upper(), position[1]
        if row not in self.rows or not col.isdigit():
            return False
        col = int(col) - 1
        return 0 <= col <= 2 and self.grid[self.rows[row]][col] == " "

    def make_move(self, position, symbol):
        row, col = position[0].upper(), int(position[1]) - 1
        self.grid[self.rows[row]][col] = symbol

    def get_available_moves(self):
        moves = []
        for r_label, r_idx in self.rows.items():
            for c in range(3):
                if self.grid[r_idx][c] == " ":
                    moves.append(f"{r_label}{c+1}")
        return moves

    def check_winner(self, symbol):
        g = self.grid
        # rows/cols
        for i in range(3):
            if all(g[i][j] == symbol for j in range(3)):
                return True
            if all(g[j][i] == symbol for j in range(3)):
                return True
        # diagonals
        if all(g[i][i] == symbol for i in range(3)):
            return True
        if all(g[i][2-i] == symbol for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(cell != " " for row in self.grid for cell in row)


class Game:
    def __init__(self, board=None, p1=None, p2=None, scoreboard=None, current="X"):
        self.board = board or Board()
        self.player1 = p1
        self.player2 = p2
        self.current_symbol = current  # "X" or "O"
        self.scoreboard = scoreboard or {"X": 0, "O": 0, "Draws": 0}
        self.state = "playing"  # "playing" | "won" | "draw"
        self.message = ""

    def to_session(self):
        return {
            "board": self.board.to_dict(),
            "player1": asdict(self.player1) if self.player1 else None,
            "player2": asdict(self.player2) if self.player2 else None,
            "current_symbol": self.current_symbol,
            "scoreboard": self.scoreboard,
            "state": self.state,
            "message": self.message,
        }

    @classmethod
    def from_session(cls, data):
        if not data:
            return None
        game = cls(
            board=Board.from_dict(data["board"]),
            p1=Player(**data["player1"]),
            p2=Player(**data["player2"]),
            scoreboard=data["scoreboard"],
            current=data["current_symbol"],
        )
        game.state = data.get("state", "playing")
        game.message = data.get("message", "")
        return game

    def current_player(self):
        return self.player1 if self.current_symbol == "X" else self.player2

    def other_player(self):
        return self.player2 if self.current_symbol == "X" else self.player1

    # --- AI logic identical to your console rules ---
    def computer_move(self):
        moves = self.board.get_available_moves()
        # 1. Try to win
        for m in moves:
            self.board.make_move(m, "O")
            if self.board.check_winner("O"):
                self.board.make_move(m, " ")  # revert preview
                return m
            self.board.make_move(m, " ")
        # 2. Block X
        for m in moves:
            self.board.make_move(m, "X")
            if self.board.check_winner("X"):
                self.board.make_move(m, " ")
                return m
            self.board.make_move(m, " ")
        # 3. Center
        if "B2" in moves:
            return "B2"
        # 4. Corners
        for c in ["A1", "A3", "C1", "C3"]:
            if c in moves:
                return c
        # 5. Random
        return random.choice(moves)

    def make_move_and_update(self, pos):
        if self.state != "playing":
            return
        if not self.board.is_valid_move(pos):
            self.message = "Invalid move. Try again."
            return

        player = self.current_player()
        self.board.make_move(pos, player.symbol)

        if self.board.check_winner(player.symbol):
            self.state = "won"
            self.message = f"{player.name} wins!"
            self.scoreboard[player.symbol] += 1
            return

        if self.board.is_draw():
            self.state = "draw"
            self.message = "It's a draw!"
            self.scoreboard["Draws"] += 1
            return

        # Switch turns
        self.current_symbol = "O" if self.current_symbol == "X" else "X"

    def reset_board_for_next_round(self):
        self.board = Board()
        self.current_symbol = "X"
        self.state = "playing"
        self.message = ""


# ---------- HTML Template (single file for simplicity) ----------

TEMPLATE = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Tic Tac Toe (Flask)</title>
  <style>
    body { font-family: system-ui, Arial, sans-serif; background:#111; color:#eee; display:flex; justify-content:center; }
    .wrap { max-width:900px; width:100%; padding:24px; }
    h1 { margin-top:0; }
    .card { background:#1a1a1a; border:1px solid #333; border-radius:16px; padding:20px; }
    .row { display:flex; gap:12px; flex-wrap:wrap; }
    .btn { padding:10px 14px; border:1px solid #444; background:#222; color:#eee; border-radius:10px; cursor:pointer; }
    .btn[disabled] { opacity:.6; cursor:not-allowed; }
    .primary { background:#2d6cdf; border-color:#2d6cdf; }
    .success { background:#2fa36b; border-color:#2fa36b; }
    .danger { background:#b64545; border-color:#b64545; }
    .grid { display:grid; grid-template-columns: 40px repeat(3, 80px); grid-auto-rows: 40px; gap:0; margin-top:16px; }
    .cell, .label { display:flex; align-items:center; justify-content:center; border:1px solid #444; font-size:26px; }
    .label { background:#151515; font-weight:700; }
    .cell button { width:100%; height:100%; font-size:26px; background:transparent; border:0; color:#eee; cursor:pointer; }
    .note { color:#bbb; margin-top:12px; }
    .msg { margin:14px 0; font-weight:700; }
    .score { margin-top:10px; }
    form.inline { display:inline; }
    .footer { margin-top:22px; color:#888; font-size:14px; }
  </style>
</head>
<body>
  <div class="wrap">
    <h1>=== Welcome to Tic Tac Toe ===</h1>

    {% if not game %}
    <div class="card">
      <h2>Start a New Game</h2>
      <form method="post" action="{{ url_for('start') }}">
        <div class="row">
          <label>Mode:
            <select name="mode" class="btn">
              <option value="pvp">Player vs Player</option>
              <option value="pvc">Player vs Computer</option>
            </select>
          </label>
          <label>Player 1 name (X):
            <input class="btn" style="width:220px" type="text" name="p1" placeholder="e.g., Amy" required>
          </label>
          <label id="p2-label">Player 2 name (O):
            <input class="btn" style="width:220px" type="text" name="p2" placeholder="e.g., John">
          </label>
        </div>
        <div class="note">If you choose Player vs Computer, Player 2 becomes "Computer (O)".</div>
        <div style="margin-top:12px;">
          <button class="btn primary" type="submit">Start</button>
        </div>
      </form>
    </div>

    {% else %}
    <div class="card">
      <div class="row" style="justify-content:space-between; align-items:center;">
        <div>
          <strong>Mode:</strong>
          {% if game.player2.is_computer %} Player vs Computer {% else %} Player vs Player {% endif %}
          &nbsp; | &nbsp; <strong>Players:</strong> {{ game.player1.name }} (X) vs {{ game.player2.name }} (O)
        </div>
        <div>
          <form class="inline" method="post" action="{{ url_for('reset_match') }}">
            <button class="btn danger" type="submit">End Match</button>
          </form>
        </div>
      </div>

      <div class="grid">
        <div class="label"></div>
        <div class="label">1</div>
        <div class="label">2</div>
        <div class="label">3</div>

        {% for rlabel, r in [('A',0), ('B',1), ('C',2)] %}
          <div class="label">{{ rlabel }}</div>
          {% for c in [0,1,2] %}
            {% set val = game.board.grid[r][c] %}
            <div class="cell">
              {% if val.strip() == '' and game.state == 'playing' and (not current_player.is_computer) and current_player.symbol == next_symbol %}
                <form method="post" action="{{ url_for('move') }}">
                  <input type="hidden" name="pos" value="{{ rlabel }}{{ c+1 }}">
                  <button type="submit">{{ val }}</button>
                </form>
              {% else %}
                <button disabled>{{ val }}</button>
              {% endif %}
            </div>
          {% endfor %}
        {% endfor %}
      </div>

      <div class="msg">
        {% if game.state == 'playing' %}
          {{ current_player.name }}'s turn ({{ current_player.symbol }})
        {% else %}
          {{ game.message }}
        {% endif %}
      </div>

      {% if game.state != 'playing' %}
      <form class="inline" method="post" action="{{ url_for('next_round') }}">
        <button class="btn success" type="submit">Play Again</button>
      </form>
      {% endif %}

      <div class="score">
        <strong>Scoreboard:</strong>
        &nbsp; X Wins: {{ game.scoreboard['X'] }}
        &nbsp; | O Wins: {{ game.scoreboard['O'] }}
        &nbsp; | Draws: {{ game.scoreboard['Draws'] }}
      </div>
    </div>
    {% endif %}

    <div class="footer">Tip: The grid accepts moves like <code>A1</code>, but here you can just click the cells.</div>
  </div>
</body>
</html>
"""

# ---------- Helpers to load/save game in session ----------

def load_game():
    return Game.from_session(session.get("game"))

def save_game(game: Game):
    session["game"] = game.to_session()

# ---------- Routes ----------

@app.get("/")
def home():
    game = load_game()
    ctx = {}
    if game:
        current_player = game.player1 if game.current_symbol == "X" else game.player2
        ctx.update({
            "game": game,
            "current_player": current_player,
            "next_symbol": game.current_symbol
        })
    return render_template_string(TEMPLATE, **ctx)

@app.post("/start")
def start():
    mode = request.form.get("mode", "pvp")
    p1_name = request.form.get("p1", "Player 1").strip() or "Player 1"

    if mode == "pvp":
        p2_name = (request.form.get("p2") or "").strip() or "Player 2"
        p2 = Player(p2_name, "O", is_computer=False)
    else:
        p2 = Player("Computer", "O", is_computer=True)

    game = Game(p1=Player(p1_name, "X"), p2=p2)
    save_game(game)
    return redirect(url_for("home"))

@app.post("/move")
def move():
    game = load_game()
    if not game:
        return redirect(url_for("home"))

    # Human move (only if current is human)
    if not game.current_player().is_computer and game.state == "playing":
        pos = request.form.get("pos", "")
        game.make_move_and_update(pos)

    # If computer's turn, let AI play automatically (may need 2 turns if human just ended the game)
    while game.state == "playing" and game.current_player().is_computer:
        pos = game.computer_move()
        game.make_move_and_update(pos)

    save_game(game)
    return redirect(url_for("home"))

@app.post("/next-round")
def next_round():
    game = load_game()
    if not game:
        return redirect(url_for("home"))
    game.reset_board_for_next_round()
    # If computer is X (not in our setup), we would let it play here; in our rules X is always human.
    save_game(game)
    return redirect(url_for("home"))

@app.post("/reset-match")
def reset_match():
    session.pop("game", None)
    return redirect(url_for("home"))

# ---------- Dev entry ----------
if __name__ == "__main__":
    app.run(debug=True)
