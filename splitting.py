import os
import shutil
import fitz
import pandas as pd
import re

# Read the Excel file with the important pages
important_pages_file = "/home/shanto/Downloads/sdsd/test/Updated_file_namesFinal_List (3)(1).xlsx"
important_pages_df = pd.read_excel(important_pages_file)

# Create the output folders if they don't already exist
if not os.path.exists("important"):
    os.mkdir("important")
if not os.path.exists("not important"):
    os.mkdir("not important")

# Loop through all files in the input folder
input_folder = "/home/shanto/Downloads/sdsd/test/Sample"
for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        # Check if the file is listed in the Excel file
        if filename not in important_pages_df["File Name"].tolist():
            continue
        
        # Check if the file has important pages
        file_df = important_pages_df.loc[important_pages_df["File Name"] == filename]
        if len(file_df) == 0:
            # No important pages specified for this file
            important_pages = set()
        else:
            # Get the set of important page numbers for this file
            page_nums_str = file_df["Useful no of pages"].iloc[0]
            print("2342")
            print (filename)
            
            print('dsad')
            page_nums_list = re.findall('\d+', page_nums_str)
            important_pages = set(map(int, page_nums_list))
            print(important_pages)
            print('dsad')
            if important_pages == {0}:
                print("deleting")
                print(filename)
                continue 
            
            print(f"Important pages for {filename}: {important_pages}")

        # Open the input PDF file and split it into separate pages
        with fitz.open(os.path.join(input_folder, filename)) as doc:
            for page_num in range(doc.page_count):
                # Check if the page is important
                if page_num + 1 in important_pages:
                    folder = "important"
                else:
                    folder = "not important"
                print("doing")
                print(filename)
                # Save the page to the appropriate folder
                page = doc.load_page(page_num)
                out_filename = f"{filename.split('.')[0]}_page{page_num+1}.pdf"
                out_path = os.path.join(folder, out_filename)
                page_rect = page.rect   # get page dimensions
                pdf_out = fitz.open()   # create a new PDF document
                pdf_out.insert_pdf(doc, from_page=page_num, to_page=page_num)  # insert the current page
                pdf_out.save(out_path)  # save the new PDF document

# Print a message when the script is done
print("Done")