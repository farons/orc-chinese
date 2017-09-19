from operation import ReadPic
from operation import PATH_OCR,PATH_PIC,PATH_TESSDATE

PATH_OCR = r'C:/Program Files/Tesseract-OCR/tesseract'
PATH_TESSDATE = r'C:/Program Files/Tesseract-OCR/tessdata'
PATH_PIC = r'TEST/picture/chinese.png'

read  = ReadPic()
code  = read.readPicBylocal(PATH_OCR, PATH_TESSDATE, PATH_PIC)
# code = read.readPicByPyt(PATH_PIC)
print(code)
file_object = open(r'TEST/chinese.txt', 'w', encoding= 'utf8')
file_object.write(code)
file_object.close( )
