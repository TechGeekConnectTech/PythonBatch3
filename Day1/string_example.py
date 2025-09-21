'''
student_name = "Sachin"
student_surname = 'Tendulkar'

print("lenght of student_name:", len(student_name))
print("Concatination of student_name and student_surname:", student_name + "  " + student_surname)
print("Check student_name variable type:", type(student_name))
'''
description = '''Sachin Ramesh Tendulkar is a former Indian international cricketer and a former captain of the Indian national team. 
He is widely regarded as one of the greatest 
batsmen in the history of cricket.
'''
#print(len(description))
#print(description[:100])  # Print first 100 characters of the description
#print(description[100:150])  # Print characters from index 100 to 150

'''
print(description.lower())
print("---------------------------------------------------")
print(description.upper())

print(description.capitalize())

print(description.replace("cricket", "Football"))
'''
student_names="Sachin, Dhoni, Kohli, Rohit, Jadeja"
name=student_names.split(",")
print(name[2])


name="Sachin"
print("My name is :", name)
print("My name is : %s" % name)
print("My name is : {}".format(name))