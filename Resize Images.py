import os
import PIL
from PIL import Image
import datetime
import pathlib

ImgSuffixes = ['.JPEG','.JPG','.PNG','.BMP']

Directory = input('Enter Directory: ')

Width = input('Enter width: ')

Height = input('Enter height: ')

Directory = Directory.replace('"','')

Counter = 0

if os.path.isdir(Directory):
        Files = os.listdir(Directory)
        for File in Files:
                Suffix = pathlib.Path(Directory + '\\' + File).suffix
                if Suffix.upper() in ImgSuffixes:
                        Counter = Counter + 1
                        IMG = Image.open(Directory + '\\' + File)
                        newIMG = IMG.resize((int(Width), int(Height)))
                        print(str(Counter) + '. Image: ' + File + ' has been resized!')
                        newIMG.save(Directory + '\\' + Width + 'x' + Height + '_' + File)
