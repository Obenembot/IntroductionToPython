import csv
from collections import defaultdict


# Define the Order of class we are going to use for our product
class Product:
    def __init__(self, productId: int, name: str, category: str, quantity: int, price: float):
        self.id = productId
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"id={self.id}, name={self.name}, category={self.category}, quantity={self.quantity}, price={self.price}"


# This variable will hold the list of products after it is read from the file.
products = []


def read_inventory_file_date():
    with open("inventory.txt", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product: Product = Product(row['ID'], row['Name'], row['Category'], int(row['Quantity']),
                                       float(row['Price']))
            products.append(product)
        print(products)


# This Holds the different options that a user can perform
def inventory_option():
    print("1. Add a new product.")
    print("2. Update an existing product.")
    print("3. Delete a product.")
    print("4. Sort products by price.")
    print("5. Filter products by category.")
    print("6. Generate an inventory summary report.")
    print("7. Generate a category summary report .")
    print("0. Exit program.")


def add_new_product():
    print("Add Product Details")
    name: str = input("Name: ")
    while name == "":  # Force the User to Capture Name
        name: str = input("Enter Name: ")

    category = input("Category: ")
    while category == "":  # Force the User to Capture Category
        category: str = input("Enter Category: ")

    quantity: str = input("Quantity: ")
    while quantity == "":  # Force the User to Capture Quantity
        quantity = input("Enter Quantity: ")

    price: str = input("Price: ")
    while price == "":  # Force the User to Capture Price
        price: str = input("Enter Price: ")

    # get and increment the last product ID
    product_id: int = int(products[-1].id) + 1
    # Note: Casting of primitive data-types
    product: Product = Product(product_id, name, category, int(quantity), float(price))
    products.append(product)


def update_product():
    print("Update Product Details")
    product_id: str = input("Enter product Id To Update: ")
    name: str = input("Name: ")
    while name == "":  # Force the User to Capture Name
        name: str = input("Enter Name: ")

    category: str = input("Category: ")
    while category == "":  # Force the User to Capture Category
        category: str = input("Enter Category: ")

    quantity: str = input("Quantity: ")
    while quantity == "":  # Force the User to Capture Quantity
        quantity: str = input("Enter Quantity: ")

    price: str = input("Price: ")
    while price == "":  # Force the User to Capture Price
        price: str = input("Enter Price: ")

    # get and increment the last product ID
    for product in products:
        if int(product.id) == int(product_id):
            # Note: Casting of primitive data-types
            update_product: Product = Product(int(product_id), name, category, int(quantity), float(price))
            products.remove(product)
            products.append(update_product)


def delete_product_by_id():
    print("******** Delete Product ******** ")
    product_id: str = input("Enter Product ID: ")
    while product_id == "":  # Force the User to Capture Option
        product_id: str = input("Enter Product ID: ")
    for product in products:
        if int(product.id) == int(product_id):
            products.remove(product)


def sort_product_by_price():
    sorted_products = sorted(products, key=lambda p: p.price, reverse=True)
    print("\n********** Sorted Products By Price **********")
    for product in sorted_products:
        print(product)
    print(end="\n")


def filter_product_by_category():
    print("********** Filter Products by Categories **********")
    filter_field: str = input("Filter Category: ")
    while filter_field == "":  # Force the User to Capture Option
        filter_field: str = input("Filter Category: ")

    filter_products = []
    for product in products:
        if product.category == filter_field:  # Filter Category condition
            filter_products.append(product)

    print("********** Filtered Products **********")
    for filter_product in filter_products:
        print(filter_product)
    print()  # Add Extra line


def inventory_summary():
    print("\n********** Product Category Summary Report **********")
    summary = defaultdict(lambda: {"count": 0, "total_value": 0.0})
    for product in products:
        category: str = product.category
        quantity: int = int(product.quantity)
        price: float = float(product.price)
        total_price: float = quantity * price  # multiple the quantity by price to get the total

        # use this approach to update the matching category.
        summary[category]["count"] += 1
        summary[category]["total_value"] += total_price

    # Use
    for category, data, in summary.items():
        print(category, data)
    print("\n")


# Initialization of the products
read_inventory_file_date()
count = 0
while count < 10:
    inventory_option()  # Loads the different options that a user can select.
    option: str = input("Select Option: ")
    while option == "":  # Force the User to Capture Option
        option: str = input("Select Option: ")

    # Based on user input/selection different method or function/activity will be perform
    option: int = int(option)
    if option == 1:
        add_new_product()
    elif option == 2:
        update_product()
    elif option == 3:
        delete_product_by_id()
    elif option == 4:
        sort_product_by_price()
    elif option == 5:
        filter_product_by_category()
    elif option == 6:
        inventory_summary()
    elif option == 7:
        inventory_summary()
    elif option == 0:
        print("Exiting program...")
        count = 20
    else:
        print("\n***Invalid Option selected***")
