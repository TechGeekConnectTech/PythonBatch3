import math

number=input("Enter a number: ")

print(f"Factorial of {number} is {math.factorial(int(number))}")
print(f"Square root of {number} is {math.sqrt(int(number))}")
print(f"Sine of {number} is {math.sin(int(number))}")
print(f"Cosine of {number} is {math.cos(int(number))}")
print(f"Tangent of {number} is {math.tan(int(number))}")
print(f"Logarithm (base 10) of {number} is {math.log10(int(number))}")
print(f"Exponential of {number} is {math.exp(int(number))}")
print(f"Ceiling of {number} is {math.ceil(float(number))}")
print(f"Floor of {number} is {math.floor(float(number))}")
print(f"Absolute value of {number} is {math.fabs(float(number))}")
print(f"Power of {number} raised to 2 is {math.pow(int(number), 2)}")
print(f"pi constant is {math.pi}")
if math.isnan(float(number)):
    print(f"{number} is Not a Number (NaN)")

print(math.isqrt(int(number))**2)
if math.isqrt(int(number))**2 == 25:
    print(f"{number} is a perfect square")

