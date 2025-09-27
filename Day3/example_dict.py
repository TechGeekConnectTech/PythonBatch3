#students = {} # Empty dictionary to store student names and their scores

students = {
    "Student_id":1,
    "Student_name":"Sachin",
    "Student_Surname":"Tendulkar",
    "Student_Score":100
    }
print(students["Student_name"]) # Accessing value using key
print(students["Student_Surname"]) # Accessing value using key
print(students["Student_Score"]) # Accessing value using key

students["Student_name"]="Rohan" # Modifying value using key
print(students) # Accessing modified value using key    

print(students.get("Student_id")) # Accessing value using get() method
print(students["Student_id"]) # Accessing value using key
print(students.get("Student_address")) # Accessing value using get() method
#print(students["Student_address"]) # Accessing value using key

print(students.keys()) # Accessing all keys in the dictionary
print(students.values()) # Accessing all values in the dictionary

print(len(students)) # Getting the number of items in the dictionary

#students.clear() # Clearing all items in the dictionary
#print(students) # Accessing modified value using key

#del students # Deleting the dictionary
#print(students) # Accessing modified value using key