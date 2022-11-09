import numpy as np
import scipy.linalg
import imageExt
from PIL import Image

global mean
mean = []

# Cuma buat test


def convertSquareMat(arr):
    # Mengubah array (N^2)x1 menjadi array matriks semula
    arrConverted = []
    ctr = 0
    for i in range(0, 256):
        temp = []
        for j in range(0, 256):
            temp.append(arr[ctr])
            ctr += 1
        arrConverted.append(temp)

    return arrConverted


def convertARow(arr):
    # Mengubah array images MxNxN menjadi (N^2) x M
    arrConverted = []
    for i in range(0, len(arr[0])):
        for j in range(0, len(arr[0][0])):
            temp = []
            for k in range(0, len(arr)):
                temp.append(arr[k][i][j])
            arrConverted.append(temp)
    return arrConverted


def nilaiTengah(arr):
    # Mencari mean training
    for i in range(0, len(arr)):
        sum = 0
        for j in range(0, len(arr[i])):
            sum += arr[i][j]

            # print("mean", sum/len(arr))
        mean.append(sum/len(arr[i]))

    # print(mean)

    # Save average save
    convMean = convertSquareMat(mean)
    img = Image.fromarray(np.uint8(convMean), mode='L')
    img.save('../test/tryset/meanTraining.png')
    # print(convMean)
    return mean


def selisih(arrmean, arr):
    # Mencari selisih antara training image dengan nilai tengah
    diff = []
    for i in range(0, len(arr)):
        temp = []
        for j in range(0, len(arr[i])):
            elmt = arr[i][j]-arrmean[i]
            temp.append(elmt)
        diff.append(temp)
    
    '''
    for i in range(0, len(diff[0])):
        temp = []
        for j in range(0, len(diff)):
            temp.append(diff[j][i])

        arrDiff = convertSquareMat(temp)
        # print(arrDiff)

        dir = '../test/tryset/selisih' + str(i) + '.png'
        img = Image.fromarray(np.uint8(arrDiff), mode='L')
        img.save(dir)
    '''

    print("Selisih")
    # print(diff)
    print("len", len(diff))
    print("len[0]",len(diff[0]))

    return diff


'''
def matrixA(arr):
    # Menggabungkan face vector menjadi matriks ukuran N^2 * M.
    A = []
    for i in range(0, len(arr[0])):
        temp = []
        for k in range(0, len(arr)):
            temp.append(arr[k][i])
        A.append(temp)
    # print(A)
    return A
'''


def eigenvector(arrA):
    print("A")
    print(len(arrA))
    print(len(arrA[0]))
    # Mencari matriks covarian C = transpose(A) x A
    At = np.array(arrA).transpose()
    print("At")
    print(At)
    C = np.matmul(At, arrA)
    print("Covarian")
    print(C)
    img = Image.fromarray(np.uint8(C), mode='L')
    img.save('../test/tryset/covarian.png')
    print(img.size)
    
    (eigval, eigvector) = np.linalg.eig(C)
    print("---")
    print(eigval)
    '''
    eigface = np.matmul(eigvector, At)
    for i in range(0, len(eigface[0])):
        temp = []
        for j in range(0, len(eigface)):
            temp.append(eigface[j][i])

        arrFace = convertSquareMat(temp)
        # print(arrDiff)

        dir = '../test/tryset/face' + str(i) + '.png'
        img = Image.fromarray(np.uint8(arrFace), mode='L')
        img.save(dir)
    '''

    '''
    print("C aksen")
    print("len", len(C))
    print("len[0]",len(C[0]))
    print(C)
    '''


imageExt.listOfPicExtract("../test/dataset//")
'''
mat = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[11, 12, 13], [14, 15, 16], [17, 18, 19]], 
    [[21, 22, 23], [24, 25, 26], [27, 28, 29]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
    [[11, 12, 13], [14, 15, 16], [17, 18, 19]]]
    '''
arr = convertARow(imageExt.arrPic)
eigenvector(selisih(nilaiTengah(arr), arr))
# eigenvector(matrixA(selisih(mean, arr)))
