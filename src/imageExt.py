from PIL import Image
from numpy import array
import os
from glob import glob


def picExtract(dir):
    im_1 = Image.open(
        dir).convert('L')
    ar = array(im_1)
    return ar


def listOfPicExtract(dirpath):
    # List of name file
    filename_list = glob(os.path.join(
        dirpath, "*.jpg"))

    arrPic = []
    for filename in filename_list:
        arrayPic = picExtract(filename)

        arrPic.append(arrayPic)

    return arrPic


'''
array = listOfPicExtract("../test/dataset//")
for i in range (0, len(array)):
    print(array[i])
    print("\n\n")
'''
