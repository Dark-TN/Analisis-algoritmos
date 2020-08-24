import numpy as np
import sys

class ProgramacionDinamica:
    def __int__(self):
        return
    def cambioMonedas(self, N, d):
        d.sort()
        tabla = np.zeros(shape = (len(d), N + 1), dtype = int)
        for i in range(len(d)):
            for j in range(N + 1):
                if i == 0 and j >= d[i]: tabla[i, j] = 1 + tabla[0, j - d[0]]
                elif i > 0 and j < d[i]: tabla[i, j] = tabla[i - 1, j]
                else: tabla[i, j] = min(tabla[i - 1, j], 1 + tabla[i, j - d[i]])
        return tabla
    def mochila(self, w, v, W):
        tabla = np.zeros(shape = (len(w), W + 1), dtype = int)
        for i in range(len(w)):
            for j in range(W + 1):
                if j < w[i]: tabla[i, j] = tabla[i - 1, j]
                else: tabla[i, j] = max(tabla[i - 1, j], tabla[i - 1, j - w[i]] + v[i])
        return tabla

dinamica = ProgramacionDinamica()
problema = int(sys.argv[1])
txt = sys.argv[2]
txt = open(txt, 'r')
data = txt.readlines()
if problema == 1:
    d = list(map(int, data[0].split(',')))
    N = int(data[1])
    print(dinamica.cambioMonedas(N, d))
else: 
    w = list(map(int, data[0].split(',')))
    v = list(map(int, data[1].split(',')))
    W = int(data[2])
    print(dinamica.mochila(w, v, W))
    