import json
from pathlib import Path

data_dir = Path.cwd() / 'data'

# Specify the path to your JSON file
file_path = data_dir / 'sample_1.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)  # Load JSON data as a Python dictionary
first_name =data['firstName']
print(f"first name: {first_name}")
age =data['age']
print(f"Age: {age}")
address =data['address']
print(f"address: {address}")
city =address['city']
print(f"city: {city}")
postalCode =address['postalCode']
print(f"postalCode: {postalCode}")

courses = data['courses']
for course in courses:
    print(f"courses: {courses}")