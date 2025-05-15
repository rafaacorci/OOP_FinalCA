
from SalesManager import SalesManager
from InventoryManager import InventoryManager
from RepairManager import RepairManager
import pandas as pd

inventory = InventoryManager()
repair = RepairManager()
sales = SalesManager()
#main menu function



def inventory_options():
    while True:
        print("------ Inventory manager ------")
        print("1. To view bicycles options")
        print("2. To view spare parts options")
        print("3. To return to the previous menu")

        user_choice = input("Please select a option").strip()
        if user_choice == "1":
            print("1. To view bicycles inventroy")
            print("2. To add a new bicycle")
            print("3. To remove a bicycle")
            print("4. To return to the previous menu")
            bike_choice = input("Please select a option").strip()
            #loading the
            if bike_choice == "1":
                inventory.load_bicycles()
                print(inventory.bicycles_df)
            if bike_choice == "2":
                #asking the user the information of the bicycle he wants to add to build the constructor
                brand = input("What is the brand?")
                model = input("What is the model?")
                frame_size = input("What is frame size?")
                serial_number = input("What is the serial number?")
                price = float(input("What is the price?"))
                while True:
                    try:
                        price = float(input("How much does it costs?"))
                        break
                    except ValueError:
                            print("Price must be a number")
                            continue
                condition = input("What is the bike condition?")
                inventory.add_bike(brand,model,frame_size,serial_number, price, condition)
                print(f"Your bike {brand},{model} has been recorded")
            if bike_choice == "3":
                # loading the dataframe so I can validate if the bike exists before trying to remove
                inventory.load_bicycles()
                bike_df = inventory.bicycles_df
                while True:
                    try:
                        user_input = int(input("Please enter the ID of the item you want to delete: "))
                        # exception to prevent the program from crashing from invalid input
                    except ValueError:
                        print("Invalid input, try again")
                        continue
                        # ensuring the user enters a valid input
                    if user_input not in bike_df["item_id"].values:
                        print("Item not found not found. Would you like to try again?")
                        while True:
                            # since the input is case sensitive, I'm making sure that the input is always lowercase
                            user_choice = input("Y/N: ").strip().lower()
                            if user_choice == "y":
                                break  # return to the previous loop
                            elif user_choice == "n":
                                print("Thank you, have a nice day")
                                return  #returning to the main menu
                            else:
                                print("Invalid input, try again")
                    else:
                        inventory.remove_bike(user_input)
                        print(f"Your bicycle {user_input} has been removed")
                        break
            elif bike_choice == "4":
                return
        elif user_choice == "2":
            print("1. To view spares parts inventroy")
            print("2. To add a new spare part")
            print("3. To remove a spare part")
            print("4. To return to the previous menu")
            spare_choice = input("Please select a option ").strip()
            if spare_choice == "1":
                inventory.load_spares()
                print(inventory.spares_df)
            elif spare_choice == "2":
                # asking the user the information of the spare part he wants to add to build the constructor
                category = input("What kind of spare part you want to add?")
                brand = input(f"What is the {category} brand?")
                model = input(f"What is the {category} model?")
                #ensuring a valid input for price
                while True:
                    try:
                        price = float(input("How much does it costs?"))
                        break
                    except ValueError:
                            print("Price must be a number")
                            continue
                condition = input("What is item condition?")
                inventory.add_spares(category,brand,model,price,condition)
                print(f"Your new {category} has been recorded sucessfully")
                break
            elif spare_choice == "3":
                # loading the dataframe so I can validate if the bike exists before trying to remove
                inventory.load_spares()
                spare_df = inventory.spares_df
                while True:
                    try:
                        user_input = int(input("Please enter the ID of the item you want to delete: "))
                        # exception to prevent the program from crashing from invalid input
                    except ValueError:
                        print("Invalid input, try again")
                        continue
                        # ensuring the user enters a valid input
                    if user_input not in spare_df["item_id"].values:
                        print("Item not found not found. Would you like to try again?")
                        while True:
                            # since the input is case sensitive, I'm making sure that the input is always lowercase
                            user_choice = input("Y/N: ").strip().lower()
                            if user_choice == "y":
                                break  # return to the previous loop
                            elif user_choice == "n":
                                print("Thank you, have a nice day")
                                return  # returning to the main menu
                            else:
                                print("Invalid input, try again")
                    else:
                        inventory.remove_spare(user_input)
                        print(f"Your spare part {user_input} has been removed")
                        break

        elif user_choice == "3":
            return
        else:
            print("invalid input. Try again.")

def main():
    #main menu loop
    while True:
        print(f"Welcome {user_name}! What would you like to do today?")
        print("1. To access inventory manager")
        print("2. To access repair manager")
        print("3. To access sales manager")
        print("4. To exit")

        user_choice = input("Please select a option. ").strip()

        if user_choice == "1":
            inventory_options()
        elif user_choice == "2":
            print("repair")
            # repair options placeholder
        elif user_choice == "3":
            #sales options placeholder
            print("sales")
        elif user_choice == "4":
            print(f"See you {user_name}, have a great day!")
            return
        else:
            print("Invalid input, try again")

user_name = input("Hi! What is your name?")
main()