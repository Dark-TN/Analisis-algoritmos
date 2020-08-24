import sys

def lcs(X, Y, m, n):
    tabla = open(sys.argv[2], "w")
    L = [[0 for x in range(n+1)] for x in range(m+1)] 
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
    index = L[m][n] 
    lcs = [""] * (index+1) 
    lcs[index] = ""
    i = m 
    j = n 
    while i > 0 and j > 0: 
        if X[i-1] == Y[j-1]: 
            lcs[index-1] = X[i-1] 
            i-=1
            j-=1
            index-=1
        elif L[i-1][j] > L[i][j-1]: 
            i-=1
        else: 
            j-=1
    tabla.write("  0  ")
    for i in Y: tabla.write("%s  " %i)
    tabla.write("\n")
    for i in range(len(L)):
        if i == 0: tabla.write("0"+str(L[i])+"\n")
        else: tabla.write(X[i-1]+str(L[i])+"\n")
    tabla.write("Porcentaje: "+str(len("".join(lcs))*100/len(X)))
    tabla.close()
    print("\nLa subsecuencia mas larga de " + X + " y " + Y + " es " + "".join(lcs))  

archivo = open(sys.argv[1], "r")
X = archivo.readline()
archivo.readline()
Y = archivo.readline()
archivo.close()
m = len(X)
n = len(Y)
lcs(X, Y, m, n)