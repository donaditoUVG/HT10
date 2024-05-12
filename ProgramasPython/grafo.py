#Autor: José Donado

class Grafo:

    ##Matriz de Adyacencia
    def __init__(self, vertices):
        self.vertices = vertices
        self.matriz = [[float('inf')] * vertices for _ in range(vertices)]

    #Método para agregar arista (arco) entre un nodo y otro indicando el peso que existe en la conexión.
    def agregar_arco(self, origen, destino, peso):
        self.matriz[origen][destino] = peso
    # Imprimir matriz de adyacencia
    def imprimir_grafo(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.matriz[i][j] != float('inf'):
                    print(f'{i} -> {j}: {self.matriz[i][j]}')


##Aplicación

# Crear un grafo con 4 vértices
grafo = Grafo(5)

# Voy a agregar 5 arquitos
grafo.agregar_arco(0, 1, 5)
grafo.agregar_arco(0, 2, 10)
grafo.agregar_arco(1, 2, 3)
grafo.agregar_arco(2, 3, 7)
grafo.agregar_arco(4, 1, 1) #El último vértice 

# Mostrarr el grafo
grafo.imprimir_grafo()
