try:
    students = iter(["Alice", "Bob", "Charlie"])
    print(next(students))
    print(next(students))
    print(next(students))
    print(next(students))  # This will raise StopIteration
except StopIteration as e:
    print("Error: StopIteration error.")
