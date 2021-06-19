import PyPDF2, os

YourCWD = os.getcwd()   # To know Your Current Working Directory
print(YourCWD)             



#os.chdir("")   #Change it to Your Dir

mypdf_1 = open("File1.pdf", "rb")   #your first  PDF File
mypdf_2 = open("File2.pdf", "rb")   #your Second PDF File

readpdf_1 = PyPDF2.PdfFileReader(mypdf_1)
readpdf_2 = PyPDF2.PdfFileReader(mypdf_2)

writer = PyPDF2.PdfFileWriter()

for pageNum in range(readpdf_1.numPages):
    page = readpdf_1.getPage(pageNum)
    writer.addPage(page)  

for pageNum in range(readpdf_2.numPages):
    page = readpdf_2.getPage(pageNum)
    writer.addPage(page)


outputFile = open("CombiledFile.pdf", "wb")
writer.write(outputFile)
outputFile.close()
mypdf_1.close()
mypdf_2.close()
 
