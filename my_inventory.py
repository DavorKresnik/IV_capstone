# Task 32 - Capstone IV

# ============= Global variable ===========
shoe_list = []

# ========== Classes ==============
class Shoe:
    '''
    This class contains attributes of country, code, product, cost and quantity of and item,
    a code that returns the value of all attributes,
    a code that sets the new quantity of the shoes and
    string representation of the Shoe class
    '''
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_country(self):
        return self.country

    def get_cost(self):
        return self.cost
    
    def get_quantity(self):
        return self.quantity
    
    def get_code(self):
        return self.code

    def get_product(self):
        return self.product

    def set_quantity(self, new_quantity):
        self.new_quantity = new_quantity
        self.quantity = new_quantity

    def __str__(self):
        return f"Country:{self.country}, Code:{self.code}, Product:{self.product}, Cost:{self.cost}, Quantity:{self.quantity}\n"


# ========== Functions ==============
def read_shoes_data():
    '''
    This function openes the inventory.txt and read the data from it
    and creates a shoes object then appends this object into the shoes list
    '''
    try:
        with open("inventory.txt", "r") as f:
            shoe_inventory = f.readlines()[1:]

        for line in shoe_inventory:
            country, code, product, cost, quantity = line.strip("\n").split(",")
            existing_shoe = Shoe(country, code, product, cost, quantity)
            shoe_list.append(existing_shoe)

    except:
        print("\nI could not reach your inventory file. Could you recheck it's location and name?\n")

def add_shoe():
    '''
    This function will allow the user to add a new shoe and append this object inside the global shoe list
    as well as appending it to the inventory.txt file
    '''
    country = input("In which warehouse is the shoe: ").title()
    code = input("Code of the shoe: ").upper()
    product = input("Product name: ").title()
    cost = input("Cost per item: ")
    quantity = input("Quantity of the item: ")

    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)

    with open("inventory.txt", "a") as f:
        f.write(f"{country},{code},{product},{cost},{quantity}\n")

    print("\nThe new shoe was added successfully\n")

def view_all():
    '''
    This function iterates over the shoes list and prints the details of the shoes
    '''
    for item in shoe_list:
        print(item)

def re_stock():
    '''
    This function finds the shoe with the lowest quantity and asks the user if they 
    want to change it then it updates the .txt file
    '''
    quantity = 100
    product = ""
    index = 0

    for indx, item in enumerate(shoe_list):
        if quantity > int(item.get_quantity()):
            quantity = int(item.get_quantity())
            product = item.get_product()
            index = indx
    
    print(f"\n{product} should re-stocked.")
    while True:
        user_choice = input("Would you like to re_stock this item? [y/n] ").lower()
        if user_choice == "n":
            break

        elif user_choice == "y":
            new_quantity = int(input("What is the new quantity? "))
            shoe_list[index].set_quantity(new_quantity)

            with open("inventory.txt", "w") as f:
                f.write("Country,Code,Product,Cost,Quantity\n")
                for item in shoe_list:
                    f.write(f"{item.get_country()},{item.get_code()},{item.get_product()},{item.get_cost()},{item.get_quantity()}\n")
            break

        else:
            print("Invalid input.")   


def search_shoe():
    '''
    This function will search for a shoe from the list using the shoe code and print it
    '''
    x = input("Enter the code of the shoe: ")
    for item in shoe_list:
        if x == item.get_code():
            print(item)

def value_per_item():
    '''
    This function calculates the total value for each site
    '''
    for index, item in enumerate(shoe_list, 1):
        total = int(item.get_cost()) * int(item.get_quantity())
        print(f"{index}: {total}")

def highest_quantity():
    '''
    Function determines the product with the highest quantity and prints 'on sale' statement
    '''
    quantity = 0
    product = ""

    for item in shoe_list:
        if quantity < int(item.get_quantity()):
            quantity = int(item.get_quantity())
            product = item.get_product() 

    print(f"\n{product} should be put on sale.\n")


# ========== Initializing the shoe directory =============
read_shoes_data()

# ========== Main Menu =============
menu  = "================================================\n"
menu += "\t  Welcome to the inventory\n"
menu += "================================================\n"
menu += "    Choose any of the following options\n\n"
menu += "a - Add new shoe\n"
menu += "w - View the inventory\n"
menu += "r - Re-stock\n"
menu += "s - Search for a shoe\n"
menu += "v - Display the value of the shoes\n"
menu += "h - Disply the shoe with the highest quantity\n"
menu += "e - Exit\n"
menu += "================================================\n"

while True:
    menu_chose = input(menu).lower()

    if menu_chose == "e":
        print("\nHave a nice day\n")
        break

    elif menu_chose == "a":
        add_shoe()

    elif menu_chose == "w":
        view_all()

    elif menu_chose == "r":
        re_stock()

    elif menu_chose == "s":
        search_shoe()
 
    elif menu_chose == "v":
        value_per_item()

    elif menu_chose == "h": 
        highest_quantity()

    else:
        print("\nInvalid input\n")