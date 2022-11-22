from PIL import Image
from numpy import array
import os
from glob import glob

global arrPic, arrPiccolor
arrPic = []
arrPiccolor = []
global size
size = 256


def picExtract(dir):
    im_1 = Image.open(
        dir).convert('L')
    im_2 = Image.open(
        dir)
    im_1 = im_1.resize((size, size), Image.ANTIALIAS)
    im_2 = im_2.resize((size, size), Image.ANTIALIAS)
    '''
    w, h = im_1.size
    print("width", w, "\n")
    print("heigth", h, "\n")
    '''
    ar1 = array(im_1)
    ar2 = array(im_2)
    return ar1, ar2


def listOfPicExtract(dirpath):
    # List of name file
    filename_list = glob(os.path.join(
        dirpath, "*.jpg"))
        
    for filename in filename_list:
        arrayPic = picExtract(filename)
        arrayPic, arrayPiccolor= picExtract(filename)
        arrPic.append(arrayPic)
        arrPiccolor.append(arrayPiccolor)

'''
print("len", len(arrPic))
print("len[0]", len(arrPic[0]))
print("len[0][0]", len(arrPic[0][0]))


for i in range (0, len(arrPic)):
    print(arrPic[i])
    print("\n\n")
'''
