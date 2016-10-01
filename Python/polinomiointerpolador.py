from numpy import array, zeros, ones

def lagranje(X,Y,x) :
    #G = array([[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]])
    G = zeros( (len(X),len(X)), float )
    for n in range(len(X)) :
        for j in range(len(X)) :
            if n == j :
                G[n][j] = x - X[j]
            else :
                G[n][j] = X[n] - X[j]
    print(G)
    R = ones(len(X),float)

#    for r in range(len(X)) :
#        R.append(1.)


    Gd = 1.0
    for i in range(len(X)) :
        for j in range(len(X)) :
            if i == j :
                Gd = Gd * G[i][j]
            R[i] = R[i] * G[i][j]

    print(Gd)
    print(R)
    resultado = 0.0
    for i in range(len(X)) :
        print (resultado)
        resultado = resultado + (Y[i]/R[i])

    return Gd*resultado

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
        for i in range(tam) - o) :
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


print (tran(X))

#print(len(X))
#print(lagranje(X,Y,x))
