import xml.etree.ElementTree as ET

# Replace 'path_to_your_file.xml' with the actual path of your XML file in Google Drive
file_path = 'OI_MDM_TO_BI_SoldTo.xml'
sink = 'OI_MDM_TO_BI_SoldTo.csv'
tree = ET.parse(file_path)
root = tree.getroot()



def flatten_xml(element):
    """
    Flattens an XML element into a dictionary and cleans the values.
    """
    flattened = {}

    for child in element:
        if len(child):
            flattened.update(flatten_xml(child))
        else:
            cleaned_value = child.text.strip() if child.text else ''
            flattened[child.tag] = cleaned_value.replace('\n', ' ').strip()

    return flattened



import pandas as pd

# Flatten each element in the root and store it in a list
flattened_data = [flatten_xml(elem) for elem in root]

# Convert the list of dictionaries into a DataFrame
df = pd.DataFrame(flattened_data)

df.to_csv(sink, index=False)