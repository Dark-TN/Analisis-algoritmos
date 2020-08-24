
####################################################################################################################################
# Autor: Ruvalcaba Montoya Jesús Eduardo                                                                                           #
# Grupo: 3CM4                                                                                                                      #
# Descripción: Implementación del algoritmo recursivo de Bron-Kerbosh sin pivote para encontrar el máximo clique de un grafo dado. #
####################################################################################################################################

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import os

class Grafo: # Clase grafo
    def __init__(self, aristas):
        self.aristas = aristas # Aristas
        self.nodos = [] # Nodos
        for i in self.aristas: # Se extraen los nodos de las aristas
            for j in i:
                if j not in self.nodos:
                    self.nodos.append(j)
        self.nodos.sort() # Se ordenan los nodos
        self.n = len(self.nodos) # Numero de nodos
        self.matriz = [] # Representación matricial del grafo
        for i in self.nodos: # Se forma la matriz de adyacencia
            arista = [0] * self.n
            for k in [j[1] for j in self.aristas if j[0] == i]:
                arista[self.nodos.index(k)] = 1
            self.matriz.append(arista)
        self.N = { 
        i: set(num for num, j in enumerate(fila) if j)
        for i, fila in enumerate(self.matriz)} # Diccionario con la información de los nodos conectados (N(v))
    def BronKerbosch(self, P = None, R = None, X = None): # Implementación del algoritmo de Bron-Kerbosch sin pivote
        P = set(self.N.keys()) if P is None else set(P)
        R = set() if R is None else R
        X = set() if X is None else X
        if not P and not X: # Si P y X estpan vacíos
            yield R # R es el máximo clique
        while P: # Mientras P siga teniendo vértices
            v = P.pop() # Se extrae v del conjunto P
            yield from self.BronKerbosch(
                P = P.intersection(self.N[v]), R = R.union([v]), X = X.intersection(self.N[v])) # Se hace la llamada recursiva
            X.add(v) # Se agrega v al conjunto X

class GUI: # clase para la interfaz gráfica
    def __init__(self):
        self.grafo = None
        self.datosArchivo = []
        self.descripcionNodos = []
        self.root = tk.Tk()
        self.root.title('Proyecto final')
        self.numerico = (self.root.register(self.funcionNumerico), "%P")
        self.frameEncabezado = tk.Frame(self.root)
        self.frameEncabezado.grid(row = 0, column = 0, sticky = 'nsew')
        path = os.path.dirname(os.path.realpath(__file__))
        imgIPN = Image.open(path + '\\Imagenes\\logo-ipn.png')
        imgIPN = imgIPN.resize((40, 54), Image.ANTIALIAS)
        imgIPN = ImageTk.PhotoImage(imgIPN)
        self.label = tk.Label(self.frameEncabezado, image = imgIPN)
        self.label.grid(row = 0, column = 0, padx = (15, 10), pady = (15, 15), sticky = 'n')
        self.label = tk.Label(self.frameEncabezado, text = 'Instituo Politécnico Nacional\nEscuela Superior de Cómputo\nAnálisis de Algoritmos\nMáximo clique\nRuvalcaba Montoya Jesús Eduardo 3CM4', justify = 'center')
        self.label.grid(row = 0, column = 1, padx = (10, 10), pady = (15, 15), sticky = 'n')
        imgESCOM = Image.open(path + '\\Imagenes\\logoescomconletras.png')
        imgESCOM = imgESCOM.resize((59, 45), Image.ANTIALIAS)
        imgESCOM = ImageTk.PhotoImage(imgESCOM)
        self.label = tk.Label(self.frameEncabezado, image = imgESCOM)
        self.label.grid(row = 0, column = 2, padx = (10, 15), pady = (15, 15), sticky = 'n')
        self.frameForm = tk.Frame(self.root)
        self.frameForm.grid(row = 1, column = 0, sticky = 'nsew')
        self.label = tk.Label(self.frameForm, text = 'Número de nodos:', justify = 'left')
        self.label.grid(row = 0, column = 0, padx = (15, 10), pady = (15, 15), sticky = 'nw')
        self.entryNumeroNodos = tk.Entry(self.frameForm, validate="key", validatecommand = self.numerico)
        self.entryNumeroNodos.grid(row = 0, column = 1, padx = (10, 15), pady = (15, 15), sticky = 'nw')
        self.label = tk.Label(self.frameForm, text = 'Agregar descripción\n de los nodos:', justify = 'left')
        self.label.grid(row = 1, column = 0, padx = (15, 10), pady = (15, 15), sticky = 'nw')
        self.textDescripcion = tk.Text(self.frameForm, width = 15, height = 4)
        self.textDescripcion.grid(row = 1, column = 1, padx = (10, 15), pady = (15, 15), sticky = 'nw')
        self.label = tk.Label(self.frameForm, text = 'Cragar archivo:')
        self.label.grid(row = 2, column = 0, padx = (15, 10), pady = (15, 15), sticky = 'w')
        self.buttonCargarArchivo = tk.Button(self.frameForm, text = 'Seleccionar', command = self.leerArchivo)
        self.buttonCargarArchivo.grid(row = 2, column = 1, padx = (10, 15), pady = (15, 15), sticky = 'w')
        self.buttonAceptar = tk.Button(self.frameForm, text = 'Aceptar', command = self.validarForm)
        self.buttonAceptar.grid(row = 3, column = 1, padx = (10, 15), pady = (15, 15), sticky = 'w')
        self.root.mainloop()
    def funcionNumerico(self, P):
        if not P: return True
        try:
            int(P)
            return True
        except ValueError:
            return False
    def leerArchivo(self):
        path = filedialog.askopenfilename(parent = self.root, initialdir = '/', title = 'Selecciona un archivo', filetypes = (('Archivos de texto', '*.txt'), ))
        if path != '':
            with open(path) as f:
                content = f.readlines()
            self.datosArchivo = [[int(i) for i in x.strip().split(',')] for x in content]
    def validarForm(self):
        if self.entryNumeroNodos.get() == '' or self.textDescripcion.get('1.0', 'end-1c') == '' or len(self.datosArchivo) == 0:
            messagebox.showerror(parent = self.root, title = "Error", message = "Llena todos los campos correctamente")
            return
        self.descripcionNodos = self.textDescripcion.get('1.0', 'end-1c').split('\n')
        if int(self.entryNumeroNodos.get()) != len(self.descripcionNodos):
            self.datosArchivo = []
            messagebox.showerror(parent = self.root, title = "Error", message = "El número de descripciones no coincide con el número de nodos")
            return
        self.guiResultado()
    def guiResultado(self):
        self.toplevel = tk.Toplevel(self.root)
        self.toplevel.title("Resultado")
        self.frameGrafo = tk.Frame(self.toplevel)
        self.frameGrafo.pack(side=tk.LEFT)
        self.figura = Figure(figsize = (6, 6), dpi = 100)
        self.a = self.figura.add_subplot(111)
        self.grafo = Grafo(self.datosArchivo)
        g = nx.Graph(self.grafo.aristas)
        nx.draw_networkx(g, ax = self.a)
        self.canvas = FigureCanvasTkAgg(self.figura, master = self.frameGrafo)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.frameGrafo)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.frameDatos = tk.Frame(self.toplevel)
        self.frameDatos.pack(side=tk.RIGHT)
        self.frameRow = tk.Frame(self.frameDatos)
        self.frameRow.pack(side = tk.TOP, pady = (15, 15), anchor = 'n')
        self.frameDescripcion = tk.Frame(self.frameRow)
        self.frameDescripcion.pack(side = tk.LEFT, padx = (10, 10))
        self.label = tk.Label(self.frameDescripcion, text = 'Descripción:')
        self.label.pack(anchor = 'w')
        self.listDescripcion = tk.Listbox(self.frameDescripcion)
        self.listDescripcion.pack()
        self.frameCliques = tk.Frame(self.frameRow)
        self.frameCliques.pack(side = tk.LEFT, padx = (10, 10))
        self.label = tk.Label(self.frameCliques, text = 'Cliques:')
        self.label.pack(anchor = 'w')
        self.listCliques = tk.Listbox(self.frameCliques)
        self.listCliques.pack()
        self.frameRow = tk.Frame(self.frameDatos)
        self.frameRow.pack(side = tk.TOP, pady = (15, 15), anchor = 'n')
        self.frameCliquesMaximos = tk.Frame(self.frameRow)
        self.frameCliquesMaximos.pack(side = tk.LEFT, padx = (10, 10))
        self.label = tk.Label(self.frameCliquesMaximos, text = 'Cliques máximos:')
        self.label.pack(anchor = 'w')
        self.listCliquesMaximos = tk.Listbox(self.frameCliquesMaximos)
        self.listCliquesMaximos.pack()
        self.frameTam = tk.Frame(self.frameRow)
        self.frameTam.pack(side = tk.LEFT, padx = (10, 10), anchor = 'n')
        self.label = tk.Label(self.frameTam, text = 'Tamaño máximo:')
        self.label.pack(anchor = 'w')
        self.entryTam = tk.Entry(self.frameTam, state = 'readonly')
        self.entryTam.pack()
        cliques = list(self.grafo.BronKerbosch())
        cliques.sort(key = len, reverse = True)
        maximo = len(cliques[0])
        maximos = [i for i in cliques if len(i) == maximo]
        for i in range(len(self.grafo.nodos)):
            self.listDescripcion.insert('end', [self.grafo.nodos[i], self.descripcionNodos[i]])
        for i in cliques:
            self.listCliques.insert('end', i)
        for i in maximos:
            self.listCliquesMaximos.insert('end', i)
        self.entryTam.config(state = 'normal')
        self.entryTam.insert('end', '%d' %maximo)
        self.entryTam.config(state = 'readonly')


gui = GUI()