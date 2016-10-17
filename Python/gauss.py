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
    #r = resolveTri(A)
    return A

A = array([ [ 2., 1., 7., 4.,-3.,-1., 4., 4., 7., 0.],
            [ 4., 2., 2., 3.,-2., 0., 3., 3., 4., 1.],
            [ 3., 4., 4., 2., 1.,-2., 2., 1., 9.,-3.],
            [ 9., 3., 5., 1., 0., 5., 6.,-5.,-3., 4.],
            [ 2., 0., 7., 0.,-5., 7., 1., 0., 1., 6.],
            [ 1., 9., 8., 0., 3., 9., 9., 0., 0., 5.],
            [ 4., 1., 9., 0., 4., 3., 7.,-4., 1., 3.],
            [ 6., 3., 1., 1., 6., 8., 3., 3., 0., 2.],
            [ 6., 5., 0.,-7., 7.,-7., 6., 2.,-6., 1.],
            [ 1., 6., 3., 4., 8., 3.,-5., 0.,-6., 0.] ])

gauss(A)
#print(gauss(A))
