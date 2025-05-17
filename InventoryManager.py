import pandas as pd
import constructors
from constructors import Bicycle, SpareParts


class InventoryManager:
    """Class to load, write, and save the CSV files for inventory"""
    def __init__(self):
        # creating an empty Pandas DataFrame to facilitate manipulation in the other methods
        self.bicycles_df = pd.DataFrame()
        self.spares_df = pd.DataFrame()
    #method to load the csv where the bicycles inventory will be stored
    def load_bicycles(self):
        #loading the bicycles CSV file inside self.bicycles_df
        self.bicycles_df = pd.read_csv("bicycles.csv")
    #method to load the csv where spare parts inventory will be stored
    def load_spares(self):
        #loading the spare parts CSV file inside self.spares_df
        self.spares_df = pd.read_csv("spare_parts.csv")
    #method to add a row to bicycle CSV
    def add_bike(self,brand, model, frame_size, serial_number, price:float, condition):
        #loading the CSV file before adding to ensure we are working with the most up to date file.
        self.load_bicycles()
        # this is to create the item ID according to the number of rows on my DataFrame to ensure that every ID is unique.
        item_id = len(self.bicycles_df) + 2
        #creating a new instance of the Bicycle class
        new_bike = Bicycle(item_id, brand, model, frame_size, serial_number, price, condition)
        #converting the instance to a dictionary so it can be added to the DataFrame
        bike_data={
            "item_id":new_bike.item_id,
            "brand":new_bike.brand,
            "model":new_bike.model,
            "frame_size":new_bike.frame_size,
            "serial_number":new_bike.serial_number,
            "price":new_bike.price,
            "condition":new_bike.condition
        }
        #concatenating the data to the DataFrame
        self.bicycles_df = pd.concat([self.bicycles_df, pd.DataFrame([bike_data])],ignore_index=True)
        #saving the new data from the DataFrame to the respective CSV file
        self.bicycles_df.to_csv("bicycles.csv", index = False)

    # method to add a row to spare CSV
    def add_spares(self, category: str ,brand:str, model:str, price:float, condition:str):
        #loading the CSV file before adding to ensure we are working with the most up to date file.
        self.load_spares()
        #this is to create the item ID according to the number of rows on my DataFrame to ensure that every ID is unique.
        item_id = len(self.spares_df) +2
        #creating a new instance of the SpareParts class
        new_part = SpareParts(item_id, category,brand, model, price, condition)
        #converting the instance to a dictionary so it can be added to the CSV file
        parts_data = {
            "item_id":new_part.item_id,
            "category":new_part.category,
            "brand":new_part.brand,
            "model":new_part.model,
            "price":new_part.price,
            "condition":new_part.condition
        }
        #concatenating data to the DataFrame
        self.spares_df = pd.concat([self.spares_df, pd.DataFrame([parts_data])], ignore_index= True)
        self.spares_df.to_csv("spare_parts.csv", index = False)


    #method to remove a row from the bike csv
    def remove_bike(self, user_input):
        # loading the CSV file before adding to ensure we are working with the most up to date file.
        self.load_bicycles()
        # using the inplace = True to ensure that the no new dataframe is created and the change is saved
        self.bicycles_df.drop(self.bicycles_df[self.bicycles_df["item_id"]== user_input].index, inplace=True)
        #saving the changes to the CSV file
        self.bicycles_df.to_csv("bicycles.csv", index = False)

    #method to remove a row from the spare csv
    def remove_spare(self, user_input):
        self.load_spares()
        # using the inplace = True to ensure that the no new dataframe is created and the change is saved
        self.spares_df.drop(self.spares_df[self.spares_df["item_id"] == user_input].index, inplace=True)
        # saving the changes to the CSV file
        self.spares_df.to_csv("spare_parts.csv", index=False)








