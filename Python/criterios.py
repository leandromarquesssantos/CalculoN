# -*- coding: utf-8 -*-
"""


@author: Leandro
"""
from numpy import array, zeros

def criteriodaslinhas(A) :
    sum  = 0
    alpha = zeros(len(A))
    for i in range(len(A)) :
        for j in range(len(A[i])) :
            if (j != i) :
                if A[i][j] < 0 :
                    sum = sum + (-1 * A[i][j])    
                else :
                    sum = sum + A[i][j]
        alpha[i] = sum / A[i][i]
    max = alpha[0]    
    for i in range(len(alpha)) :    
        if (alpha[i] > max) :
            max = alpha[i]
        
    if (max < 1) :    
        return True
    else :
        return False

def criteriodascolunas(A) :
    sum = 0
    beta = zeros(len(A))
    for i in range(len(A)) :
        for j in range(len(A[i])) :
            if (j != i) :
                if A[i][j] < 0 :
                    sum = sum + (-1 * A[i][j])    
                else :
                    sum = sum + A[i][j]
        beta[i] = sum / A[j][j]

    max = beta[0]    
    for i in range(len(beta)) :    
        if  (beta[i] > max) :
            max = beta[i]
        
    if (max < 1) :    
        return True
    else :
        return False

def criteriodesassenfeld(A) :
    alfa = 0
    beta = []
    for i in range(len(A)) :
        if A[i][1] < 0 :
            alfa = (alfa + (-1 * A[i][1]))
        else :
            alfa = (alfa + A[i][1])
    beta.append(alfa / A[0][0])
    
    return beta[0]
    alfa = 0
    for i in range(len(A)) :
        if i != 0 :
            
                if A[i-1][i] < 0 :
                    alfa = alfa + (A[i-1][i] * -1)

A = array([[5.,2.,0.],
           [1.,0.,5.],
           [7.,-1.,8.]])

#A = array([[10., 2., 1.],
#           [ 0., 5., 1.],
#           [ 2., 3., 10.]])

if (criteriodaslinhas(A)) :
    print ('passou na linha')
else :
    print ('nao passou na linha')


if (criteriodascolunas(A)) :
    print ('passou na coluna')
else :
    print ('nao passou na coluna')

print (criteriodesassenfeld(A))