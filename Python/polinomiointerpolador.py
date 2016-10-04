from numpy import array, zeros, ones

def lagranje(X,Y,x) :
    #Inicia a matriz G[i][j] com zeros no tamanho de i = x j = x
    G = zeros( (len(X),len(X)), float )
    #laço de repetição para percorrer todos os elementos
    for n in range(len(X)) :
        for j in range(len(X)) :
            #se n == j diagonal principal.
            if n == j :
                G[n][j] = x - X[j]
            else :
                G[n][j] = X[n] - X[j]
    #inicia vetor R de tamanho de x com numero 1
    R = ones(len(X),float)
    Gd = 1.0
    for i in range(len(X)) :
        for j in range(len(X)) :
            if i == j :
                Gd *= G[i][j]
            R[i] *= G[i][j]

    resultado = 0.0
    for i in range(len(X)) :
        resultado += (Y[i]/R[i])

    resultado *= Gd
    return resultado

'''
Função que transpoe um vetor
'''
def tran(X) :
    vetor = zeros( (len(X),1), float)
    for i in range(len(X)) :
        vetor[i][0] = X[i]
    return vetor


def newton(X,Y,x) :
    tam = len(X)
    X = tran(X)
    Y = tran(Y)

    delta[0][0] = ((Y[1] - Y[0]) / (X[1] - X[0]))
    delta[1][0] = ((Y[2] - Y[1]) / (X[2] - X[1]))
    o = 1
    while tam - o > 1 :
        for i in (range(tam) - o) :
            delta[i][0] = (Y[i+o] - Y[i+1-o]) / (X[i+o] - X[i+1-o])


    return 0


#X = [0.1, 0.6, 0.8]
#Y = [1.221, 3.32, 4.9533]
#x = 0.2

#X = [183., 173., 168., 188., 158., 163., 178.]
#Y = [ 79.,  69.,  70.,  81.,  61.,  63.,  73.]

#X = [158., 163., 168., 173., 178., 183., 188.]
#Y = [ 61.,  63.,  70.,  69.,  73.,  79.,  81.]
#x = 175.

X = [0.9, 1.1, 2.0]
Y = [3.211, 2.809, 1.614]
x = 1.2

#print(X)
#print (tran(X))

#print(len(X))
print(lagranje(X,Y,x))
