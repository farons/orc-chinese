
from operation import ReadPic, FileOperation
from operation import PATH_OCR, PATH_PIC, PATH_TESSDATE

PATH_OCR = r'C:/Program Files/Tesseract-OCR/tesseract'
PATH_TESSDATE = r'C:/Program Files/Tesseract-OCR/tessdata'

PATH_PIC = r'TEST/picture/1041.jpg'
OPEN_FIlE = r'TEST/result/init/1041.txt'
WRITE_FIlE = r'TEST/result/clear/1041.txt'
LAST_FILE = r'TEST/result/standard/1041.txt'

file = FileOperation()      # get object
readImage = ReadPic()

code = readImage.readPicByPyt(PATH_PIC,11)      # get word form picture 

file.writeFile(code,OPEN_FIlE)      # write in init
file.clearBL(OPEN_FIlE,WRITE_FIlE)      # write in clear

file.standardFile(WRITE_FIlE, LAST_FILE)
data = readImage.getData(LAST_FILE)        # get DATA= {"ID":"","title":""}
print(data)