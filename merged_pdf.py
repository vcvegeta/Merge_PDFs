from PyPDF2 import PdfWriter    # PdfWriter is the class imported from the PyPDF2 module
import os

merger = PdfWriter()        # PdfWriter() is a constructor method (i.e. __init__) of the PdfWriter class, merger is the object here. 
files = [file for file in os.listdir() if file.endswith(".pdf")]    # list comprehension

for pdf in files:
    print(pdf)
    merger.append(pdf)   # .append() is what merges the files.

merger.write("merged-pdf.pdf")  # The .write() method is used to save the final PDF into a new file on disk.
merger.close() 