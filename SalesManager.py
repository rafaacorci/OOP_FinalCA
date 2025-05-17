from datetime import date
import pandas as pd
from constructors import Sales
from InventoryManager import InventoryManager #importing so I can call some methods from that class
import matplotlib.pyplot as plt


class SalesManager:
    """Class that will manage all sales related actions """
    def __init__(self):
        self.inventory = InventoryManager()
        self.sales_df = pd.DataFrame()

    # method to load the sales CSV
    def load_sales(self):
        self.sales_df = pd.read_csv("sales.csv")
    # method to record a new sale
    def record_sales_bicyles(self, item_id):
        self.load_sales()
        sale_id = len(self.sales_df)+2
        #opening the bicycle CSV file
        self.inventory.load_bicycles()
        bike_df = self.inventory.bicycles_df
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

    #record the sales of spare parts
    def record_sales_spare(self, item_id):
        self.load_sales()
        sale_id = len(self.sales_df) +2
        #opening spare parts CSV
        self.inventory.load_spares()
        spare_df = self.inventory.spares_df
        #using this information to help build the constructor
        part_id = spare_df[spare_df["item_id"]==item_id].iloc[0]
        #fetching the information I want from the DataFrame to build the constructor
        brand = part_id["brand"]
        model = part_id["model"]
        price = part_id["price"]
        category = part_id["category"]
        sale_date = date.today()
        #building the contructor
        new_sale = Sales(sale_id,item_id,"SparePart",category,brand,model,sale_date,price)
        #converting the instance to a dictionary so it can be added to the DataFrame and CSV
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
        #concatenating to the DataFrame
        self.sales_df = pd.concat([self.sales_df,pd.DataFrame([sale_data])], ignore_index= True)
        #saving the data to the respective CSV file.
        self.sales_df.to_csv("sales.csv", index = False)

    # method generate sales reports
    def generate_sales_report(self):
        self.load_sales()
        #making sure that the "sale_date" field is date type to create the charts
        self.sales_df["sale_date"] = pd.to_datetime(self.sales_df["sale_date"], dayfirst= True)
        # grouping the sales by dates and kinds with the sum of the total each sold.
        grouped_sales = (self.sales_df.groupby([self.sales_df["sale_date"].dt.date,"kind"])["price"].sum().unstack())
        #plotting bar chart
        grouped_sales.plot(kind = "bar", figsize=(12,6))
        plt.title("Total sales revenue of bicycles and spare parts per day")
        plt.xlabel("Sale Date")
        plt.ylabel("Total sales €")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.legend(title="Kind")
        plt.show()




