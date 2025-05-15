
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
                print(pd.read_csv("bicycles.csv"))
            if bike_choice == "2":
                brand = input("What is the brand?")
                model = input("What is the model?")
                frame_size = input("What is frame size?")
                serial_number = input("What is the serial number?")
                price = input("What is the price?")
                condition = input("What is the bike condition?")
                inventory.add_bike(brand,model,frame_size,serial_number, price, condition)
                print(f"Your bike {brand},{model} has been recorded")
            elif bike_choice == "4":
                return
        elif user_choice == "2":
            print("1. To view spares parts inventroy")
            print("2. To add a new spare part")
            print("3. To remove a spare part")
            print("4. To return to the previous menu")
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