import pandas as pd
from InventoryManager import InventoryManager
from SalesManager import SalesManager
from RepairManager import RepairManager
from datetime import date
manager = InventoryManager()
sales = SalesManager()
repair = RepairManager()
#manager.add_bike("Cannondael", "Topstone","Large","SNDAS12",1300,"New")
#manager.add_bike("Cannondael", "Topstone5","Large","SNDAS12",1300,"New")

#repair.update_repair(1,"collected")

#print(pd.read_csv("repairs.csv"))

#print("Item not found not found. Would you like to try again?\nY/N")

sales.generate_sales_report()


