import requests
import json
url="https://fakestoreapi.com/products"
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    path = r"C:\Users\dhanu\OneDrive\Desktop\etl_project\raw_data\data.json"
    with open(path,"w") as json_file:
        json.dump(data,json_file)
    print("saved successfully")
else:
    print("exited")

