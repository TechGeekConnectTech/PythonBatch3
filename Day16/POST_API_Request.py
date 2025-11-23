import requests

url="https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "Adding Student",
    "body": "Sachin",
    "userId": 1,
    "Address":"Wagholi"
}
response = requests.post(url,json=data)
print(response.status_code)
print(response.json())