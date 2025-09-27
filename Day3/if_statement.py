'''
if condition:
    #Write code which executes if condition is satisfied
elif another_condition:
    #Write code which executes if another_condition is satisfied    
else:
    #Write code which executes if condition is not satisfied
'''

fruits = ['apple', 'banana', 'cherry']

if 'banana' in fruits:
    print("Banana is in the list!")

if 'grape' not in fruits or 'apple' in fruits:
    print("Grape is not in the list or apple is in the list!")

age=10
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")  


city="Bangalore"
area="Whitefield"

if city=="Bangalore":
    if area=="Whitefield":
        print("You are in IT hub of India - Whitefield")
    else:
        print("You are in IT hub of India - Other Area")    
    print("You are in IT hub of India")
elif city=="Mumbai":
    print("You are in Financial capital of India")
elif city=="Chennai":
    print("You are in Detroit of India")
elif city=="Kolkata":
    print("You are in City of Joy")
elif city=="Delhi":
    print("You are in Capital of India")
else:
    print("You are in some other city")        
