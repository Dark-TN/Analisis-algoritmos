import sys

class Voraz:
    def __init__(self):
        return
    def cambioMonedas(self, n, D):
        D.sort()
        S = []
        s = 0
        x = 0
        i = len(D) - 1
        while s < n:
            while i >= 0:
                if D[i] + s <= n:
                    x = D[i]
                    break
                i -= 1
            if x != 0:
                S.append(x)
                s += x
        if s != n: return "No encuentro la solucion"
        return S
    def mochila(self, w, v, W):
        x = []
        vw = []
        peso = 0
        solucion = 0
        for j in range(len(v)):
            x.insert(j, 0)
            vw.append(float(v[j]) / w[j])
        while peso < W:
            i = 0
            for j in range(1, len(vw)):
                if vw[j] > vw[i]:
                    i = j
            if peso + w[i] <= W:
                x[i] = 1
                peso += w[i]
                solucion += v[i]
            else:
                x[i] = float((W - peso)) / w[i]
                solucion += x[i] * v[i]
                peso = W
            vw[i] = 0
        return x, solucion

voraz = Voraz()
problema = int(sys.argv[1])
txt = sys.argv[2]
txt = open(txt, 'r')
data = txt.readlines()
if problema == 1:
    D = list(map(int, data[0].split(',')))
    n = int(data[1])
    print(voraz.cambioMonedas(n, D))
else: 
    w = list(map(int, data[0].split(',')))
    v = list(map(int, data[1].split(',')))
    W = int(data[2])
    print(voraz.mochila(w, v, W))
