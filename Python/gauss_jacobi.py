# -*- coding: utf-8 -*-
"""


@author: Leandro
"""

from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

def gauss_jacobi(A,B,k=0,x=None):
    
    #cria uma matriz do comprimento da matriz A preenchida com zeros    
    if x is None :
        x = zeros(len(A))
        
    if k == 0 :
        x[0] = (1 / A[0][0])*(B[0] - (A[0][1]*x[1]) - (A[0][2]-x[2]))
        x[1] = (1 / A[1][1])*(B[1] - (A[1][0]*x[0]) - (A[1][2]-x[2]))
        x[2] = (1 / A[2][2])*(B[2] - (A[2][0]*x[0]) - (A[2][1]-x[1]))
        k ++
    print (k)
    return x


 
"""
     max      |Xi^k+1 - Xi^k| /       max     |Xi^k+1|
 1 <= i <= n                      1 <= i <= n
"""

def erro(X,Xant,tolerado = 10**-2) :
    resultado = (X - Xant)
    #print(type(resultado))
    er = max(resultado) / max(X)
    print (er)
    #if er < tolerado :
    #    return True
    return False


A = array('f',[[10,3,-2],[2,8,-1],[1,1,5]])

B = array('f',[[57],[20],[-4]])

print("Linhas: ",len(A))

print("Colunas: ",len(A[0]))


print("A: ")
pprint(A)
"""
for i in range(len(A)):
    print(A.transpose()[i]) #transposta
    """
print("B: ")
print(B)

print("X: ")
print(gauss_jacobi(A,B))

for i in range(len(gauss_jacobi(A,B))) :
    print(gauss_jacobi(A,B).transpose()[i])

print(max(gauss_jacobi(A,B)))

erro(gauss_jacobi(A,B), A)

    