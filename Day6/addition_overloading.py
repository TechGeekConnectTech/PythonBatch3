import math

class AreaCalculator:
    def area(self, a=None, b=None):
        if a is not None and b is not None:
            return a * b  # Area of rectangle
        elif a is not None:
            return math.pi * a * a  # Area of circle
        else:
            raise ValueError("Invalid parameters for area calculation")
        
cal=AreaCalculator()
print(cal.area(5))
print(cal.area(10,20))        # Circle with radius 5``        