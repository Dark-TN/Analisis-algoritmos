import time

arreglo1 = []
arreglo2 = []
n = 0

def initArreglo(n):
    for i in range(n):
        arreglo2.insert(i, -1)

def fibonacci1(n):
    if n < 2:
        return n
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)

def fibonacci2(n):
    if n < 2:
        return n
    else:
        arreglo1.insert(0, 0)
        arreglo1.insert(1, 1)
        for i in range(2, n+1):
            arreglo1.insert(i, arreglo1[i-1] + arreglo1[i-2])
        return arreglo1[n-1]

def fibonacci3(n):
    if n < 2:
        return n
    if arreglo2[n-1] == -1:
        arreglo2[n-1] = fibonacci3(n-1)
    if arreglo2[n-2] == -1:
        arreglo2[n-2] = fibonacci3(n-2)
    arreglo2[n] = arreglo2[n-1] + arreglo2[n-2]
    return arreglo2[n]


file = open("p1p1a3.txt","w")

file.write("muestras\ttiempo\n")

for i in range(5, 105, 5):
    print("#### %d muestras ####\n" %i)
    '''ti = time.time()
    fibonacci1(i)
    tf = time.time()
    print("Algoritmo 1: %.6f" %(tf-ti))
    file.write("%d\t%.4f\n" %(i,tf-ti))'''


    '''ti = time.time()
    fibonacci2(i)
    tf = time.time()
    print("Algoritmo 2: %f" %(tf-ti))
    file.write("%d\t%f\n" %(i,tf-ti))'''

    n = i
    arreglo2 = []
    initArreglo(n + 1)
    ti = time.time()
    fibonacci3(n)
    tf = time.time()
    print("Algoritmo 3: %.6f" %(tf-ti))
    file.write("%d\t%.4f\n" %(i,tf-ti))

