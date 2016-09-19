# -*- coding: utf-8 -*-
"""


@author: Leandro
"""

from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot
#funcao que implementa o medoto Gauss Jacobi, recebendo como parametro matrizes A e B
def gauss_jacobi(A,B,k=0,x=None) :
    #cria uma matriz do comprimento da matriz A preenchida com zeros    
    #inicializa o vetor X com 0 em cada posição
    x = zeros(len(A)) #x = [0,0,0,...]
    #enquanto o valor encontrado for maior que o erro tolerado, continua com a interação enquanto o resultado da funcao erro for true        
    while (erro(gauss_jacobi(A,B),x)) : 
        x[0] = (1 / A[0][0])*(B[0] - (A[0][1]*x[1]) - (A[0][2]-x[2]))
        x[1] = (1 / A[1][1])*(B[1] - (A[1][0]*x[0]) - (A[1][2]-x[2]))
        x[2] = (1 / A[2][2])*(B[2] - (A[2][0]*x[0]) - (A[2][1]-x[1]))
        k = k + 1
    print (k)
    #retorna o vetor X como resultado
    return x


 
"""
     max      |Xi^k+1 - Xi^k| /       max     |Xi^k+1|
 1 <= i <= n                      1 <= i <= n
"""
#funcao bool que verifica se o valor encontrado é menor que o erro tolerado, recebe o valor da interação atual e a anterior
def erro(X,Xant,tolerado = 10**-2) :
    #resultado armazena o vetor resultado interação atual - anterior
    resultado = array(X - Xant)
    print(resultado)
    print(range(len(resultado)))
    #inicia a variavel com o primeiro elemento da matriz
    maior1 = resultado[0][0]
    #inicia a variavel com o primeiro elemento do vetor
    maior2 = X[0]
    #loop para percorrer todos os elementos 
    for i in range(len(resultado)) :
        #loop para percorrer todos os elementos
        for j in range(len(resultado[i])) :
            #variavel armazena o valor da posicao atual da matriz resultado
            var = float(resultado[i][j])
            #se o valor for menor que zero
            if (var < 0) :
                #multiplica o valor por -1 para torna-lo positivo
                var = var * -1
            #se o valor for maior que o valor armazenado na variavel maior1
            if var > maior1 :
                #salva o valor da variavel na variavel maior1
                maior1 = var       
    #loop para percorrer todos os elementos    
    for i in range(len(X)) :
        #variavel armazena o valor da posição atual do vetor
        var = float(X[i])
        #se o valor for menor que zero
        if (var < 0) :
            #multiplica o valor por -1 para torna-lo positivo
            var = var * -1
        #se o valor for maior que o valor da variavel maior2
        if var > maior2 :
            #salva o valor da variavel na variavel maior2
            maior2 = var
    
    print(maior1,maior2)
    #variavel er recebe o o valor da variavel maior1 dividido pela maior2
    er = maior1 / maior2
    print (er)
    #se variavel er for menor que a variavel tolerado 
    if er < tolerado :
        #retorna Falso
        return False
    #se não retorna Verdadeiro
    return True


A = array([[10., 3.,-2.],
           [ 2., 8.,-1.],
           [ 1., 1., 5.]])

B = array([[57.],
           [20.],
           [-4.]])

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


if (erro(gauss_jacobi(A,B), A)):
    print("True")
else :
    print("False")
    

    