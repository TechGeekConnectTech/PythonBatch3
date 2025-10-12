class Dog:
    def sound(self):
        return "Woof"
    
class Cat:
    def sound(self):
        return "Meow"

def animal_sound(animal):
    print(animal.sound())


dog=Dog()
cat=Cat()


animal_sound(dog)  # Output: Woof
animal_sound(cat)  # Output: Meow