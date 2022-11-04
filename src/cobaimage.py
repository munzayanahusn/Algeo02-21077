from PIL import Image
from numpy import array
import os
from glob import glob


def picExtract(dir):
    im_1 = Image.open(
        dir).convert('L')
    ar = array(im_1)
    return ar


dir = "../test/dataset/5pixel.jpg"
arrayPic = picExtract(dir)
print(arrayPic)

# List of name file
filename_list = glob(os.path.join(
    r"test/dataset\\", "*.jpg"))

for filename in filename_list:
    print(filename)

'''
# folder path
dir_path = r'D:\PROGRAM KULIAH\TUBES ALGEO 2\Algeo02-21077\test\dataset\\'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)

'''
