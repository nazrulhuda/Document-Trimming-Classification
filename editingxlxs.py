import pandas as pd
import re

# Read the input Excel file
df = pd.read_excel('/home/shanto/Downloads/sdsd/test/file_namesFinal_List (3)(1).xlsx')

# Update the "Useful no of pages" column for all rows
df['Useful no of pages'] = df['Useful no of pages'].astype(str).apply(lambda x: re.findall(r'\d+', x))
df['Useful no of pages'] = df['Useful no of pages'].apply(lambda x: [int(i.replace("-", ",")) for i in x])
df['Useful no of pages'] = df['Useful no of pages'].apply(lambda x: "{" + ",".join(str(i) for i in x) + "}" if x else "{0}")

# Save the updated data to a new Excel file
df.to_excel('/home/shanto/Downloads/sdsd/test/Updated_file_namesFinal_List (3)(1).xlsx', index=False)