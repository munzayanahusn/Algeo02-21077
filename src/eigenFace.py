
from turtle import xcor
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
    print("len[0]", len(diff[0]))

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


# Ini nyari eig vector yg pake QR
# trus setelah diliat2 lagi kyknya cuma perlu K eig value terbesar gitu kan jadi nyoba power method

def Q_i(Q_min, i, j, k):
    if i < k or j < k:
        return float(i == j)
    else:
        return Q_min[i-k][j-k]

def QRDec(A):
    n = len(A)
    R = A
    Q = np.zeros((0, 0))
    for k in range(n-1):                                                                 
        I = np.identity(n)
        x = [row[k] for row in R[k:]]
        e = [row[k] for row in I[k:]]
        alpha = np.sign(x[0]) * np.sqrt(sum([x_i**2 for x_i in x]))
        u = list(map(lambda p,q: p + alpha * q, x, e))
        norm_u = np.sqrt(sum([u_i**2 for u_i in u]))
        v = list(map(lambda p: p/norm_u, u))
        Q_min = [ [float(i==j) - 2.0 * v[i] * v[j] for i in range(n-k)] for j in range(n-k) ]
        Q_t = [[ Q_i(Q_min,i,j,k) for i in range(n)] for j in range(n)]
        if(k == 0): Q = Q_t  
        else: Q = np.matmul(Q_t,Q)
        R = np.matmul(Q_t,R)
    return np.transpose(Q), R
'''


def eigenvector(arrA):
    print("A")
    print(len(arrA))
    print(len(arrA[0]))
    # Mencari matriks covarian C = transpose(A) x A
    At = np.array(arrA).transpose()
    # print("At")
    # print(At)
    C = np.matmul(At, arrA)
    # print("Covarian")
    # print(C)
    
    img = Image.fromarray(np.uint8(C), mode='L')
    img.save('../test/tryset/covarian.png')
    print(img.size)

    '''
    (eigval, eigvector) = np.linalg.eig(C)
    print("---")
    print(eigval)

    temp = np.hsplit(eigvector, 1)
    for i in range(0, len(temp)):
        eigface = np.matmul(arrA, temp[i])
        eigface.reshape(eigface,(256,256,-1))

        dir = '../test/tryset/face' + str(i) + '.png'
        img = Image.fromarray(np.uint8(eigface), mode='L')
        img.save(dir)

    ''
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
    C1 = np.copy(C)
    n = len(C)
    QQ = np.identity(n)
    for k in range(50000):
        Q, R = QRDec(C1)
        C1 = R @ Q
        QQ = QQ @ Q
    eigvals = np.diag(C1)
    a = np.empty((len(eigvals), n, n)) 
    #x = [[[0 for k in range (n)] for j in range (100)] for i in range (len(eigvals))]
    #x = np.empty((len(eigvals), n, n))
    cntv = 0
    eigvecs = np.empty((n, 1))
    countsplit = 1
    for i in range (0, len(eigvals)):
        a[i] = np.subtract(np.multiply(np.identity(n), eigvals[i]), C)
        x = scipy.linalg.null_space(a[i])
        b, c = np.shape(x)
        if(c > 0): 
            countsplit += 1
            x = np.hsplit(x, c)
            for i in range(len(x)):
                eigvecs = np.concatenate((eigvecs, x[i]))
    eigvecs = np.vsplit(eigvecs, countsplit)
    return eigvecs

#ini power method
'''
def normalize(x):
    fac = abs(x).max()
    x_n = x / x.max()
    return fac, x_n

def powermethod(arr):
    n = len(arr)
    eigvec = np.ones(n)
    eigval = 0
    for i in range(1000):
        eigvec = np.dot(arr, eigvec)
        eigval, eigvec = normalize(eigvec)
    return eigval, eigvec

shifted power method buat nyari K largest eigen valuenya masih belum bener, jadi bar bisa nyari 1 largest euigval
def calceigfaces(C, K = 3):
    n = len(C)
    eigfaces = np.empty((K, n))
    first_eigval, first_eigvec = powermethod(C)
    eigfaces[0] = first_eigvec
    C -= (first_eigval * np.identity(n))
    eigval, eigvec = powermethod(C)
    for i in range(1, K):
        eigfaces[i] = eigvec
        print(eigval)
    return eigfaces
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
#nilaiTengah(arr)
#eigenvector(matrixA(selisih(mean, arr)))
C = ([[ 3,  -2,  0],
       [ -2,  3,  0],
       [ 0,  0,  5]])
D = ([[ 3,  0],
      [ 8,  -1]])
'''
eigval, arr = powermethod(C)
print(eigval)
print(arr)
'''