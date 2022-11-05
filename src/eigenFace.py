import numpy as np
import imageExt

global mean
mean = []


def convertARow(arr):
    arrConverted = []
    for i in range(0, len(arr)):
        temp = []
        for j in range(0, len(arr[i])):
            for k in range(0, len(arr[i][j])):
                temp.append(arr[i][j][k])
        arrConverted.append(temp)

    return arrConverted


def nilaiTengah(arr):
    for i in range(0, len(arr[0])):
        sum = 0
        for k in range(0, len(arr)):
            sum += arr[k][i]

            # print("mean", sum/len(arr))
        mean.append(sum/len(arr))

    print(mean)
    # print(mean)


def selisih(arrmean, arr):
    diff = []
    '''
    print("Selisih")
    print("len mean", len(arrmean))
    print("len arr",len(arr))
    print("len arr[1]", len(arr[1]))
    '''
    for k in range(0, len(arr)):
        temp = []
        for i in range(0, len(arr[k])):
            elmt = arr[k][i]-arrmean[i]
            temp.append(elmt)
        diff.append(temp)

    '''
    print("Selisih")
    print("len", len(diff))
    print("len[0]",len(diff[0]))
    print(diff)
    '''

    return diff


def matrixA(arr):
    A = []
    for i in range(0, len(arr[0])):
        temp = []
        for k in range(0, len(arr)):
            temp.append(arr[k][i])
        A.append(temp)
    # print(A)
    return A


def eigenvector(arrA):
    Caksen = np.matmul(np.array(arrA).transpose(), arrA)
    print("C aksen")
    print("len", len(Caksen))
    print("len[0]", len(Caksen[0]))
    print(Caksen)


imageExt.listOfPicExtract("../test/dataset//")
# convertARow(imageExt.arrPic)
arr = convertARow(imageExt.arrPic)
nilaiTengah(arr)
eigenvector(matrixA(selisih(mean, arr)))
