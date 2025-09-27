fruits={"Apple", "Banana", "Orange"}
print(fruits)
print(type(fruits))

#fruits[1] = "Grapes" # This will raise an error because sets do not support indexing
#print(fruits)

#print(fruits[0]) # This will raise an error because sets do not support indexing

fruits.add("Apple") # Adding a duplicate item will have no effect
fruits.add("Grapes") # Adding a new item
print(fruits)

fruits.remove("Banana") # Remove an item
print(fruits)

print(len(fruits)) # Print the length of the set


fruits.pop() # Remove and return an arbitrary item
print(fruits)
#fruits.clear() # Clear the set
#print(fruits)



#del fruits # Delete the set
#print(fruits) # This will raise an error because the set has been deleted


