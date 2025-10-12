import threading
import time
def print_numbers():
    for i in range(1,10):
        print(f"Number: {i}")

def print_letters():
    for l in ['A','B','C','D','E','F','G','H','I']:
        print(f"Letter: {l}")

print("Starting Parallel execution...")
T1 = threading.Thread(target=print_numbers)
T2 = threading.Thread(target=print_letters)

#Start Thread
print("Thread Starting...")
T1.start()
T2.start()
#Wait until threads are completed

print("Main Thread Completed...")