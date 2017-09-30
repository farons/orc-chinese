# Coding: utf-8
# Author: faron
# E-mail: yanzhilongll@163.com
#   Time: 2017-9-26 
from matplotlib import pyplot as plt
import cv2
import re

PATH_OCR = ""
PATH_PIC = ""
PATH_TESSDATE = ""
PSM = ""

class ReadPic(object):
    """
    read words from images by using tesseract
    """
    def __init__(self):
        """"
        This function is to init class.
        """
        pass
    
    def readPicBylocal(self, pathOfOcr, pathOfTessData, pathOfPic):
        """
        This function is through the local program(exe) to open the picture to go back to the characters in image.
        pathOfOcr: the path of tesseract.exe
        pathOfPic: the path of picture
        the type of picture : JPG, GIF ,PNG , TIFF and so on.
        """
        try:
            import Image
        except ImportError:
            from PIL import Image
        import pytesseract
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # tessdata_dir_config = 'C:\Program Files\Tesseract-OCR\tessdata'
        tessdata_dir_config = pathOfTessData
        pytesseract.pytesseract.tesseract_cmd = pathOfOcr
        image = Image.open(pathOfPic)
        code = pytesseract.image_to_string(image, lang='normal', config=tessdata_dir_config)
        return code
    
    def readPicByPyt(self, pathOfPic, psm):
        """
        This function is through pytesseract to open picture to go back to the characters in image 
        """
        try:
            import Image
        except ImportError:
            from PIL import Image
        import pytesseract
        PSM = "-psm"+" "+str(psm)
        print(PSM)
        image = Image.open(pathOfPic)
        code = pytesseract.image_to_string(image, lang="chi_sim", config=PSM)
        return code

    # Author: faron
    #   Time: 2017-9-26 
    # def cvTest(self, filePath):
    #     """
    #     this is a test of cv2
    #     """
    #     img = cv2.imread(filePath)
    #     cv2.imshow("miao",img)
    #     cv2.waitKey(50000)

class FileOperation:
    """
    file operation
    """
    def __init__(self):
        pass

    def writeFile(self, string, newFilePath):
        """
        writing a string to a text file
        """
        file = open(newFilePath, 'w', encoding= 'utf8')
        file.write(string)
        file.close( )

        
    def clearBL(self, filePath, newFilePath):
        """
        clear blank lines in txt
        filePath: the path of txt file
        newFilePath: the new file path
        """
        try:
            file = open(filePath, "r", encoding= 'utf8')
            newFile = open(newFilePath, "w", encoding= 'utf8')
            lines = file.readlines()
            for li in lines:
                if li.split():
                    newFile.writelines(li)
            file.close()
            newFile.close()
        except Exception as e:
            print(e)
        finally:
            return newFile

    
    def isContainZh(self, words):
        for c in words:          # delete timeflag
            if '\u4e00' <= c <= '\u9fa5':
                return True
            
        return False
        
    def standardFile(self, filePath, newFilePath):
        """
        delete nums
        delete space
        delete useless content:Take ":" as the boundary

        """
        import  re
        
        try:
            file = open(filePath, "r", encoding= 'utf8')
            newFile = open(newFilePath, "w", encoding= 'utf8')
            lines = file.readlines()

            if not self.isContainZh(lines[0]):      # remove numbers
                del lines[0]

            del lines[0]        # remove invalid words at the head of file

            for li in lines:
                li = li.replace(" ","")     # remove spaces
                if ":" in li:       # delete useless content:Take ":" as the boundary
                    break
                newFile.writelines(li)
            file.close()
            newFile.close()
        except Exception as e:
            print(e)
        finally:
            return newFile


# WRITE_FIlE = r'TEST/result/clear/61.txt'
# LAST_FILE = r'TEST/result/standard/61.txt'

# file = FileOperation()      # get object

# file.standardFile(WRITE_FIlE, LAST_FILE)