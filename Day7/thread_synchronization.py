import threading
import time


lock=threading.Lock()

def write_into_file(student_names):
    print(f"Thread {threading.current_thread().name} is opening the file.")
    lock.acquire()
    print(f"Thread {threading.current_thread().name} has acquired the lock.")
    with open("shared_file.txt","a") as f:
        f.writelines([f"{name}\n" for name in student_names])

    f.close()
    lock.release()
    print(f"Thread {threading.current_thread().name} has released the lock.")
    print("File writing completed.")

students=[]
student_list1 = ['Alice', 'Bob', 'Charlie', 'David']
student_list2 = ['Eve', 'Frank', 'Grace', 'Heidi']
student_list3 = ['Ivan', 'Judy', 'Mallory', 'Niaj']

students.append(student_list1)
students.append(student_list2)
students.append(student_list3)

threads = []
for student in students:
    t=threading.Thread(target=write_into_file, args=([student],))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
    
print("All students have been written to the file.")    
        