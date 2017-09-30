# Coding: utf-8
# Author: faron
# E-mail: yanzhilongll@163.com
#   Time: 2017-9-26 
from operation import ReadPic, FileOperation
from operation import PATH_OCR, PATH_PIC, PATH_TESSDATE

PATH_OCR = r'C:/Program Files/Tesseract-OCR/tesseract'
PATH_TESSDATE = r'C:/Program Files/Tesseract-OCR/tessdata'

PATH_PIC = r'TEST/picture/61.bmp'
OPEN_FIlE = r'TEST/result/init/61.txt'
WRITE_FIlE = r'TEST/result/clear/61.txt'
LAST_FILE = r'TEST/result/standard/61.txt'

file = FileOperation()      # get object
readImage = ReadPic()

code = readImage.readPicByPyt(PATH_PIC,11)      # get word form picture 

file.writeFile(code,OPEN_FIlE)      # write in init
file.clearBL(OPEN_FIlE,WRITE_FIlE)      # write in clear

file.standardFile(WRITE_FIlE, LAST_FILE)