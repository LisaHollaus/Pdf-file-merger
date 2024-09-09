import PyPDF2
import os

# Setting the base directory to the directory containing the PDF files or subdirectories
base_directory = r"C:\Users\user\Documents\PDFs"  # Change this to the directory containing the PDF files or subdirectories

# Loop through all the directories and subdirectories in the base directory
for root, dirs, files in os.walk(base_directory):
    # make sure there are no merged PDFs in the current directory
    # if there are, remove them, so they don't get merged again
    if "merged-pdfs.pdf" in files:
        files.remove("merged-pdfs.pdf")

    # if there are less than 2 pdfs in the current directory, skip it
    if len([file for file in files if file.endswith(".pdf")]) < 2:
        continue

    # Create a PdfMerger object
    merger = PyPDF2.PdfMerger()

    # Loop through all the files in the current directory
    for file in files:
        if file.endswith(".pdf"):
            try:
                merger.append(os.path.join(root, file))
            except PyPDF2.errors.PdfReadError:
                print(f"Could not read file: {file}")
                continue

    # Write the merged PDF to a file if it's not empty
    if merger.pages:
        merger.write(os.path.join(root, "merged-pdfs.pdf"))

    merger.close()
