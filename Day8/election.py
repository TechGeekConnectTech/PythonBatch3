class InvalidAgeError(Exception):
    pass


while True:
    try:
        age=int(input("Enter your age: "))
        if age<18:
            print("You are not eligible to vote.")
            raise InvalidAgeError
        else:
            print("You are eligible to vote.")
            break
    except ValueError as e:
        print("Invalid input. Please enter a valid age in numbers.")
    except Exception as e:
        print("Invalid age error:", e)    