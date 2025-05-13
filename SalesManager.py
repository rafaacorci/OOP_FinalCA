from datetime import date
import pandas as pd
from constructors import Sales
from InventoryManager import InventoryManager #importing so I can call some methods from that class


class SalesManager:
    """Class that will manage all sales related actions """
    def __init__(self):
        self.inventory = InventoryManager()
        self.sales_df = pd.DataFrame()

    # method to load the sales CSV
    def load_sales(self):
        self.sales_df = pd.read_csv("sales.csv")
    # method to record a new sale
    def record_sales_bicyles(self):
        self.load_sales()
        sale_id = len(self.sales_df)+1
        #opening the bicycle CSV file
        self.inventory.load_bicycles()
        bike_df = self.inventory.bicycles_df
        while True:
            try:
                item_id = int(input("What is the item ID?"))
            except ValueError:
                    print("Invalid input, try again.")
                    continue
                    #checking if the item_id entered is valid
            if item_id not in bike_df["item_id"].values:
                    print("Item not found not found. Would you like to try again?")
                    while True:
                        #since the input is case sensitive, I'm making sure that the input is always lowercase
                        user_choice = input("Y/N: ").strip().lower()
                        if user_choice == "y":
                                break  # return to the previous loop
                        elif user_choice == "n":
                                print("Thank you, have a nice day")
                                return  # adicionar opcao depois para que o usuario volte para o menu (agora eu to saindo por competo)
                        else:
                            print("Invalid input, try again")
                            continue
            else:
                # I will use the information stored in the bicycle dateframe to build the the sales constructor
                bike_id = bike_df[bike_df["item_id"] == item_id].iloc[0]
                #getting the information I want from the dataframe and preparing for the constructor
                brand = bike_id["brand"]
                model = bike_id["model"]
                price = bike_id["price"]
                sale_date = date.today()
                #building the sales constructor
                new_sale = Sales(sale_id,item_id,"Bicycle",None,brand,model,sale_date,price)
                #converting to a dictionary to so it can be added to the Dataframe
                sale_data = {
                            "sale_id":new_sale.sale_id,
                            "item_id":new_sale.item_id,
                            "kind":new_sale.kind,
                            "category":new_sale.category,
                            "brand":new_sale.brand,
                            "model":new_sale.model,
                            "sale_date":new_sale.sale_date,
                            "price":new_sale.price
                            }
                #concatenating to the Dataframe
                self.sales_df = pd.concat([self.sales_df,pd.DataFrame([sale_data])],ignore_index=True)
                #saving the data to the respective CSV file
                self.sales_df.to_csv("sales.csv", index = False)
                print(f"Your item {item_id} sale has been recorded as sale_id {sale_id}")
                return



    # method to save the changes made on the sales CSV file
    def save_sales(self):
        pass
    # method generate sales reports
    def generate_sales_report(self):
        pass

