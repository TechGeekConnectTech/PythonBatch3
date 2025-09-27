fruits=("Apple", "Banana", "Orange")
print(fruits)
#fruits[1]="Grapes" # This will raise an error because tuples are immutable

#fruits.append("Mango") # This will raise an error because tuples do not support append

print(fruits[2])
fruits.count("Banana") # Count occurrences of Banana
print(fruits.count("Banana"))

print(fruits.index("Orange")) # Find index of Orange

print(type(fruits))
print(len(fruits))