import requests

url="https://jsonplaceholder.typicode.com/posts/1"
data = {
    "title": "Adding Student",
    "body": "Sachin",
    "userId": 1,
    "Address":"Mumbai"
}
response = requests.put(url,json=data)
if response.status_code==200:
    print("Updated Successfully")
    print(response.json())
else:
    print("Failed to Update")    