from datetime import date
from SalesManager import SalesManager
from InventoryManager import InventoryManager
from RepairManager import RepairManager
import pandas as pd

inventory = InventoryManager()
repair = RepairManager()
sales = SalesManager()

def sales_options():
    while True:
        print("------ Sales manager ------")
        print("1. To register a new bike sale")
        print("2. To register a new spare part sale")
        print("3. To generate a sales report")
        print("4. To return to the previous menu")

        user_choice = input("Please select an option").strip()

        if user_choice == "1":
            #loading the bicycles inventory DataFrame so I can validate if the bike being sold exists.
            inventory.load_bicycles()
            bike_df = inventory.bicycles_df
            while True:
                try:
                    item_id = int(input("What is the bike you are selling?"))
                except ValueError:
                    print("Invalid input. Try again.")
                    continue
                if item_id not in bike_df["item_id"].values:
                    print("Bike not found. Would you like to try again?")
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
                    sales.record_sales_bicyles(item_id)
                    print(f"Bike {item_id} sale sucessfully recorded")
                    break


        elif user_choice == "2":
            # loading the spare parts inventory DataFrame so I can validate if the bike being sold exists.
            inventory.load_spares()
            spare_df = inventory.spares_df
            while True:
                try:
                    item_id = int(input("What is the bike you are selling?"))
                except ValueError:
                    print("Invalid input. Try again.")
                    continue
                if item_id not in spare_df["item_id"].values:
                    print("Bike not found. Would you like to try again?")
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
                    sales.record_sales_spare(item_id)
                    print(f"Spare part {item_id} sale sucessfully recorded")
                    break
        elif user_choice == "3":
            sales.generate_sales_report()
            break
        elif user_choice == "4":
            return
        else:
            print("Invalid input. Try again")

def repair_options():
    while True:
        print("------ Repair manager ------")
        print("1. To register a new repair request")
        print("2. To update an existing repair request")
        print("3. To return to the previous menu")
        #Iam using strip to faciliate input validation
        user_choice = input("Please select an option").strip()

        if user_choice == "1":
            customer = input("What is the customer name?")
            description = input("What is the issue with the bike?")
            while True:
                try:
                    price = float(input("What is the repair cost?"))
                    break
                except ValueError:
                    print("Price must be a number")
                    continue
            drop_off_date = date.today()
            collection_date = input("What is the collection date? (DD/MM/YYYY")
            repair.record_repair(customer,description,price,drop_off_date, collection_date)
            print(f"{customer} repair request registered")
        elif user_choice == "2":
            #loading the repair Dataframe to validate input
            repair.load_repair()
            repair_df = repair.repair_df
            while True:
                try:
                    user_input = int(input("What repair ID would you like to update?"))
                except ValueError:
                    print("Invalid input. Try again.")
                    continue
                if user_input not in repair_df["repair_id"].values:
                    print("Repair requestn not found. Would you like to try again?")
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
                    new_status = input("What is the new status?")
                    repair.update_repair(user_input,new_status)
                    print(f"Your repair {user_input} has been updated to {new_status}")
                    break
        elif user_choice == "3":
            return

def inventory_options():
    while True:
        print("------ Inventory manager ------")
        print("1. To view bicycles options")
        print("2. To view spare parts options")
        print("3. To return to the previous menu")

        user_choice = input("Please select a option ").strip()
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
            elif bike_choice == "2":
                #asking the user the information of the bicycle he wants to add to build the constructor
                brand = input("What is the brand?")
                model = input("What is the model?")
                frame_size = input("What is frame size?")
                serial_number = input("What is the serial number?")
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
            elif bike_choice == "3":
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
            else:
                print("Invalid input. Try again")
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
                    except ValueError:
                            print("Price must be a number")
                            continue
                condition = input("What is item condition?")
                inventory.add_spares(category,brand,model,price,condition)
                print(f"Your new {category} has been recorded sucessfully")
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
            repair_options()
        elif user_choice == "3":
            sales_options()
        elif user_choice == "4":
            print(f"See you {user_name}, have a great day!")
            break
        else:
            print("Invalid input, try again")

user_name = input("Hi! What is your name?")
main()