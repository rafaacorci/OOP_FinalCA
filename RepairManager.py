from tkinter import READABLE

import pandas as pd
from constructors import Repairs
class RepairManager:
    """Class to manage all repair related actions"""
    def __init__(self):
        # creating an empty Pandas DataFrame to facilitate manipulation in the other methods
        self.repair_df = pd.DataFrame()
    #method to load the repair CSV
    def load_repair(self):
        self.repair_df = pd.read_csv("repairs.csv")
    #method to record a new repair on CSV
    def record_repair(self,customer_name: str, description: str, cost: float, drop_off_date, collection_date):
        self.load_repair()
        repair_id = len(self.repair_df) +1
        #creating a new instance of repairs
        new_repair = Repairs(repair_id,customer_name,description,cost,drop_off_date, collection_date,"Open")
        #converting instance to dictionary
        repair_data = {
            "repair_id":new_repair.repair_id,
            "customer_name": new_repair.customer_name,
            "description": new_repair.description,
            "cost": new_repair.cost,
            "drop_off_date":new_repair.drop_off_date,
            "collection_date":new_repair.collection_date,
            "status": new_repair.status
        }
        #concatenating data to the Dataframe
        self.repair_df = pd.concat([self.repair_df,pd.DataFrame([repair_data])], ignore_index= True)
        self.repair_df.to_csv("repairs.csv", index = False)

    #method to update a record on repairs CSV e.g. status from ready for collection to collected
    def update_repair(self, repair_id: int, new_status: str):
        self.load_repair()
        self.repair_df.loc[self.repair_df["repair_id"] == repair_id,"status"] = new_status
        self.repair_df.to_csv("repairs.csv", index = False)




