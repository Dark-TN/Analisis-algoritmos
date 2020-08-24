import time
import random
import matplotlib.pyplot as plt

def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

muestras = [i for i in range(1000, 11000, 1000)]
tiempo_mejor_insertion = []
tiempo_prom_insertion = []
tiempo_peor_insertion = []
tiempo_mejor_bubble = []
tiempo_prom_bubble = []
tiempo_peor_bubble = []

for i in muestras:
    arr_mejor = [i for i in range(0, i+1)]
    arr_prom = [random.randint(0, i) for j in range(i)]
    arr_peor = [i for i in range(i, -1, -1)]
    arr = arr_mejor.copy()
    t_i = time.time()
    insertionSort(arr)
    t_f = time.time()
    t = t_f - t_i
    tiempo_mejor_insertion.append(t)
    arr = arr_mejor.copy()
    t_i = time.time()
    bubbleSort(arr)
    t_f = time.time()
    t = t_f - t_i
    tiempo_mejor_bubble.append(t)
    arr = arr_prom.copy()
    t_i = time.time()
    insertionSort(arr)
    t_f = time.time()
    t = t_f - t_i
    tiempo_prom_insertion.append(t)
    arr = arr_prom.copy()
    t_i = time.time()
    bubbleSort(arr)
    t_f = time.time()
    t = t_f - t_i
    tiempo_prom_bubble.append(t)
    arr = arr_peor.copy()
    t_i = time.time()
    insertionSort(arr)
    t_f = time.time()
    t = t_f - t_i
    tiempo_peor_insertion.append(t)
    arr = arr_peor.copy()
    t_i = time.time()
    bubbleSort(arr)
    t_f = time.time()
    t = t_f - t_i
    tiempo_peor_bubble.append(t)

fig, ax = plt.subplots()
ax.plot(muestras, tiempo_mejor_insertion)
ax.plot(muestras, tiempo_mejor_bubble)
plt.title('Comparacion mejor tiempo')
plt.xlabel('Muestras')
plt.ylabel('Tiempo')
plt.legend(['Insertion Sort', 'Bubble Sort'])
plt.savefig("C:/Users/jedua/Documents/ESCOM/Analisis de algoritmos/mejorCaso.png")
fig, ax = plt.subplots()
ax.plot(muestras, tiempo_prom_insertion)
ax.plot(muestras, tiempo_prom_bubble)
plt.title('Comparacion tiempo promedio')
plt.xlabel('Muestras')
plt.ylabel('Tiempo')
plt.legend(['Insertion Sort', 'Bubble Sort'])
plt.savefig("C:/Users/jedua/Documents/ESCOM/Analisis de algoritmos/casoProm.png")
fig, ax = plt.subplots()
ax.plot(muestras, tiempo_peor_insertion)
ax.plot(muestras, tiempo_peor_bubble)
plt.title('Comparacion peor tiempo')
plt.xlabel('Muestras')
plt.ylabel('Tiempo')
plt.legend(['Insertion Sort', 'Bubble Sort'])
plt.savefig("C:/Users/jedua/Documents/ESCOM/Analisis de algoritmos/peorCaso.png")

archivo = open('C:/Users/jedua/Documents/ESCOM/Analisis de algoritmos/tablaMejor.txt', 'w')
for i in range(len(muestras) + 1):
    if i == 0:
        archivo.write("muestras\tinsertion sort\tbubble sort\t\n")
    else:
        archivo.write("%d\t%.4f\t%.4f\t\n" %(muestras[i-1], tiempo_mejor_insertion[i-1], tiempo_mejor_bubble[i-1]))
archivo.close()

archivo = open('C:/Users/jedua/Documents/ESCOM/Analisis de algoritmos/tablaProm.txt', 'w')
for i in range(len(muestras) + 1):
    if i == 0:
        archivo.write("muestras\tinsertion sort\nbubble sort\t\n")
    else:
        archivo.write("%d\t%.4f\t%.4f\t\n" %(muestras[i-1], tiempo_prom_insertion[i-1], tiempo_prom_bubble[i-1]))
archivo.close()

archivo = open('C:/Users/jedua/Documents/ESCOM/Analisis de algoritmos/tablaPeor.txt', 'w')
for i in range(len(muestras) + 1):
    if i == 0:
        archivo.write("muestras\tinsertion sort\nbubble sort\t\n")
    else:
        archivo.write("%d\t%.4f\t%.4f\t\n" %(muestras[i-1], tiempo_peor_insertion[i-1], tiempo_peor_bubble[i-1]))
archivo.close()