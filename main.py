import re

class Vehicle:
    def __init__(self, vin, make, model, odo, purchase_price) -> None:
        self.vin = vin
        self.make = make
        self.model = model
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


def not_empty(input):
    if not input:
        raise ValueError("Input Cannot be Empty")
    return True

def validate_length(input, expected_length):
    if(len(input) < expected_length):
        raise ValueError("Input needs more characters")
    elif(len(input) > expected_length):
        raise ValueError("Input is too long")
    else:
        return True

def validateAlphaNumeric(input):
    pattern = r"^[a-zA-Z0-9]+$"  # alphanumeric characters only

    if not re.match(pattern, input):
        raise ValueError("Input does not match required pattern")
    return True

def validateString(input):
    if not isinstance(input, str):
        raise ValueError("Input must be a String")
    return True

def validateFloat(input):
    if not isinstance(input, float):
        raise ValueError("Input must be a Float")
    return True

def validateInt(input):
    if not isinstance(input, int):
        raise ValueError("Input must be a Integer")
    return True



if __name__ == "__main__":
    vin = "SALCL2FX4RH346788"
    make = "Porsche"
    model = "911"
    odo = 123
    cost = 123030.00

    vehicles = []


    # Testing Validations
    if(not_empty(vin) and validateAlphaNumeric(vin) and validate_length(vin, 17)):
        if(not_empty(make) and validateString(make)):
            if(not_empty(model) and validateAlphaNumeric(model)):
                if(not_empty(odo) and validateInt(odo)):
                    if(not_empty(cost) and validateFloat(cost)):
                        vehicles.append(Vehicle(vin, make, model, odo, cost))

    for vehicle in vehicles:
        vehicle.add_repair("Test Repair1", 252.36)
        vehicle.add_repair("Test Repair2", 52.3)
        vehicle.add_repair("Test Repair3", 25.6)
        vehicle.add_repair("Test Repair4", 2.36)
        print(vehicle)
        vehicle.show_repairs()