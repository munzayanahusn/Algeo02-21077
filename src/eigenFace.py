#version
import time
import numpy as np
import scipy.linalg
import imageExt
from PIL import Image

global mean
mean = []
facenotfound = False

start = time.time()
def convertSquareMatrix(arr):
    # Mengubah array (N^2)x1 menjadi array matriks semula
    arrConverted = []
    ctr = 0
    for i in range(0, imageExt.size):
        temp = []
        for j in range(0, imageExt.size):
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
        mean.append(np.int_(sum/len(arr[i])))
    '''
    # Save average
    convMean = convertSquareMatrix(mean)
    img = Image.fromarray(np.uint8(convMean), mode='L')
    img.save('../test/tryset/meanTraining.png')
    # print(convMean)
    '''
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
    '''
    # print("Covarian")
    # print(C)
    img = Image.fromarray(np.uint8(C), mode='L')
    img.save('../test/tryset/covarian.png')
    #print(img.size)
    '''
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
        alpha = np.sign(x[0]) * np.linalg.norm(x)
        u = list(map(lambda p, q: p + alpha * q, x, e))
        norm_u = np.linalg.norm(u)
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
    for k in range(1000):
        Q, R = QRDec(C1)
        C1 = np.matmul(R, Q)
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
                if(countsplit == 1 and j == 0):
                    eigvecs = x[j]
                else:
                    eigvecs = np.concatenate((eigvecs, x[j]))
    eigvecs = np.vsplit(eigvecs, countsplit)
    return eigvecs

def calceigface(A, eigvecs):
    for i in range (0, len(eigvecs)):
        eigvecs[i] = np.dot(A, eigvecs[i])
    return eigvecs

def reconstruct(eigface, diff):
    weights = np.zeros((len(diff[0]), len(eigface)))
    rec_face=[]
    for i in range(len(diff[0])):
        w = np.dot(eigface, diff[:,i])
        weights[i,:] = w
        face = np.dot(w, eigface)
        face = face + np.transpose(meann)
        reshape_face = np.reshape(face, (imageExt.size,imageExt.size))
        rec_face.append(reshape_face)
    return rec_face

def projectquery(eigface, normquery):
    weights = np.zeros((len(eigface), len(eigface)))
    for i in range(len(eigface)):
        w = np.dot(eigface, normquery)
        w = np.reshape(w, (len(w), ))
        weights[i,:] = w
        face = np.dot(w, eigface)
        face = face + np.transpose(meann)
        reshape_face = np.reshape(face, (imageExt.size,imageExt.size))
    return reshape_face

def eucdist(arr1, arr2):
    temparr = np.abs(arr1 - arr2)
    sum_sq = np.dot(np.transpose(temparr), temparr)
    sum_sq = np.sqrt(sum_sq)
    return np.min(sum_sq)
    
def findface(prq, rec_face, th = 1000):
    mindist = eucdist(prq, rec_face[0])
    idxclosestface = 0
    for i in range(1, len(rec_face)):
        currdist = eucdist(prq, rec_face[i])
        if(mindist > currdist):
            mindist = currdist
            idxclosestface = i
    if(mindist > th): 
        idxclosestface = -1
    return idxclosestface


# PROGRAM UTAMA

# Training Image
imageExt.listOfPicExtract("../test/dataset//")
arr = np.array(convertOneRow(imageExt.arrPic))
meann = nilaiTengah(arr)
diff = np.array(selisih(meann, arr))

'''
for i in range(len(diff[0])):
    tempd = diff[:, i]
    tempd = (tempd-np.min(tempd))/(np.max(tempd)-np.min(tempd))
    tempd *= 255
    tempd = (np.reshape(tempd, (size, size)))
    dir = '../test/faceEigen/difface' + str(i) +'.png'
    img = Image.fromarray(np.uint8(tempd), mode='L')
    img.save(dir)
'''

cov = np.int_(covarian(diff))
eigv = eigenvector(cov)
eigface = calceigface(diff, eigv)
eigface = np.reshape(eigface, (len(eigface), (imageExt.size*imageExt.size)))

'''
for i in range(len(eigface)):
    temp = eigface[i]
    temp = (temp-np.min(temp))/(np.max(temp)-np.min(temp))
    temp *= 255
    temp = (np.reshape(temp, (imageExt.size, imageExt.size)))
    dir = '../test/faceEigen/face' + str(i) +'.png'
    img = Image.fromarray(np.uint8(temp), mode='L')
    img.save(dir)
'''

rec_face = reconstruct(eigface, diff)

for i in range(len(rec_face)):
    tempr = rec_face[i]
    tempr = (tempr-np.min(tempr))/(np.max(tempr)-np.min(tempr))
    tempr *= 255
    rec_face[i] = tempr

'''
for i in range(len(rec_face)):
    print(rec_face[i])
    tempr = (np.reshape(rec_face[i], (imageExt.size, imageExt.size)))
    dir = '../test/faceEigen/recface' + str(i) +'.png'
    img = Image.fromarray(np.uint8(tempr), mode='L')
    img.save(dir)
'''

#Query
query, querycol = imageExt.picExtract("../test/queryface.jpg")
query = np.reshape(query, ((imageExt.size*imageExt.size), 1))

normquery = np.array(selisih(meann, query))

prq = projectquery(eigface, normquery)
prq = (prq-np.min(prq))/(np.max(prq)-np.min(prq))
prq *= 255

'''
tempprq = (np.reshape(prq, (imageExt.size, imageExt.size)))
dir = '../test/faceEigen/prq' +'.png'
img = Image.fromarray(np.uint8(tempprq), mode='L')
img.save(dir)
'''

idxclosestface = findface(prq, rec_face)
arrPiccolor = np.array(imageExt.arrPiccolor)
if(idxclosestface != -1): 
    closestface = arrPiccolor[idxclosestface]
    tempc = (closestface-np.min(closestface))/(np.max(closestface)-np.min(closestface))
    tempc *= 255
    dir = '../test/res.png'
    img = Image.fromarray(np.uint8(tempc))
    img.save(dir)
else: facenotfound = True

end = time.time()
timetaken = end-start