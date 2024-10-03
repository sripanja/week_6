import json  # Import the built-in json module to parse and work with JSON data
import pprint  # Import pprint to pretty-print the JSON data in a readable format
from pathlib import Path  # Import Path from pathlib to handle file paths in a platform-independent way

# Set the directory where the JSON file is located
data_dir = Path.cwd() / 'data'  # Path.cwd() gives the current working directory, and 'data' is appended to it

# Specify the path to your JSON file inside the data directory
file_path = data_dir / 'sample_2.json'  # Create a full file path by combining the directory and the JSON file name

# Open the JSON file in read mode ('r') using a context manager (with statement)
with open(file_path, 'r') as file:
    data = json.load(file)  # Load JSON data from the file and convert it into a Python dictionary

# Pretty-print the contents of the JSON file for better readability
pprint.pprint(data)

import json
from pathlib import Path

# Sample Python dictionary (this will be converted to JSON)
data = {
    "phone": "+1-555-555-1234",
    "email": "john.doe@example.com",
    "address": {
        "street": "1234 Elm Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10001",
        "country": "USA"
    }
}
# Set the directory where the JSON file will be saved
data_dir = Path.cwd() / 'data'

# Specify the file path where you want to write the JSON data
file_path = data_dir / 'contact.json'

# Open the file in write mode ('w')
with open(file_path, 'w', encoding='utf8') as file:
    # Use json.dump() to write the Python dictionary to the file as JSON
    json.dump(data, file, indent=4)  # 'indent=4' makes the JSON output more readable (pretty-printing)

print(f"Data written to {file_path}")
