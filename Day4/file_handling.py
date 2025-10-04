import os

#file_obj = open("student.txt","w")   #write mode
#file_obj = open("student.txt","r")  #read mode
#file_obj = open("student.txt","a")  #append mode
#file_obj = open("student.txt","r+")  #read and write mode
#file_obj = open("student.txt","a+")  #append and read mode
#file_obj = open("student.txt","w+")  #write and read mode
#file_obj = open("student.txt","x")  #create mode
#file_obj = open("student.txt","x+")  #create and read mode
#file_obj = open("student.txt")  #default read mode

#file_obj = open("student.txt","a")
#file_obj.write("Sachin")
#file_obj.write("\nTendulkar")
#file_obj.write("\nIndia")
#file_obj.write("\nCricket")
#file_obj.close()  #read mode in binary

#file_obj = open("student.txt","r")
#data = file_obj.read()
#print(data)
'''
file_obj = open("student.txt","r")
data = file_obj.readlines()
for line in data:
    if "India" in line:
        print(line)
file_obj.close()

file_obj = open("student.txt","r")
data = file_obj.readline()
print(data)
file_obj.close()

students = ["Dhoni\n","Raina\n","Kohli\n","Bumrah\n","Jadeja\n"]
file_obj=open("indian_players.txt","w")
file_obj.writelines(students)
file_obj.close()

isfound=False
file_obj=open("indian_players.txt","r")
data=file_obj.readlines()
for line in data:
    if "Ranjana" in line:
        isfound=True
        break
file_obj.close()


if isfound:
    print("Ranjana is founnd in the file")
else:
    print("Ranjana is not found in the file")
    '''


file_obj=open("indian_players.txt","r")
data=file_obj.readlines()
for line in data:
    name,score=line.split(",")
    if int(score) > 35:
        print(name, "Student passed with score:", score)
    else:
        print(name, "Student failed with score:", score)
file_obj.close()

# Delete the files
os.remove("student.txt")

