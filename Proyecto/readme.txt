Ruvalcaba Montoya Jesús Eduardo 3CM4

Este programa fue desarrollado en el lenguaje de programación Python
Este programa requiere las siguientes bibliotecas externas:
	- networkx 	Utilizada para dibujar el grafo
	- matplotlib	Utilizada para mostrar el grafo dibujado
Ambas bibliotecas pueden instalarse utilizando el administrador de paquetes "pip", escribiento los siguientes comandos en una terminal
	- pip install networkx
	- pip install matplotlib

Para ejecutar el programa, seguir los siguientes pasos:
	- Abrir una terminal
	- Posicionarse en la ubicación del programa
	- Ejecutar el comando "python Proyecto.py"

El programa mostrará en pantalla el formulario inicial:
	- En el primer campo se debe proporcionar el numero de nodos
	- En el segundo campo se debe proporcionar a descripción de cada uno de los nodos (es decir, que representa cada nodo, puede ser el nombre de una 
	  persona o el nombre de un lugar), separados por saltos de línea. Ejemplo: Si tenemos 3 nodos, la descripción debería verse de la siguiente manera:
 		Eduardo
		Itzel
		Nemo
	- Un archivo con los datos de las aristas (nodos conectados). Este último archivo debe tener la siguiente estructura:
		nodo1,nodo2
	  Ejemplo: si tenemos 3 nodos conectados entre sí, el archivo quedaría de la siguiente manera:
		0,1
		0,2
		1,0
		1,2
		2,0
		2,1
	El número relacionado al primer nodo de la relación, seguido de una coma, y el número relacionado al segundo nodo de la relación.
	Los nodos deben ser numerados del 0 al n-1 (n es el número de nodos), y se deben incluir las uniones de cada uno de los nodos, esto con el fin de
	formar la matriz de adyacencia.
	Para mayor referencia, junto con el código fuente se incluye un archivo de prueba con esta estructura.

Al precionar el botón aceptar se generará el grafo, y una lista con las descripciones, los cliques, los máximos cliques y el tamaño máximo de los cliques 
