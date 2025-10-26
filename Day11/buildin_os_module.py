import os

#Get the current working directory
print("Current Working Directory:", os.getcwd())
#List all files and directories in the current directory
print("Files and Directories in '", os.getcwd(), "':", os.listdir(os.getcwd()))
#Create a new directory
new_dir = "test"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory '{new_dir}' created")
else:
    print(f"Directory '{new_dir}' already exists")    

#Rename the directory
renamed_dir = "retest"
if not os.path.exists(renamed_dir):
    os.rename(new_dir, renamed_dir)
else:
    print(f"Directory '{renamed_dir}' already exists to rename")    

list_dir=["retest","test","demo"]
#Remove the directory
for dir_name in list_dir:
    if os.path.exists(dir_name):
        os.rmdir(dir_name)
        print(f"Directory '{dir_name}' removed")
    else:
        print(f"Directory '{dir_name}' does not exist to remove")


#with open("sample.txt", "w") as f:
#    f.write("This is a sample file.")  


if os.path.exists("sample.txt"):
    print("File 'sample.txt' exists")
    print("File size:", os.path.getsize("sample.txt"), "bytes")
    print("File last modified time:", os.path.getmtime("sample.txt"))
    print("File last accessed time:", os.path.getatime("sample.txt"))
    os.rename("sample.txt", "sample_renamed.txt")
    print("File 'sample.txt' renamed to 'sample_renamed.txt'")

'''
import time
time.sleep(5)  # Sleep for 2 seconds to demonstrate time difference

os.remove("sample_renamed.txt")
print("File 'sample_renamed.txt' removed")
'''

# Check process id
print("Current Process ID:", os.getpid())
# Check parent process id
print("Parent Process ID:", os.getppid())

# Environment variables
print("Environment Variables:", os.environ['COMPUTERNAME'])

os.environ['MY_NAME']='TechGeekConnect'

print("MY_NAME Environment Variable:", os.environ['MY_NAME'])

print("My system name is :", os.name)
print("My system platform is :", os.sys.platform)
if os.sys.platform == "win32":
    print("This is a Windows system")
elif os.sys.platform == "linux":
    print("This is a Linux system")    

# permissions
#get current file name
file_name=os.path.basename(__file__)
os.chmod(file_name, 0o777)  # Read, write, execute for all    