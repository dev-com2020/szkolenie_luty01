from PyPDF2 import PdfFileReader

file = open('document-1.pdf','rb')
doc = PdfFileReader(file)

print(doc.numPages)
print(doc.isEncrypted)

print(doc.documentInfo)
print(doc.documentInfo['/CreationDate'])
print(doc.documentInfo['/Producer'])
print(doc.pages[1].extractText())

file.close()
