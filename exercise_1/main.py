from lxml import etree  # Import the etree module from the lxml library for XML parsing.
from pathlib import Path  # Import Path from pathlib to handle file paths.

# Define the directory containing the XML file by getting the current working directory and appending 'data' to it.
data_dir = Path.cwd() / 'data'

# Define the path to the XML file by appending the file name to the data directory.
sample_xml_file = data_dir / 'sample.xml'

# Parse the XML file and create an ElementTree object representing the XML structure.
tree = etree.parse(sample_xml_file)

"""
The code above is the same for reading an xml file in week_5/exercise_2/main.py
"""

# Use a valid XPath expression to select elements
result = tree.xpath('/bookstore/book[price>35.00]/child::*/text()')  # Adjust this XPath based on your XML structure

# Print the result
print(result)

