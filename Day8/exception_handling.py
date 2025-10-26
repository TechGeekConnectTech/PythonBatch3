
num=int(input("Enter a number: "))
try:
    with open("data.txt", "r") as file:
        data = file.read()
        print("File content:", data)
except Exception as e:
    print("An unexpected error occurred:", str(e))
    div=None
finally:
    print("File read successfully.")

print("This statement is after the division.")