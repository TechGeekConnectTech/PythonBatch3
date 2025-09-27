'''
name1= "Ajay"
name2= "Vijay"
name3= "Sanjay"


print(name1)
print(name2)
print(name3)    

names = [] # Empty list

names = ["Ajay", "Vijay", "Sanjay",0,1,10.2, True, False] # List with 3 names

print(names) 
print(names[1])  # Print the second name in the list

names[2] = "Ranjana"
print(names)
# Print the entire list

names.append("Ramesh") # Add a new name to the list
print(names)
'''
fruits = []
# Append fruits to the list
fruits.append("Apple")
fruits.append("Banana")
fruits.append("Orange")
print(fruits)

# Remove a fruit from the list
fruits.remove("Banana")
print(fruits)

# Print the length of the list
print(len(fruits))

# Accessing elements by index
print(fruits[1])  # Second fruit

fruits.append("Grapes")
fruits.append("Mango")
fruits.append("Pineapple")
print(fruits)

# Iterate through the list
for fruit in fruits:
    if fruit == "Mango":
        print("Summer season fruit")
    elif fruit == "Pineapple":
        print("Tropical fruit")
    elif fruit == "Apple":
        print("Keeps the doctor away")
    elif fruit == "Orange":
        print("Rich in Vitamin C")
    elif fruit == "Grapes":
        print("Used to make wine")
    else:                
        print("I like", fruit)

#Before Sort
print("Before Sort", fruits)
# Sort the list
fruits.sort()
print(fruits)        

# Reverse the list
fruits.reverse()
print("After Reverse", fruits)

fruits.insert(2, "Kiwi") # Insert Kiwi at index 2
print(fruits)

print(fruits.count("Apple")) # Count occurrences of Apple

print(type(fruits))
# Clear list
#fruits.clear()
#print(fruits)