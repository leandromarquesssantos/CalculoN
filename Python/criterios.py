# -*- coding: utf-8 -*-
"""


@author: Leandro
"""
from numpy import array, zeros, amax

def maximo(vetor,criterio) :
    max = vetor[0]
    for i in range(len(vetor)) :
        if  vetor[i] > max :
            max = vetor[i]

    print (max)
    if max < criterio :
        return True
    else :
        return False

def criteriodaslinhas(A) :
    sum  = 0
    alfa = zeros(len(A))
    for i in range(len(A)) :
        for j in range(len(A[i])) :
            if j != i :
                if A[i][j] < 0 :
                    sum = sum + (-1 * A[i][j])
                else :
                    sum = sum + A[i][j]
        alfa[i] = sum / A[i][i]

        return maximo(alfa,0)

def criteriodascolunas(A) :
    sum = 0
    beta = zeros(len(A))
    for i in range(len(A)) :
        for j in range(len(A[i])) :
            if j != i :
                if A[i][j] < 0 :
                    sum = sum + (-1 * A[i][j])
                else :
                    sum = sum + A[i][j]
        beta[i] = sum / A[j][j]

    return maximo(beta,0)

def criteriodesassenfeld(A) :
    alfa = 0
    beta = []

    for i in range(len(A)) :
        if i != 0 :
            if A[0][i] < 0 :
                alfa = (alfa + (-1 * A[0][i]))
            else :
                alfa = (alfa + A[0][i])
        if alfa / A[0][0] < 0 :
            resultado = (alfa * (1 / A[0][0]) * -1)
        else :
            resultado = alfa * (1 / A[0][0])


    beta.append(resultado)

#    return beta[0]

    for i in range(len(A)) :
        alfa = 0
        if i == 0 :
            resultado = A[i][i] * beta[i] / A[0][0]
            if resultado < 0 :
                resultado = resultado * -1
            beta.append(resultado)

        else :
            for s in range(len(beta)) :
                for l in range(len(A[i]))
                    alfa = 0
                    if l == 0 :
                        alfa = A[i][l] * beta[i]
                    else :
                        
#            resultado = beta[i] * A[i][i] / A[i][i]
#            if resultado < 0 :
#                resultado = resultado * -1
#            alfa = 0
#            for n in range(len(A)) :
#                if alfa < 0 :
#                    alfa = alfa + (A[n][i] * -1)
#                else :
#                    alfa = alfa + A[n][i]


            if A[i][i] < 0 :
                alfa = alfa / (A[i][i] * -1)
            else :
                alfa = alfa / A[i][i]
            if alfa < 0 :
                resultado = resultado + (alfa * -1)
            else :
                resultado = resultado + alfa
            beta.append(resultado)
    print(beta)
    return maximo(beta,1)

A = array([[3., 0., 1.],
           [1.,-1., 0.],
           [3., 1., 2.]])

#A = array([[5.,2.,0.],
#           [1.,0.,5.],
#           [7.,-1.,8.]])

#A = array([[10., 2., 1.],
#           [ 0., 5., 1.],
#           [ 2., 3., 10.]])

'''if (criteriodaslinhas(A)) :
    print ('passou na linha')
else :
    print ('nao passou na linha')

if (criteriodascolunas(A)) :
    print ('passou na coluna')
else :
    print ('nao passou na coluna')


if (criteriodesassenfeld(A)) :
    print ('passou no criterio de sassenfeld')
else :
    print ('nao passou no criterio de sassenfeld')
'''

print (criteriodesassenfeld(A))
print (maximo(A[2],1))
