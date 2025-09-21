description="   this is our python class    "
mobile="12345678s90"

print("Capitalize :",description.capitalize())
print("UpperCase : ",description.upper())
print("LowerCase : ",description.lower())
print("Title : ",description.title())
print("Count of p : ",description.count('p'))
print("Find : ",description.find('our'))
print("Replace : ",description.replace('python','java'))
print("Split : ",description.split(' '))
print("Startswith :",description.startswith('our'))
print("Endswith :",description.endswith('class'))
print("Length : ",len(description))
print("Index of a : ",description.index('a'))
print("Is all alphanumeric : ",description.isalnum())
print("Is all alphabet : ",description.isalpha())
print("Is all digit : ",description.isdigit())
if mobile.isdigit() and len(mobile)==10:
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")

print("Is all space : ",description.isspace())
print("Is all lower : ",description.islower())
print("Is all upper : ",description.isupper())
print("Is all title : ",description.istitle())
print("Strip : ",description.strip())
print("Lstrip : ",description.lstrip())
print("Rstrip : ",description.rstrip())
print("Center",description.center(44,'*'))