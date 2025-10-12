class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Vehicle Brand: {self.brand}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        Vehicle.__init__(self,brand, model)
        self.num_doors = num_doors

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Number of Doors: {self.num_doors}"

class ElectricCar(Car):
    def __init__(self, brand, model, num_doors, battery_capacity):
        Car.__init__(self,brand, model, num_doors)
        self.battery_capacity = battery_capacity

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Battery Capacity: {self.battery_capacity} kWh"


elecObj=ElectricCar("Tesla", "Model S", 4, 100)
print(elecObj.display_info())
