import requests
url="https://fakestoreapi.com/products"
response=requests.get(url)
if response.status_code == 200:
    print(response.json())
else:
    print("exited")