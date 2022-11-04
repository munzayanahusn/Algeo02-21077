from PIL import Image
from numpy import array
import os
from glob import glob

global arrPic
arrPic = []

def picExtract(dir):
    im_1 = Image.open(
        dir).convert('L')
    ar = array(im_1)
    return ar

def listOfPicExtract(dirpath):
    # List of name file
    filename_list = glob(os.path.join(
        dirpath, "*.jpg"))

    for filename in filename_list:
        arrayPic = picExtract(filename)

        arrPic.append(arrayPic)

'''
listOfPicExtract("../test/dataset//")
print("len", len(arrPic))
print("len[0]",len(arrPic[0]))
print("len[0][0]",len(arrPic[0][0]))

for i in range (0, len(arrPic)):
    print(arrPic[i])
    print("\n\n")
'''