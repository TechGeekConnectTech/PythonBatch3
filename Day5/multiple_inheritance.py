class ElectricCar:
    abc=10
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def display_battery_info(self):
        print(f"Battery capacity is {self.battery_capacity} kWh")
        
class PetrolCar:
    abc="Hello"
    def __init__(self, fuel_tank_capacity):
        self.fuel_tank_capacity = fuel_tank_capacity

    def display_fuel_info(self):
        print(f"Fuel tank capacity is {self.fuel_tank_capacity} liters")

class HybridCar(ElectricCar, PetrolCar):
    def __init__(self, battery_capacity, fuel_tank_capacity):
        ElectricCar.__init__(self, battery_capacity)
        PetrolCar.__init__(self, fuel_tank_capacity)

    def display_info(self):
        self.display_battery_info()
        self.display_fuel_info()
        print(f"Car brand name is {self.brand} and name is {self.name}")


# #parent object
petrolcar=PetrolCar(50)
petrolcar.xyz=20
print(petrolcar.xyz)
petrolcar.display_fuel_info()

#child object 
hybridcar=HybridCar(10,20)
hybridcar.brand="Toyota"
hybridcar.name="Prius"
print(hybridcar.battery_capacity)
hybridcar.display_info()
print("-----------",hybridcar.abc)  #from ElectricCar
print("---------",hybridcar.abc)  #from PetrolCar   

#parent object
electriccar=ElectricCar(20)
electriccar.display_battery_info()

