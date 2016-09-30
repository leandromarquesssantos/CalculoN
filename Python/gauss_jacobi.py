# -*- coding: utf-8 -*-
"""


@author: Leandro
"""
from numpy import array, zeros, dot, allclose
#funcao que implementa o medoto Gauss Jacobi, recebendo como parametro matrizes A e B
def gauss_jacobi(A,B,k=0,x=None) :
    #cria uma matriz do comprimento da matriz A preenchida com zeros
    #inicializa o vetor X com 0 em cada posição
    x = zeros(len(A)) #x = [0,0,0,...]
    #variavel para controlar o loop enquanto for verdadeira continua com o loop
    continua = True
    #variavel contador do numero de interações
    interacoes = 0
    #enquanto o valor encontrado for maior que o erro tolerado, continua com a interação enquanto o resultado da funcao erro for true
    while (continua) :
        #interacoes recebe interacoes + 1
        interacoes += 1
        #é necessario que cada interação o vetor X seja limpo
        X = zeros(len(A)) #x = [0,0,0,...]
        #para cara coluna na matriz
        for k in range(len(A[0])) :
            #variavel para salvar o produto da multiplicação das posições anteriores ao indice k de A e de x
            c = dot(A[k, :k], x[:k]) # x[:k] significa do incio de x[] até o x[k]
            #variavel para salvar o produto da multiplicação das posições posteriores ao indice k de A e de x
            d = dot(A[k, k + 1:], x[k + 1:]) #x[k+1:] significa do x[k+1] até o fim dos elementos de x[]
            #calcula o valor do termo pela formula gauss jabobi.
            X[k] = ((B[k] - c - d) / A[k, k])
        #continua recebe false caso o valor esteja proximo o suficiente, de acordo com a tolerancia indicada (1^-10). caso contrario recebe true
        #continua = not allclose(X, x, rtol=1e-10) #utilizando a função da biblioteca que calcula o valor do erro
        continua = erro(X, x) #utilizando a funcao erro que escrevi para calcular o valor erro
        print(interacoes)
        #impoe um limite de interações
        if (interacoes == 10000) :
            print("não encontrou")
            return x
        #salva o valor calculado X na variavel x
        x = X;
    #retorna o vetor x como resultado
    return x

#funcao bool que verifica se o valor encontrado é menor que o erro tolerado, recebe o valor da interação atual e a anterior
def erro(X,Xant,tolerado = 10**-10) :
    #resultado armazena o vetor resultado interação atual - anterior
    resultado = array(X - Xant)
    print(resultado)
    print(range(len(resultado)))
    #inicia a variavel com o primeiro elemento da matriz
    maior1 = resultado[0]
    #inicia a variavel com o primeiro elemento do vetor
    maior2 = X[0]
    #loop para percorrer todos os elementos
    for i in range(len(resultado)) :
        #variavel armazena o valor da posicao atual da matriz resultado
        var = float(resultado[i])
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
print(A)
"""
for i in range(len(A)):
    print(A.transpose()[i]) #transposta
    """
print("B: ")
print(B)

print("x: ")
print(gauss_jacobi(A,B))
