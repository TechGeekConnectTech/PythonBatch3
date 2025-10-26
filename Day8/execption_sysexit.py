import sys
try:
    print("Before sys.exit()")
    sys.exit("Exiting the program")
except SystemExit as e:
    print("Caught SystemExit exception:", e)
print("This statement will not be printed.")
