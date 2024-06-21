import os
import fitz
import easyocr

class PDFConverter:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.reader = easyocr.Reader(['en'])

    def convert(self):
        # Create output folder if it doesn't already exist
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        # Iterate through all files in the input folder
        for filename in os.listdir(self.input_folder):
            # Skip non-PDF files
            if not filename.endswith(".pdf"):
                continue
            
            # Construct input and output paths for this file
            input_path = os.path.join(self.input_folder, filename)
            output_path = os.path.join(self.output_folder, os.path.splitext(filename)[0] + ".txt")
            
            # Determine if PDF document is text-based or scan-based
            is_text_based = self.is_text_based(input_path)
            
            # Only extract text from single page documents
            if len(fitz.open(input_path)) == 1:
                # Use fitz to extract text from text-based PDF documents
                if is_text_based:
                    self.extract_text_fitz(input_path, output_path)
                # Use EasyOCR to extract text from scan-based PDF documents
                else:
                    self.extract_text_ocr(input_path, output_path)

    def is_text_based(self, input_path):
        with fitz.open(input_path) as doc:
            # Iterate through each page in the document
            for page in doc:
                # Check if page contains any text objects
                text_objects = page.get_text("text")
                if text_objects:
                    return True
        return False
    
    def extract_text_fitz(self, input_path, output_path):
        with fitz.open(input_path) as doc:
            # Extract the text from the single page document
            page = doc[0]
            text = page.get_text()
                
            # Save the page text to the output file
            with open(output_path, "w") as out_file:
                out_file.write(text)

    def extract_text_ocr(self, input_path, output_path):
        with fitz.open(input_path) as doc:
            # Extract the image from the single page document
            page = doc[0]
            pix = page.get_pixmap()
            img = fitz.Pixmap(pix)
            img.save(f"{self.output_folder}/page.png")
            
            # Read text from the page image with EasyOCR
            result = self.reader.readtext(f"{self.output_folder}/page.png")
            
            # Save the OCR text to the output file
            with open(output_path, "w") as out_file:
                for line in result:
                    out_file.write(line[1])
                    out_file.write("\n")
                    
            # Delete the temporary image file
            os.remove(f"{self.output_folder}/page.png")

# Input folder path containing the files to be converted
input_folder = '/home/shanto/Downloads/sdsd/test/not important'

# Output folder path to save the converted text files
output_folder = '/home/shanto/Downloads/sdsd/test/dataset/not important'

converter = PDFConverter(input_folder, output_folder)
converter.convert()