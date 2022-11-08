import numpy as np
import scipy.linalg
import imageExt
from PIL import Image

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


def QRdec(arr):
    n = len(arr)
    Q = np.empty((n, n))
    u = np.empty((n, n))
    u[:, 0] = arr[:, 0]
    Q[:, 0] = u[:, 0] / np.linalg.norm(u[:, 0])
    for i in range(1, n):
        u[:, i] = arr[:, i]
        for j in range(i):
            u[:, i] -= (arr[:, i] @ Q[:, j]) * Q[:, j]
        Q[:, i] = u[:, i] / np.linalg.norm(u[:, i])
    R = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            R[i, j] = arr[:, j] @ Q[:, i]
    return Q, R


def diag_sign(A):
    "Compute the signs of the diagonal of matrix A"

    D = np.diag(np.sign(np.diag(A)))

    return D


def adjust_sign(Q, R):
    """
    Adjust the signs of the columns in Q and rows in R to
    impose positive diagonal of Q
    """

    D = diag_sign(Q)

    Q[:, :] = Q @ D
    R[:, :] = D @ R

    return Q, R


def eigenvector(arrA):
    C = np.matmul(np.array(arrA).transpose(), arrA)
    img = Image.fromarray(C, mode='L')
    img.save ('covarian.png')
    img.show()
    n = len(C)

    '''
    print("C aksen")
    print("len", len(C))
    print("len[0]",len(C[0]))
    print(C)
    
    C0 = np.copy(C)
    C1 = np.copy(C)
    diff = np.inf
    i = 0
    while (diff > 1e-12) and (i < 1000):
        C0[:, :] = C1
        Q, R = adjust_sign(*QRdec(C0))
        C1[:, :] = R @ Q
        diff = np.abs(C1 - C0).max()
        i += 1
    eigvals = np.diag(C1)
    print("eigvals:")
    print(eigvals)
    a = np.empty((len(eigvals), n, n))
    x = [[[0 for k in range(n)] for j in range(100)]
         for i in range(len(eigvals))]
    print(np.shape(x[0]))
    print(np.shape(x))
    for i in range(0, len(eigvals)):
        a[i] = np.subtract(np.multiply(np.identity(n), eigvals[i]), C)
        print(a[i])
        x[i] = scipy.linalg.null_space(a[i])
        print(x[i])
        print("\n")
    
    l = 0
    for k in range(len(eigvals)):
        for j in range (n):
            for i in range (100):
                if(not np.any(x[k][j][i])):
                    l += 1
    v = np.empty((l, n))
    l = 0
    for k in range(len(eigvals)):
        for j in range (n):
            for i in range (100):
                if(not np.any(x[k][j][i])):
                    v[l] = 
                    l += 1
    '''


imageExt.listOfPicExtract("../test/dataset//")
# convertARow(imageExt.arrPic)
arr = convertARow(imageExt.arrPic)

nilaiTengah(arr)
eigenvector(matrixA(selisih(mean, arr)))

'''
# nilaiTengah(arr)
# eigenvector(matrixA(selisih(mean, arr)))
C = ([[3,  -2,  0],
      [-2,  3,  0],
      [0,  0,  5]])
D = ([[3,  0],
      [8,  -1]])
eigenvector(C)
'''