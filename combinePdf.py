import os
from pyPdf import PdfFileWriter, PdfFileReader

# Creating an object where pdf pages are appended to
output = PdfFileWriter()

# Creating a routine that appends files to the output file


def append_pdf(ipFile, output=output):
    [output.addPage(ipFile.getPage(page_num)) for page_num in range(ipFile.numPages)]

appendFile = True
filesToCombine = False

while appendFile:
    ip = raw_input("Provide file along with absolute path (or) Type 'quit':\n")
    if ip == 'quit':
        if filesToCombine:
            fh = open("output.pdf", "wb")
            output.write(fh)
            fh.close()
        else:
            print 'INFO: No files to combine'
        appendFile = False
    else:
        if os.path.isfile(ip):
            append_pdf(PdfFileReader(open(ip, "rb")))
            filesToCombine = True
