from PIL import Image
from numpy import array
import os
from glob import glob

global arrPic
arrPic = []


def picExtract(dir, i):
    i += 1
    im_1 = Image.open(
        dir).convert('L')

    im_1 = im_1.resize((256, 256), Image.ANTIALIAS)
    '''
    w, h = im_1.size
    print("width", w, "\n")
    print("heigth", h, "\n")
    '''
    ar = array(im_1)
    return ar


def listOfPicExtract(dirpath):
    # List of name file
    filename_list = glob(os.path.join(
        dirpath, "*.jpg"))
    i = 0
    for filename in filename_list:
        i += 1
        arrayPic = picExtract(filename, i)

        arrPic.append(arrayPic)


listOfPicExtract("../test/dataset//")
print("len", len(arrPic))
print("len[0]", len(arrPic[0]))
print("len[0][0]", len(arrPic[0][0]))

'''
for i in range (0, len(arrPic)):
    print(arrPic[i])
    print("\n\n")
'''
