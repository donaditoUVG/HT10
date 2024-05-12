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




# FUNCIÓN DE FLOYD WARSHALL
def floyd_warshall(grafo):
    distancias = grafo.matriz

    # Iterar sobre todos los vértices como nodos intermedios
    for k in range(grafo.vertices):
        # Iterar sobre todos los vértices como nodos de origen
        for i in range(grafo.vertices):
            # Iterar sobre todos los vértices como nodos de destino
            for j in range(grafo.vertices):
                # Si el camino de i a j a través de k es más corto, actualizar la distancia
                if distancias[i][j] > distancias[i][k] + distancias[k][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]

    return distancias

# Ejemplo de uso


# Llamar a la función floyd_warshall para obtener las distancias mínimas
distancias_minimas = floyd_warshall(grafo)

# Imprimir las distancias mínimas entre todos los pares de ciudades
for fila in distancias_minimas:     
    print(fila)
