students = [
    {
    "Student_id":1,
    "Student_name":"Sachin",
    "Student_Surname":"Tendulkar",
    "Student_Score":100
    },
    {
    "Student_id":2,
    "Student_name":"Rohan",
    "Student_Surname":"Sharma",
    "Student_Score":95
    },
    {
    "Student_id":3,
    "Student_name":"Ajay",
    "Student_Surname":"Kumar",
    "Student_Score":90
    }  
]

print(students[0]["Student_name"]) # Accessing value using key
print(students[1]["Student_name"])
print(students[2]["Student_name"])

for student in students:
    print(student["Student_name"], student["Student_Surname"], "has scored", student["Student_Score"])