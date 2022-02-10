#importing Libs
from pdf2image import convert_from_path
import os
import shutil
poppler_path = r"Utils\poppler\Library\bin"

#starting The Process
while True:
    print("==============================PDF To Image Converter by @tr0j3n==============================")

    #Getting The PDF File
    pdf_file = input("\n\nPATH To The PDF File: ")

    #Getting The Folder Name To Store Files
    xoxo =input("\nEnter a Name For The Folder: ")

    os.mkdir(xoxo)

    #Copying The PDF file To The Folder That mentioned Above
    original = pdf_file
    target = xoxo+r'\convert.pdf'

    shutil.copyfile(original, target)
    pdf_file = target

    #Converting
    pages = convert_from_path(pdf_file,poppler_path=poppler_path)


    img_file = pdf_file.replace(".pdf","")



    count = 0
    for page in pages:
        count+= 1
        jpeg_file = img_file + "-" +str(count) + ".jpg"
        page.save(jpeg_file, 'JPEG')

    #deleting The PDF file In The Folder That we created
    os.remove(target)
    print("successfully Converted The PDF\n\n")

    #asking For Another Run
    x = input("Do You Want To Continue Converting Files?\n IF You Want Type = y\n Else Press Enter:  ")
    if x == "y":
        continue
    else:
        break
              
