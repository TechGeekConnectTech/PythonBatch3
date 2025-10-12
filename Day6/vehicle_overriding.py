class Vehicle:
    def fuel_type(self):
        return "Petrol or Diesel"

class Car(Vehicle):
    def fuel_type(self):
        return "Petrol"

class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electric"        


vehicle=Vehicle()
car=Car()
electric_car=ElectricCar()
print(vehicle.fuel_type())      # Output: Petrol or Diesel
print(car.fuel_type())          # Output: Petrol    
print(electric_car.fuel_type()) # Output: Electric

'''
vehicles = [Vehicle(), Car(), ElectricCar()]

for v in vehicles:
    print(f"{v.__class__.__name__}: using {v.fuel_type()} fuel")
'''    