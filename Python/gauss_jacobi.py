# -*- coding: utf-8 -*-
"""

@author: Leandro M
"""
from numpy import array, zeros, dot
#funcao que implementa o medoto Gauss Jacobi, recebendo como parametro matrizes A e B
def gauss_jacobi(A,B,k=0,x=None) :
    A = pivoteamento(A,B)
    #Imprime a matriz escalonada
    print(A) 
    arq = open("escalonada.csv", 'w')        
    arq.writelines(str(A))
    arq.close

    #cria uma matriz do comprimento da matriz A preenchida com zeros
    #inicializa o vetor X com 0 em cada posição
    x = zeros(len(A)) #x = [0,0,0,...]
    #variavel para controlar o loop enquanto for verdadeira continua com o loop
    continua = True
    #variavel contador do numero de interações
    interacoes = 0
    #variavel para ser a saida no arquivo
    saida = [] 
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
        #print(interacoes)
        #impoe um limite de interações
        if (interacoes == 1000) :
            print("não encontrou")
            return x
        #salva o valor calculado X na variavel x
        x = X;
        #para ir salvando os resultados da interação em um arquivo csv para abrir no excel
        saida.append(str(interacoes)+';')    
        for aux in range(len(X)) :
            saida.append('{}'.format(X[aux]))
            saida.append(';')
        saida.append('\n')
        arq = open("resultado.csv", 'w')        
        arq.writelines(saida)
        arq.close
    #retorna o vetor x como resultado
    return x

#funcao bool que verifica se o valor encontrado é menor que o erro tolerado, recebe o valor da interação atual e a anterior
def erro(X,Xant,tolerado = 10**-10) :
    #resultado armazena o vetor resultado interação atual - anterior
    resultado = array(X - Xant)
    #print(resultado)
    #print(range(len(resultado)))
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

    #print(maior1,maior2)
    #variavel er recebe o o valor da variavel maior1 dividido pela maior2
    er = maior1 / maior2
    #print (er)
    #se variavel er for menor que a variavel tolerado
    #getcontext().prec = 6

    if er < tolerado :
        #retorna Falso
        return False
    #se não retorna Verdadeiro
    return True


def pivoteamento(A,B):
    n = len(A[0]) - 1
    for j in range(len(A[0]) - 1):
        i = 1
        while i <= (n-j) :
            #A[j][j] é o pivo
            if abs(A[j+i][j]) > abs(A[j][j]) :
                k = j
                while (k <=n) :
                    aux = A[j+i][k]
                    A[j+i][k] = A[j][k]
                    A[j][k] = aux
                    k += 1
                aux = B[j+i]
                B[j+i] = B[j]
                B[j] = aux
            pivo = A[j][j]
            primeiro = A[j+i][j]
            if pivo != 0 :
                B[j+i] = B[j+i] - (primeiro / pivo)*B[j]
                z = j
                while z <= n :
                    A[j+i][z] = A[j+i][z] - (primeiro / pivo) * A[j][z]
                    z += 1
            i += 1
        j += 1
    #retorna o pivoteamento 
    return A 

'''
A = array([[10., 3.,-2.],
           [ 2., 8.,-1.],
           [ 1., 1., 5.]])

B = array([[57.],
           [20.],
           [-4.]])


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

B = array([ [ 86. ],
            [ 45. ],
            [52.5 ],
            [108. ],
            [66.5 ],
            [90.5 ],
            [139. ],
            [ 61. ],
            [-43.5],
            [ 31.] ])

A = array([ [ 2., 2., 1., 1.],
            [ 1.,-1., 2.,-1.],
            [ 3., 2.,-3.,-2.],
            [ 4., 3., 2., 1.] ])

B = array([ [ 7.],
            [ 1.],
            [ 4.],
            [12.] ])

'''
print("A: ")
print(A)
"""
for i in range(len(A)):
    print(A.transpose()[i]) #transposta
    """
print("B: ")
print(B)

print(gauss_jacobi(A,B).transpose())
