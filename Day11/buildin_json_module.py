import json

student = {
    "name":"Sachin",
    "age":30,
    "courses":["Math","CompSci"]
}

#
print(student)
print(type(student))

# Convert Python object to JSON string
student_json=json.dumps(student)

print(student_json)
print(type(student_json))

# Convert JSON string back to Python object
student_obj=json.loads(student_json)

print(student_obj)
print(type(student_obj))

# Pretty print JSON string
student_pretty=json.dumps(student, indent=5)
print(student_pretty)

# Access data from JSON string by converting it back to Python object
student_data=json.loads(student_json)
print(student_data['name'])
print(student_data['age'])
print(student_data['courses'])

'''
# Write JSON string to a file
with open('student.json', 'w') as f:
    json.dump(student, f)

'''

# Read JSON string from a file
with open('student.json', 'r') as f:
    student_from_file=json.load(f)

for student in student_from_file:
    print(type(student))
