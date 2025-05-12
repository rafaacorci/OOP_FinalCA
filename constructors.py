class Item(object):
    #constructor
    def __init__ (self, item_id:int, brand:str, model:str, price:float, condition:str ):
        self.item_id = item_id
        self.brand = brand
        self.model = model
        self.price = price
        self.condition = condition
    #string method
    def __str__(self):
        return "item_id: {}, brand: {}, model: {}, price: {}, condition:{}".format(self.item_id,self.brand,
                                                                                   self.model, self.price, self.condition)

class Bicycle(Item):
    #constructor subclass of Item
    def __init__(self, item_id:int, brand:str, model:str, frame_size: str, serial_number: str, price:float,condition:str ):
        Item.__init__(self, item_id, brand, model, price, condition)
        self.frame_size = frame_size
        self.serial_number = serial_number

    #string method
    def __str__(self):
        return "item_id: {}, brand: {}, model: {}, frame_size: {}, serial_number: {}, price: {}, condition: {}".format(
            self.item_id, self.brand,self.model,self.frame_size, self.serial_number, self.price, self.condition
        )

class SpareParts(Item):
    #constructor subclass of Item
    def __init__(self,item_id:int, category: str ,brand:str, model:str, price:float, condition:str ):
        Item.__init__(self, item_id, brand, model, price, condition)
        self.category = category

    #string method
    def __str__ (self):
        return  "item_id: {}, category: {}, brand:{}, model: {}, price:{}, condition:{}".format(
            self.item_id,self.category, self.brand, self.model, self.price, self.condition)


class Sale(object):
    #constructor
    def __init__(self, sale_id: int, item_id: int, sale_date, price):
        self.sale_id = sale_id
        self.item_id = item_id
        self.sale_date = sale_date
        self.price = price
    #string method
    def __str__(self):
        return  "sale_id: {}, item_id: {}, sale_date: {}, price: {}".format(self.sale_id,self.item_id,
                                                                            self.sale_date,self.price)

class Repairs(object):
    #constructors
    def __init__(self, repair_id: int, customer_name: str, description: str, cost: float, drop_off_date: int,
                 collection_date, status):
        self.repair_id = repair_id
        self.customer_name = customer_name
        self.description = description
        self.cost = cost
        self.drop_off_date = drop_off_date
        self.collection_date = collection_date
        self.status = status
    #string method
    def __str__(self):
        return ("repair_id:{}, customer_name: {}, description: {}, cost: {}, drop_off_date: {}, collection_date: {},"
                "status: {}").format(self.repair_id,self.customer_name,self.description,self.cost,self.drop_off_date,
                                     self.collection_date,self.status)



