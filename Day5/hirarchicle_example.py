class Animal:
    def __init__(self, category):
        self.category = category

    def behave(self):
        print("This animal category is:", self.category)
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__("Pet")
        self.name = name

    def behave(self):
        super().behave()  # Call the parent class method
        print(f"{self.name} barks and wags its tail.")

class Tiger(Animal):
    def __init__(self, name):
        super().__init__("Wild")
        self.name = name

    def behave(self):
        super().behave()  # Call the parent class method
        print(f"{self.name} roars and prowls.")

dog=Dog("Buddy")
dog.behave()  # Output: Buddy barks and wags its tail.   
tiger=Tiger("Sheru")
tiger.behave()  # Output: Sheru roars and prowls.