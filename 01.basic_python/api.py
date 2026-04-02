import requests

# url = "https://httpbin.org/basic-auth/user/pass"
url = 'https://jsonplaceholder.typicode.com/todos/1'
response = requests.get(url)
print(response.json())