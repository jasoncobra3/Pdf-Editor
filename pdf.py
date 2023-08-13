import PyPDF2
from PyPDF2 import PdfReader
from  PyPDF2 import  PdfWriter

def ext_text():
    reader = PdfReader("Abstarct.pdf")#you can use file path also
    numer = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(text)


def search():
    src=open("Abstarct.pdf","rb")
    read1=PyPDF2.PdfReader(src)
    txt=input("Enter the text you want to search:")
    for page_num in range(len(read1.pages)):
        page = read1.pages[page_num]
        text = page.extract_text()
        if txt in text:
            print(f"Found '{txt}' on page {page_num + 1}")
    src.close()

def ext_image():
    reader = PdfReader("Abstarct.pdf")

    page = reader.pages[0]
    count = 0
    if page in page.images:
        for image_file_object in page.images:
            with open(str(count) + image_file_object.name, "wb") as fp:
                fp.write(image_file_object.data)
                count += 1
    else:
        print("This image do not contain any image!")


def encrypt():
    password=input("Enter the password:")
    reader = PdfReader("Abstarct.pdf")
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt("password")

    with open("encrypted_pdf.pdf", "wb") as f:
        writer.write(f)

def decrypt():
    reader = PdfReader("encrypted_pdf.pdf")
    writer = PdfWriter()

    if reader.is_encrypted:
        reader.decrypt("password")

    for page in reader.pages:
        writer.add_page(page)

    with open("decrypted_pdf.pdf", "wb") as f:
        writer.write(f)

def merge():
    merger = PdfWriter()

    for pdf in ["Abstarct.pdf","traffic signal.pdf"]:
        merger.append(pdf)

    merger.write("merged-pdf.pdf")
    merger.close()

def compressor():
    reader = PdfReader("Abstarct.pdf")
    writer = PdfWriter()

    for page in reader.pages:
        page.compress_content_streams()
        writer.add_page(page)

    with open("compressed.pdf", "wb") as f:
        writer.write(f)

while(True):
    print("$$$$$$$$$$$$--------PDF EDITOR-------------$$$$$$$$$$$$$$$$")
    print("Select the opeation to perform on PDF!")
    print("\n 1.Extract Text \n 2.Search Words \n 3. Compress PDF \n 4.Merge PDF \n 5.Extract image \n 6. Encrypt PDF \n 7. Decrypt PDF \n 8.Exit")
    a=int(input("Enter your choice : "))
    if a==1:
        ext_text()
    elif a==2:
        search()
    elif a==3:
        compressor()
    elif a==4:
        merge()
    elif a==5:
        ext_image()
    elif a==6:
        encrypt()
    elif a==7:
        decrypt()
    elif a==8:
        print("Thank you for using my pdf editor!")
        break

