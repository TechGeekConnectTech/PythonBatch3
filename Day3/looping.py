fruits = ['apple', 'banana', 'cherry']

#while fruits:
#    print(fruits)


#while condition:
#    #write code which executes as long as condition is satisfied     

#while True:
#    print("Infinite Loop")

count=1
while count<=10:
    print("Count is :",count)
    count+=1

for fruit in fruits:
    for char in fruit:
        print(char)   

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    if fruit=='banana':
        break
    print(fruit)       

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    if fruit=='banana':
        continue
    print(fruit)      

for i in range(10,36):
    if i%2==0:
        print("Even Number :",i)
    else:   
        print("Odd Number :",i)