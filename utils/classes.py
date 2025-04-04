class Vehicle:
    def __init__(self, vin, make, model, year, odo, purchase_price) -> None:
        self.vin = vin
        self.make = make
        self.model = model
        self.year = year
        self.odo = odo
        self.purchase_price = purchase_price
        self.repairs = []

    def add_repair(self, repair_desc, repair_cost) -> None:
        self.repairs.append(Repair(len(self.repairs), repair_desc, repair_cost))

    def remove_repair(self, id) -> None:
        for (repair, index) in enumerate(self.repairs):
            if(repair.id == id):
                self.repairs.pop(index)

    def calculate_repairs(self) -> float:
        amount = 0.0
        for repair in self.repairs:
            amount += repair.get_total()
        return round(amount, 2)

    def total_price(self) -> float:
        try:
            return round(self.purchase_price + self.calculate_repairs(), 2)
        except:
            print("Cannot Calculate Total")

    def show_repairs(self):
        for repair in self.repairs:
            print(repair)

    def __repr__(self):
        return f"""
VIN: {self.vin}
MAKE: {self.make}
MODEL: {self.model}
YEAR: {self.year}
ODOMETER: {self.odo}
PURCHASE PRICE: {self.purchase_price}
REPAIR COST: {self.calculate_repairs()}
PRICE: {self.total_price()}
"""


class Repair:
    def __init__(self, id, description, cost) -> None:
        self.id = id
        self.desc = description
        self.cost = cost

    def get_tax(self) -> float:
        return round(self.cost * 0.08, 2)

    def get_total(self) -> float:
        return round(self.cost + self.get_tax(), 2)
    
    def __repr__(self):
        return f"""
{self.desc}:
COST : {self.cost}
TAX  : {self.get_tax()}
TOTAL: {self.get_total()}
"""
    

class Customer:
    def __init__(self, first_name, last_name, address, phone, vehicle):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.vehicle = vehicle

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f"""
NAME: {self.get_full_name()}
ADDRESS: {self.address}
PHONE: {self.phone}
VEHICLE: {self.vehicle.year} {self.vehicle.make} {self.vehicle.model}
"""