#def <function_name>(<parameter>,<parameter2>):
#    <function_body>
#    return <return_value>

# Defination of a function named greet that takes one parameter 'name'
def greet(name):
    print("Hello",name)

greet(1)
greet("Sachin")
greet(10.2)
greet([1,2,3])
greet((1,2,3))
greet({1,2,3})
greet({1:"one",2:"two",3:"three"})
greet(True)
greet()