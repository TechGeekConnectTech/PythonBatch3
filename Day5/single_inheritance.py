class Vehicle:
    def __init__(self,brand,name):
        self.brand=brand  
        self.name=name
        print("Parameter Constructor is getting called")

    def display_info(self):
        print(f"Car brand name is {self.brand} and name is {self.name}")


class Car(Vehicle):
    def __init__(self,brand,name, wheels):
        super().__init__(brand,name)
        self.wheels=wheels
        print("Car class constructor is called")

    def show_vehicle(self):
        print(f"Car has {self.wheels} wheels")


vehicle=Vehicle("Maruti","Ciaz")
vehicle.display_info()
car=Car("BMW","X5",4)
car.show_vehicle()     