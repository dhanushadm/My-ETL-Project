import json
import csv
path = r"C:\Users\dhanu\OneDrive\Desktop\etl_project\raw_data\data.json"
with open(path,"r") as json_file:
    data=json.load(json_file)
extracted_data=[]
for item in data:
    extracted_data.append({
        "id":item.get("id"),
        "title":item.get("title"),
        "price":item.get("price")
    })

csv_file_path=r"C:\Users\dhanu\OneDrive\Desktop\etl_project\transformed_data\data.csv"
with open(csv_file_path,"w") as csv_file:
    writer=csv.DictWriter(csv_file, fieldnames=['id','title','price'])
    writer.writeheader()
    writer.writerows(extracted_data)
print("Data saved successfully")
