class Car:
    brand="Maruti"
    name="ciaz"

    # def __init__(self):
    #     self.brand=None
    #     self.name=None
    #     print("Default Constructor is getting called")

    # def __init__(self,brand,name):
    #     self.brand=brand  
    #     self.name=name
    #     print("Parameter Constructor is getting called")

    def display_info(self):
        print(f"Car brand name is {self.brand} and name is {self.name}")

def show():
    print("SHowing information")


bmw=Car()
print(bmw.brand)
bmw.brand="Maruti"
bmw.name="Ciaz"
# obj1=Car("Maruti","Ciaz")
bmw.display_info()
# bmw=Car("BMW","S7")
show()