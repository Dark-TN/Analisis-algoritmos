from random import randint, randrange
import numpy as np
import time

class LasVegas():
    def __init__(self):
        self.array = []
        self.arrayOriginal = []
    def llenarArreglo(self, n):
        del self.array[:]
        del self.arrayOriginal[:]
        for i in range(n):
            self.arrayOriginal.append(randint(0, 1000))
        self.array = self.arrayOriginal.copy() 
    def randomQuickSort(self, inicio, fin):
        if inicio < fin:
            pivote = randint(inicio, fin)
            temp = self.array[fin]
            self.array[fin] = self.array[pivote]
            self.array[pivote] = temp
            p = self.randomParticion(inicio, fin)
            self.randomQuickSort(inicio, p-1)
            self.randomQuickSort(p+1, fin)
    def randomParticion(self, inicio, fin):
        pivote = randint(inicio, fin)
        temp = self.array[fin]
        self.array[fin] = self.array[pivote]
        self.array[pivote] = temp
        nuevoPivoteIndex = inicio - 1
        for index in range(inicio, fin):
            if self.array[index] < self.array[fin]:
                nuevoPivoteIndex = nuevoPivoteIndex + 1 
                temp = self.array[nuevoPivoteIndex]
                self.array[nuevoPivoteIndex] = self.array[index]
                self.array[index] = temp
        temp = self.array[nuevoPivoteIndex + 1]
        self.array[nuevoPivoteIndex + 1] = self.array[fin]
        self.array[fin] = temp
        return nuevoPivoteIndex + 1
    def quickSort(self, inicio, fin): 
        if inicio < fin: 
            p = self.particion(inicio, fin) 
            self.quickSort(inicio, p - 1) 
            self.quickSort(p + 1, fin) 
    def particion(self, inicio, fin): 
        i =  inicio-1
        pivote = self.array[fin]
        for j in range(inicio , fin): 
            if self.array[j] <= pivote:
                i = i+1 
                self.array[i], self.array[j] = self.array[j], self.array[i] 
        self.array[i+1], self.array[fin] = self.array[fin], self.array[i+1] 
        return i+1
    def reinas(self,n, N):
        tablero = np.zeros((8, 8), dtype=int)
        reinas = tablero.copy()
        soluciones = 0
        solucion = True
        peligro = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x < 8 and
                                   -1 < y < 8 and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 < 8) and
                                   (0 <= y2 < 8))]
        if n == 3:
            reinas[1][6] = reinas[2][2] = reinas[3][7] = reinas[5][4] = reinas[6][0] = 1
        elif n == 4:
            reinas[2][2] = reinas[3][7] = reinas[5][4] = reinas[6][0] = 1
        elif n == 5:
            reinas[2][2] = reinas[5][4] = reinas[6][0] = 1
        else:
            for i in range(N):
                solucion = True
                tablero = np.zeros((8, 8), dtype=int)
                for j in range(8):
                    x = randrange(0, 7)
                    y = randrange(0, 7)
                    if tablero[x][y] > 0:
                        solucion = False
                        break
                    else:
                        tablero[x][y] = 1
                        for k in peligro(x, y):
                            tablero[k[0]][k[1]] = 2
                if solucion:
                    soluciones += 1
            return soluciones
        tablero = reinas
        for x in range(8):
            for y in range(8):
                if tablero[x][y] == 1:
                    for i in peligro(x, y):
                        tablero[i[0]][i[1]] = 2
        for i in range(N):
            solucion = True
            for j in range(8-n):
                x = randrange(0, 7)
                y = randrange(0, 7)
                if tablero[x][y] > 0:
                    solucion = False
                    break
            if solucion:
                soluciones += 1
        return soluciones
                
txt = open("quicksort.txt", "w")
txt.write("muestras\tquicksort\trandom quicksort\n")
lv = LasVegas()
for i in range(1000, 11000, 1000):
    txt.write("%d\t" %i)
    lv.llenarArreglo(i)
    ti = time.time()
    lv.quickSort(0, i-1)
    tf = time.time() - ti
    txt.write("%.6f\t" %tf)
    ti = time.time()
    lv.randomQuickSort(0, i-1)
    tf = time.time() - ti
    txt.write("%.6f\n" %tf)
txt.close()
txt = open("reinas.txt", "w")
txt.write("solucionesA\t3\t4\t5\t8\n")
i = 10000
while i <= 1000000:
    txt.write("%d\t" %i)
    n = 3
    while n <= 8:
        s = lv.reinas(n, i)
        if n < 8:
            txt.write("%d\t" %s)
        else:
            txt.write("%d\n" %s)
        if n == 5:
            n += 3
        else:
            n += 1
    if i == 10000: i += 40000
    elif i == 100000: i *= 10
    else: i += 50000
            

