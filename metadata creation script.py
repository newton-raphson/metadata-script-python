'''Python Script to Obtain Metadata where traits are available in excel file'''
'''Excel File columns should be: Col1   indexes starting from 0
                                 Col2...ColN trait name in Column and values of traits              
                                            '''

import pandas as pd
import json
import os

# Set the path to the Excel file
# Replace with the name of the excel file you have
excel_file = 'Sample NFT Metadata.xlsx'
# Folder Name where metadata named to be stored
folder_name = 'metadata'

# Read the Excel file into a pandas dataframe
df = pd.read_excel(excel_file)
# to fill the empty cells with O 
df.fillna("0", inplace=True)
# Iterate through each row in the dataframe
for index, row in df.iterrows():
    # Create a dictionary to hold the data for the current row
    data_dict = {}
    data_dict[df.columns[0]] = f"Sample NFT #{row[df.columns[0]]}"
    # add your description here
    data_dict['description'] = f"Sample NFT description"
    data_dict["image"] = f"/{row[df.columns[0]]}.png"
    attributes=[]
    for col in df.iloc[:, 1:]:
        attributes.append({"trait_type":col,"value":row[col]})
        print(col)
    data_dict["attributes"]=attributes
    # Create a filename for the JSON file using the Name column
    json_file_name = f"{row[df.columns[0]]}.json"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    # Save the modified JSON data back to the file
    with open(folder_name+'/' + json_file_name, 'w') as file:
        json.dump(data_dict, file)

print("Done")
