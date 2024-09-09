# Pdf-file-merger
A quick way to merge multiple pdf files into one pdf file using python.

## Installation
pip install -r requirements.txt
 
## Usage
1. Change the base_directory to the directory path which contains the pdf files (or all subdirectories leading to the files) you want to merge in the main.py file.
2. Use ```python main.py``` 
3. The merged pdf file will be saved in the base_directory with the name "merged_pdf.pdf" 

Note: The pdf files will be merged in the order they are found in the directory and only include files with the .pdf extension from the same directory.
