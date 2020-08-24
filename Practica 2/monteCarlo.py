#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd
import math

np.random.seed(1984)

def f1(x):
    return (1 - x**2)**(3/2)
def f2(x):
    return math.e**(x + x**2)
def f3(x):
    return (1 + x**2)**2
def f4(x):
    return (1 / (np.cos(x) + 2))
def f5(x):
    return np.log(x)

class MonteCarlo:
    def __init__(self):
        return
    def calcularPi(self, N):
        x, y = np.random.uniform(-1, 1, size=(2, N))
        interior = (x**2 + y**2) <= 1.0
        pi = interior.sum() * 4 / N
        error = abs((pi - np.pi) / pi) * 100
        exterior = np.invert(interior)
        return (pi, x, y, interior, exterior, error)
    def aproxIntegral(self, x1, x2, n, func):
        X = np.linspace(x1, x2, n)
        y1 = 0
        y2 = max((func(X))) + 1
        area = (x2 - x1) * (y2 - y1)
        check = []
        xs = []
        ys = []
        for i in range(n):
            x = np.random.uniform(x1, x2, 1)
            xs.append(x)
            y = np.random.uniform(y1, y2, 1)
            ys.append(y)
            if abs(y) > abs(func(x)) or y < 0:
                check.append(0)
            else:
                check.append(1)
        return(np.mean(check) * area, xs, ys, check)

class GUI:
    def __init__(self):
        self.monteCarlo = MonteCarlo()
    def formIntegral(self):
        self.root = tk.Tk()
        self.root.title("Aproximación de integrales por el método de Monte Carlo")
        self.label1 = tk.Label(self.root, text= "Rango a: ")
        self.label1.grid(row = 0, column = 0, sticky = "w", padx = (10, 5), pady = (10, 10))
        self.entry1 = tk.Entry(self.root)
        self.entry1.grid(row = 0, column = 1, sticky = "w", padx = (10, 5), pady = (10, 10))
        self.label2 = tk.Label(self.root, text= "Rango b: ")
        self.label2.grid(row = 0, column = 2, sticky = "w", padx = (10, 5), pady = (10, 10))
        self.entry2 = tk.Entry(self.root)
        self.entry2.grid(row = 0, column = 3, padx = (10, 10), pady = (10, 10))
        self.label3 = tk.Label(self.root, text= "Número de aleatorios: ")
        self.label3.grid(row = 1, column = 0, sticky = "w", padx = (10, 5), pady = (10, 10))
        self.entry3 = tk.Entry(self.root)
        self.entry3.grid(row = 1, column = 1, padx = (10, 5), pady = (10, 10))
        self.label5 = tk.Label(self.root, text = "Seleccione una función: ")
        self.label5.grid(row = 1, column = 2, sticky = "w", padx = (10, 5), pady = (10, 10))
        self.combo1 = ttk.Combobox(self.root)
        self.combo1.grid(row = 1, column = 3, padx = (10, 10), pady = (10, 10))
        self.combo1["values"] = ["Funcion 1", "Funcion 2", "Funcion 3", "Funcion 4", "Funcion 5"]
        self.label4 = tk.Label(self.root, text= "Calcula integral aproximada: ")
        self.label4.grid(row = 2, column = 0, sticky = "w", padx = (10, 5), pady = (10, 10))
        self.label6 = tk.Label(self.root, text = " ")
        self.label6.grid(row = 2, column = 1, sticky = "w", padx = (10, 5), pady = (10, 10))
        self.button1 = tk.Button(self.root, text = "Simular", command = lambda: self.simularIntegral())
        self.button1.grid(row = 3, column = 1, padx = (10, 5), pady = (10, 10))
        self.root.mainloop()
    def simularIntegral(self):
        a = int(self.entry1.get())
        b = int(self.entry2.get())
        n = int(self.entry3.get())
        func = self.combo1.current()
        X=np.linspace(a, b, n)
        if func == 0:
            aprox,x,y,c = self.monteCarlo.aproxIntegral(a, b, n, f1)
            plt.plot(X, f1(X))
        elif func == 1:
            aprox,x,y,c = self.monteCarlo.aproxIntegral(a, b, n, f2)
            plt.plot(X, f2(X))
        elif func == 2:
            aprox,x,y,c = self.monteCarlo.aproxIntegral(a, b, n, f3)
            plt.plot(X, f3(X))
        elif func == 3:
            aprox,x,y,c = self.monteCarlo.aproxIntegral(a, b, n, f4)
            plt.plot(X, f4(X))
        else:
            aprox,x,y,c = self.monteCarlo.aproxIntegral(a, b, n, f5)
            plt.plot(X, f5(X))
        self.label6.config(text = str(aprox))
        df=pd.DataFrame()
        df['x'] = x
        df['y'] = y
        df['c'] = c
        plt.scatter(df[df['c']==0]['x'], df[df['c']==0]['y'],color='red')
        plt.scatter(df[df['c']==1]['x'], df[df['c']==1]['y'],color='blue')
        plt.show()
    def simularPi(self):
        i = 100
        txt = open("pi.txt", "w")
        while i <= 1000000:
            pi, x, y, interior, exterior, error = self.monteCarlo.calcularPi(i)
            txt.write("%d\t%.4f\n" %(i, pi))
            i *= 10
        txt.close()
        plt.figure(figsize=(6,6))
        plt.plot(x[interior], y[interior], 'b.')
        plt.plot(x[exterior], y[exterior], 'r.')
        plt.plot(0, 0, label='$\hat \pi$ = {:4.4f}\nerror = {:4.4f}%'.format(pi,error), alpha=0)
        plt.axis('square')
        plt.legend(frameon=True, framealpha=0.9, fontsize=14)
        plt.show()
        
gui = GUI()
gui.simularPi()
gui.formIntegral()
