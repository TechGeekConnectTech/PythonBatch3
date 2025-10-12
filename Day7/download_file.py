import threading
import time
import datetime

def download_file(file_name):
    print(f"Starting download of {file_name} at {datetime.datetime.now().strftime('%H:%M:%S')}")
    # Simulate a file download with sleep
    time.sleep(2)
    print(f"Completed download of {file_name} at {datetime.datetime.now().strftime('%H:%M:%S')}")

files=["file1.txt","file2.txt","file3.txt","file4.txt","file5.txt"]

threads=[]
for file in files:
    thread=threading.Thread(target=download_file, args=(file,))
    threads.append(thread)
    thread.start()

for thread in threads:
    print("Information about thread:", thread.name, thread.is_alive())
    thread.join()


print("All downloads completed.")    

