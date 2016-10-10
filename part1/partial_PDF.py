from easygui import *
from PyPDF2 import PdfFileReader, PdfFileWriter

# choose and open a PDF file
input_file_name = fileopenbox("", "Choose a file", "*.pdf")
if input_file_name is None: # exit on "Cancel"
    exit()

# page length of the PDF file
input_file = PdfFileReader(open(input_file_name, "rb"))
total_pages = input_file.getNumPages()

# enter box
## beginning
msg_b = "Choose a biginning page"
begin = enterbox(msg_b, "Biginning Page")
while (not begin.isdigit() or begin == "0" or int(begin)>total_pages):
    msgbox("Error: Provide a valid number", "Error", "OK")
    begin = engerbox(msg_b, "Biginning Page")
    if begin is None:   # exit on "Cancel
        exit()

## last
msg_l = "Choose a last page"
last = enterbox(msg_l, "Last Page")
while (not last.isdigit() or last == "0" or
       int(begin)>total_pages or int(begin) > int(last)):
    msgbox("Error: Provide a valid number", "Error", "OK")
    last = engerbox(msg_l, "Biginning Page")
    if last is None:   # exit on "Cancel
        exit()

# save
output_file_name = filesavebox("", "Save the PDF file as...", "*.pdf")
while input_file_name == output_file_name: # cannot use same file as input
    msgbox("Cannot overwrite original file!", "Please choose another file...")
    output_file_name = filesavebox("", "Save the rotated PDF as...", "*.pdf")
if output_file_name is None:
    exit() # exit on "Cancel"

# read in file, set new page range
output_PDF = PdfFileWriter()

for pg_num in range(int(begin)-1, int(last)):
    page = input_file.getPage(pg_num)
    output_PDF.addPage(page)

output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()
