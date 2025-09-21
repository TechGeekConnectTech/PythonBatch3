

def fun():
    a=10
    b=20
    global c
    c=a+b


fun()
print(c)  
print(a) 
print(b) 
