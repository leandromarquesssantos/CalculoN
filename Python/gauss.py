# -*- coding: utf-8 -*-
"""


@author: Leandro
"""

from numpy import array 

#Funcao que resolve quando a matriz e triangular
def resolveTri(A):
    n = len(A) - 1
    res = []

    for i in range(len(A)):
        j = len(A) - 1
        x = []
        r = 0.0
        while (A[n][j] != 0):
            x.append(A[n][j])
            j = j - 1
            if j < 0:
                break
        if len(x) == 1:
            res.append(A[n][-1] / x[0])
        else:
            i = 0
            for i in range(len(res)):
                r = x[i] * res[i] + r
            res.append((A[-n][-1] - r) / x[-1])
        n = n - 1
    return res

#Funcao que acha o maior numero entre os valores da coluna passada
def achaMaior(A, i, j):
    maior = 0
    maiorIndice = i
    while i < len(A):
        if abs(A[i][j]) > maior:
            maior = A[i][j]
            maiorIndice = i
        i += 1
    return maiorIndice

def gauss(A):
    for j in range(len(A[0]) - 1):
        i = j
        maior = achaMaior(A, i, j)
        aux = A[i]
        A[i] = A[maior]
        A[maior] = aux
        j1 = j
        div = A[i][j]
        while j1 < len(A[i]):
            A[i][j1] = A[i][j1] / div
            j1 += 1
        i += 1
        while i < len(A):
            mul = A[i][j]
            for j1 in range(len(A[0])):
                A[i][j1] -= A[j][j1] * mul
            i += 1
    print ('\nMatriz apos pivotacao\n')
    print (A)
    r = resolveTri(A)
    return r

A = array([[10., 3.,-2.],
           [ 2., 8.,-1.],
           [ 1., 1., 5.]])

print(gauss(A))
