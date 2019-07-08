import json

# create a shopping list array to store the store and grocery item information
# create a store class to store the store information
# create a grocery item class to store the grocery item information

# SHOPPING LIST ARRAY
# Let the user ADD, DELETE the shopping lists they've created based off of the stores
# The store should be listed with a name and address

# STORE
# Let the user ADD, DELETE, the total list of items on the shopping list with the quantities listed as well
# The grocery item should be listed with a name and a quantity

# JSON FILE
# The user should be able to save the data to a json file upon closing the application
# The user should be able to load the data from the json file upon opening the application

shopping_list = []
user_input = ''
dict_file_list = []
dict_item_list = []

# Classes

class Store:
    def __init__(self, name, address, grocery_list = []):
        self.name = name
        self.address = address
        self.grocery_list = grocery_list
    
    @staticmethod
    def from_dictionary(dict):
        return Store(dict["name"], dict["address"], dict["grocery_list"])

class Grocery_Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    @staticmethod
    def from_dictionary(dict):
        return Grocery_Item(dict["name"], dict["quantity"])

# Functions

def overview():
    print("Welcome to Your Shopping List Manager App!\nPlease select one of the options below!")
    if len(shopping_list) == 0:
        print("Since you haven't started, go ahead and add a store to begin adding items!")
    else:
        for index in range(len(shopping_list)):
            print(f"{index + 1} - {shopping_list[index].name} - {shopping_list[index].address} - {len(shopping_list[index].grocery_list)} Items in list.")

# Store Functions

def add_store():
    store_name = input("Please enter the store name: ")
    store_address = input("Please enter the store address: ")
    store = Store(store_name, store_address)
    shopping_list.append(store)

def del_store():
    try:
        shopping_list.remove(select_a_store())
    except:
        print("ERROR: There are not any stores in your list yet!")

def select_a_store():
    store_index = input("Please enter the number of the store you would like to select: ")
    return shopping_list[store_index - 1]

# Grocery Item Functions

def add_grocery_item(store):
    grocery_name = input("Please enter the grocery item name: ")
    grocery_quantity = input("Please enter the gorcery item quantity: ")
    grocery_item = Grocery_Item(grocery_name, grocery_quantity)
    store.grocery_list.append(grocery_item)

def del_grocery_item(store):
    try:
        store.grocery_list.remove(select_a_grocery_item(store))
    except:
        print("ERROR: There are not any grocery items on this list yet!")

def select_a_grocery_item(store):
    grocery_item_index = input("Please enter the number of the item you would like to select: ")
    return store.grocery_list[grocery_item_index - 1]

def view_shopping_list(store):
    print(f"{store.name} - {store.address} - {len(store.grocery_list)} Items in list.")
    for item in store.grocery_list:
        print(f"{item.name} - {item.quantity}")

def send_data_to_json():
    for store in shopping_list:
        dict_file_list.append(store.__dict__)
        for item in store.grocery_list:
            dict_item_list.append(item.__dict__)
        dict_file_list[store.__dict__].append(dict_item_list)
    with open("shopping_list.json", "w") as file_object:
        json.dump(dict_file_list, file_object)
    dict_file_list.clear()
    dict_item_list.clear()

def take_data_from_json():
    with open("shopping_list.json") as file_object:
        dict_file_list = json.load(file_object)
    for dict_store in dict_file_list:
        store = Store.from_dictionary(dict_store)
        shopping_list.append(store)
        for dict_item in store.grocery_list:
            item = Grocery_Item.from_dictionary(dict_item)
            shopping_list[store].grocery_list.append(item)
    dict_file_list.clear()
    dict_item_list.clear()

if len(shopping_list) == 0:
    try:
        take_data_from_json()
    except:
        print("Tabula Rasa")

while user_input != "q":
    overview()
    user_input = input('Type "view list" to Select a Shopping List to View\nPress 1 to Add a Store\n Press 2 to Delete a Store\nPress 3 to Add a Grocery Item\nPress 4 to Delete a Grocery Item\nPress "q" to Quit')
    if user_input != '1' and user_input != '2' and user_input != '3' and user_input != '4' and user_input != 'q' and user_input != "view list":
        print("ERROR: Please select one of the available options!")
    if user_input == "view list":
        view_shopping_list(select_a_store())
    if user_input == '1':
        add_store()
    if user_input == '2':
        del_store()
    if user_input == '3':
        add_grocery_item(select_a_store())
    if user_input == '4':
        del_grocery_item(select_a_store())
    if user_input == 'q':
        print("Thanks for using your shopping list!")
        send_data_to_json()
        break