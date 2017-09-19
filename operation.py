PATH_OCR = ""
PATH_PIC = ""
PATH_TESSDATE = ""

class ReadPic(object):
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
        code = pytesseract.image_to_string(image, lang='chi_sim', config=tessdata_dir_config)
        return code
    
    def readPicByPyt(self, pathOfPic):
        """
        This function is through pytesseract to open picture to go back to the characters in image 
        """
        try:
            import Image
        except ImportError:
            from PIL import Image
        import pytesseract

        image = Image.open(pathOfPic)
        code = pytesseract.image_to_string(image)
        return code
