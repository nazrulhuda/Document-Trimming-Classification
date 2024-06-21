import pandas as pd
import requests
import os

# Read the Excel file into a pandas dataframe
df = pd.read_excel('/home/shanto/Downloads/sdsd/Text track Doc Extraction Useful_ Not useful pages.xlsx')

# Filter rows with 'Bank Statement' in the 'Document Type' column
bank_stmts = df[df['Document Type'] == 'Bank Statement']

# Remove '/' from the 'Document Name' column
bank_stmts['Document Name'] = bank_stmts['Document Name'].str.replace('/', '')

# Remove 'Page', 'pg', 'Pg', and 'PG' from the 'Useful no of pages' column
bank_stmts['Useful no of pages'] = bank_stmts['Useful no of pages'].str.replace('Page', '').str.replace('pg', '').str.replace('Pg', '').str.replace('PG', '')

# Create a directory named 'BS' to save the downloaded files
os.makedirs('BS', exist_ok=True)

# Loop through each row in the filtered dataframe
for index, row in bank_stmts.iterrows():
    # Get the URL from the 'Related link' column
    url = row['Related link']
    
    # Get the file name from the 'Document Name' column and remove forward slashes
    filename = 'BS/' + row['Document Name'].replace('/', '')
    
    # Set the appropriate file extension based on the file type in the 'Related link' column
    file_ext = url.split('.')[-1].lower()
    if file_ext == 'pdf':
        filename += '.pdf'
    elif file_ext == 'doc' or file_ext == 'docx':
        filename += '.docx'
    else:
        # If the file type is not PDF or DOC, print a warning message and skip the file
        print(f"Warning: unsupported file type for URL {url}")
        continue
    
    # Download the file and save it in the 'BS' directory
    r = requests.get(url)
    open(filename, 'wb').write(r.content)
