# -*- coding: utf-8 -*-
import sys
import time

class Voraz:
    def __init__(self, p, i, j):
        self.min = self.MatrixChainOrder(p, i, j)
    def MatrixChainOrder(self, p, i, j): 
        if i == j: 
            return 0
        min = sys.maxsize 
        for k in range(i, j): 
            count = (self.MatrixChainOrder(p, i, k)  + self.MatrixChainOrder(p, k + 1, j) + p[i-1] * p[k] * p[j])
            if count < min: min = count
        return min

class Dinamica:
    def __init__(self, p, n):
        self.min = self.MatrixChainOrder(p, n)
    def MatrixChainOrder(self, p, n): 
        m = [[0 for x in range(n)] for x in range(n)] 
        for i in range(1, n):
            m[i][i] = 0
        for L in range(2, n):
            for i in range(1, n-L + 1): 
                j = i + L-1
                m[i][j] = sys.maxsize
                for k in range(i, j):
                    q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j]
                    if q < m[i][j]:
                        m[i][j] = q
        return m[1][n-1]

class Menu:
    def __init__(self):
        print("Selecciona una opción:\n\t1.- Algoritmo voraz\n\t2.- Programación dinámica")
        self.opt = int(input(">"))
        print("\nIngrese el tamaño de las matrices entre separados por una coma. Ejemplo: 30x5,5x20,20x10.")
        self.mat = input(">")
        self.mat = self.mat.split(",")
        self.arr = []
        for i in range(len(self.mat)): 
            self.mat[i] = self.mat[i].split("x")
            if i == 0:
                self.arr.append(int(self.mat[i][0]))
                self.arr.append(int(self.mat[i][-1]))
            else: self.arr.append(int(self.mat[i][-1]))
        del self.mat
        print(self.arr)
        if self.opt == 1:
            print(Voraz(self.arr, 1, len(self.arr) - 1).min)
        else: 
            print(Dinamica(self.arr, len(self.arr)).min)

menu = Menu()
