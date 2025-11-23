import requests

url="https://jsonplaceholder.typicode.com/posts/1"
response=requests.delete(url)
if response.status_code==200:
    print("Deleted Successfully")
else:
    print("Failed to Delete")