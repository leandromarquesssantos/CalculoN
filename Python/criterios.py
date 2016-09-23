# -*- coding: utf-8 -*-
"""


@author: Leandro
"""
from numpy import array, zeros

def criteriodaslinhas(A) :
    sum  = 0
    resultado = zeros(len(A))
    for i in range(len(A)) :
        for j in range(len(A[i])) :
            if (j != i) :
                if A[i][j] < 0 :
                    sum = sum + (-1 * A[i][j])    
                else :
                    sum = sum + A[i][j]
        resultado[i] = sum / A[i][i]
    
    max = resultado[0]    
    for i in resultado :    
        if (resultado[i] > max) :
            max = resultado[i]
        
    if (max < 1) :    
        return True
    else :
        return False

def criteriodascolunas(A) :
    sum = 0
    resultado = zeros(len(A))
    for i in range(len(A)) :
        for j in range(len(A[i])) :
            if (j != i) :
                if A[i][j] < 0 :
                    sum = sum + (-1 * A[i][j])    
                else :
                    sum = sum + A[i][j]
        resultado[i] = sum / A[j][j]

    max = resultado[0]    
    for i in resultado :    
        if (resultado[i] > max) :
            max = resultado[i]
        
    if (max < 1) :    
        return True
    else :
        return False

def criteriodesassenfeld(A) :

    for i in A :
        for j in A[i] :
            if (j != i) :
                if A[i][j] < 0 :
                    sum = sum + (-1 * A[i][j])    
                else :
                    sum = sum + A[i][j]
        resultado[i] = sum / A[i][i]    



A = array([[10., 2., 1.],
           [ 0., 5., 1.],
           [ 2., 3., 10.]])

if (criteriodaslinhas(A)) :
    print ('passou na linha')
else :
    print ('nao passou na linha')


if (criteriodascolunas(A)) :
    print ('passou na coluna')
else :
    print ('nao passou na coluna')

