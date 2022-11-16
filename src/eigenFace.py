
from turtle import xcor
import numpy as np
import scipy.linalg
import imageExt
from PIL import Image

global mean
mean = []


def convertSquareMatrix(arr):
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


def convertOneRow(arr):
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
    # Mencari average face training
    for i in range(0, len(arr)):
        sum = 0
        for j in range(0, len(arr[i])):
            sum += arr[i][j]

            # print("mean", sum/len(arr))
        mean.append(np.int_(sum/len(arr[i])))
    # Save average
    convMean = convertSquareMatrix(mean)
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
    return diff
    '''
    # Save image selisih
    for i in range(0, len(diff[0])):
        temp = []
        for j in range(0, len(diff)):
            temp.append(diff[j][i])

        arrDiff = convertSquareMat(temp)
        # print(arrDiff)

        dir = '../test/tryset/selisih' + str(i) + '.png'
        img = Image.fromarray(np.uint8(arrDiff), mode='L')
        img.save(dir)
    
    print("Selisih")
    # print(diff)
    print("len", len(diff))
    print("len[0]", len(diff[0]))
    '''


def covarian(A):
    # Mencari matriks covarian C = transpose(A) x A
    At = np.transpose(A)
    # print("At")
    # print(At)
    C = (np.matmul(At, A))
    # print("Covarian")
    # print(C)
    img = Image.fromarray(np.uint8(C), mode='L')
    img.save('../test/tryset/covarian.png')
    #print(img.size)
    return C

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
        u = list(map(lambda p, q: p + alpha * q, x, e))
        norm_u = np.sqrt(sum([u_i**2 for u_i in u]))
        v = list(map(lambda p: p/norm_u, u))
        Q_min = [[float(i == j) - 2.0 * v[i] * v[j] for i in range(n-k)] for j in range(n-k)]
        Q_t = [[Q_i(Q_min, i, j, k) for i in range(n)] for j in range(n)]
        if(k == 0):
            Q = Q_t
        else:
            Q = np.matmul(Q_t, Q)
        R = np.matmul(Q_t, R)
    return np.transpose(Q), R

def eigenvector(C):
    C1 = np.copy(C)
    n = len(C)
    QQ = np.identity(n)
    for k in range(1000):
        Q, R = QRDec(C1)
        C1 = np.matmul(R, Q)
        QQ = np.matmul(QQ, Q)
    eigvals = np.diag(C1)
    a = np.empty((len(eigvals), n, n))
    eigvecs = np.empty((n, 1))
    countsplit = 0
    for i in range(0, len(eigvals)):
        a[i] = np.subtract(np.multiply(np.identity(n), eigvals[i]), C)
        x = scipy.linalg.null_space(a[i])
        b, c = np.shape(x)
        if(c > 0):
            countsplit += 1
            x = np.hsplit(x, c)
            for j in range(len(x)):
                if(countsplit == 0 and j == 0):
                    eigvecs = x[j]
                else:
                    eigvecs = np.concatenate((eigvecs, x[j]))
        eigvecs = np.delete(eigvecs, 0, 0)
    eigvecs = np.vsplit(eigvecs, countsplit)
    return eigvecs

def calceigface(A, eigvecs):
    for i in range (0, len(eigvecs)):
        eigvecs[i] = np.dot(A, eigvecs[i])
    return eigvecs

def reconstruct(eigface, diff, k):
    weights = np.zeros((len(diff[0]),k))
    rec_face=[]
    for i in range(len(diff[0])):
        w = np.dot(eigface, diff[:,i])
        weights[i,:] = w
        face = np.dot(w, eigface)
        face = face + np.transpose(meann)
        reshape_face = np.reshape(face, (256,256))
        rec_face.append(reshape_face)
    return rec_face

def projectquery(eigface, normquery, k):
    weights = np.zeros((len(eigface),k))
    for i in range(len(eigface)):
        w = np.dot(eigface, normquery)
        w = np.reshape(w, (len(w), ))
        weights[i,:] = w
        face = np.dot(w, eigface)
        face = face + np.transpose(meann)
        reshape_face = np.reshape(face, (256,256))
    return reshape_face

def eucdist(arr1, arr2):
    arr1 = np.ravel(arr1)
    arr2 = np.ravel(arr2)
    temparr = arr1 - arr2
    sum_sq = np.dot(np.transpose(temparr), temparr)
    return np.sqrt(sum_sq)
    
def findface(prq, rec_face, th = 80):
    mindist = eucdist(prq, rec_face[0])
    idxclosestface = 0
    for i in range(1, len(rec_face)):
        print("mindist: " + str(mindist))
        currdist = eucdist(prq, rec_face[i])
        print("curdist: " + str(currdist))
        if(mindist > currdist):
            mindist = currdist
            idxclosestface = i
    #if(mindist > th): 
        #idxclosestface = -1
    return idxclosestface


# PROGRAM UTAMA

# Training Image
imageExt.listOfPicExtract("../test/dataset//")
arr = np.array(convertOneRow(imageExt.arrPic))
print(np.shape(arr))
meann = nilaiTengah(arr)
diff = np.array(selisih(meann, arr))

'''
for i in range(len(diff[0])):
    tempd = diff[:, i]
    tempd = (tempd-np.min(tempd))/(np.max(tempd)-np.min(tempd))
    tempd *= 255
    diff[:, i] = tempd
'''
for i in range(len(diff[0])):
    tempd = diff[:, i]
    tempd = (tempd-np.min(tempd))/(np.max(tempd)-np.min(tempd))
    tempd *= 255
    tempd = (np.reshape(diff[:, i], (256, 256)))
    dir = '../test/faceEigen/difface' + str(i) +'.png'
    img = Image.fromarray(np.uint8(tempd), mode='L')
    img.save(dir)

cov = np.uint8(covarian(diff))
eigv = eigenvector(cov)
eigface = calceigface(diff, eigv)
eigface = np.reshape(eigface, (len(eigface), 65536))

'''
for i in range(len(eigface)):
    temp = eigface[i]
    temp = (temp-np.min(temp))/(np.max(temp)-np.min(temp))
    temp *= 255
    eigface[i] = temp
'''

for i in range(len(eigface)):
    temp = eigface[i]
    temp = (temp-np.min(temp))/(np.max(temp)-np.min(temp))
    temp *= 255
    temp = (np.reshape(eigface[i], (256, 256), 'A'))
    dir = '../test/faceEigen/face' + str(i) +'.png'
    img = Image.fromarray(np.uint8(temp), mode='L')
    img.save(dir)

rec_face = reconstruct(eigface, diff, len(eigface))

for i in range(len(rec_face)):
    tempr = rec_face[i]
    tempr = (tempr-np.min(tempr))/(np.max(tempr)-np.min(tempr))
    tempr *= 255
    rec_face[i] = tempr

for i in range(len(rec_face)):
    print(rec_face[i])
    tempr = (np.reshape(rec_face[i], (256, 256), 'A'))
    dir = '../test/faceEigen/recface' + str(i) +'.png'
    img = Image.fromarray(np.uint8(tempr), mode='L')
    img.save(dir)

#Query
query = np.reshape((imageExt.picExtract("../test/queryface.jpg")), (65536, 1))
normquery = np.array(selisih(meann, query))
prq = projectquery(eigface, normquery, len(eigface))
prq = (prq-np.min(prq))/(np.max(prq)-np.min(prq))
prq *= 255
print("---------- prq -------------")
print(prq)
print("------------------------")
tempprq = (np.reshape(prq, (256, 256), 'A'))
dir = '../test/faceEigen/prq' +'.png'
img = Image.fromarray(np.uint8(tempprq), mode='L')
img.save(dir)
idxclosestface = findface(prq, rec_face)
print(idxclosestface)
if(idxclosestface != -1): 
    closestface = arr[:,idxclosestface]
    tempc = (np.reshape(closestface, (256, 256)))
    tempc = (tempc-np.min(tempc))/(np.max(tempc)-np.min(tempc))
    tempc *= 255
    dir = '../test/Res/res.png'
    img = Image.fromarray(np.uint8(tempc), mode='L')
    img.save(dir)
#ini semua buat ngetes pake library numpy buat eigval eigvec

### BACKUP COMMENT ###
# ini power method
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

'''
C = ([[ 3,  -2,  0],
       [ -2,  3,  0],
       [ 0,  0,  5]])
D = ([[ 3,  0],
      [ 8,  -1]])

eigval, arr = powermethod(C)
print(eigval)
print(arr)
'''

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

# Coba pakai lib
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
