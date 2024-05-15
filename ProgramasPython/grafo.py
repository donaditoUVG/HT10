import networkx as nx

class Grafo:

    def __init__(self):
        self.grafo = nx.DiGraph()

    def agregar_arco(self, origen, destino, peso):
        self.grafo.add_edge(origen, destino, weight=peso)

    def eliminar_arco(self, origen, destino):
        self.grafo.remove_edge(origen, destino)

    def imprimir_grafo(self):
        for origen, destino, datos in self.grafo.edges(data=True):
            peso = datos['weight']
            print(f'{origen} -> {destino}: {peso}')

    def calcular_excentricidades(self):
        excentricidades = {}
        for nodo in self.grafo.nodes():
            excentricidades[nodo] = max(nx.single_source_shortest_path_length(self.grafo, nodo).values())
        return excentricidades

    def mostrar_matriz_adyacencia(self):
        matriz = nx.adjacency_matrix(self.grafo)
        print("Matriz de adyacencia:")
        print(matriz.todense())

def leer_archivo(nombre_archivo, grafo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            origen, destino, normal, lluvia, nieve, tormenta = linea.split()
            normal = int(normal)
            grafo.agregar_arco(origen.lower(), destino.lower(), normal)

def escribir_archivo(nombre_archivo, grafo):
    with open(nombre_archivo, 'w') as archivo:
        for origen, destino, datos in grafo.grafo.edges(data=True):
            peso = datos['weight']
            # Se asumen los pesos para lluvia, nieve y tormenta como iguales a 'normal'
            archivo.write(f'{origen} {destino} {peso} {peso} {peso} {peso}\n')

def encontrar_centro(grafo):
    excentricidades = grafo.calcular_excentricidades()
    centro = min(excentricidades, key=excentricidades.get)
    return centro

# Crear un grafo
grafo = Grafo()

# Leer el archivo y construir el grafo
archivo_grafo = "C:/Users/josep/OneDrive - UVG/SEMESTRE III/Poo/HT10/HT10/lib/grafos.txt"
leer_archivo(archivo_grafo, grafo)

# Función para preguntar la ciudad de origen y destino y mostrar la ruta más corta
def ruta_mas_corta():
    origen = input("Ingrese el nombre de la ciudad de origen: ").lower()
    destino = input("Ingrese el nombre de la ciudad de destino: ").lower()
    if not grafo.grafo.has_node(origen) or not grafo.grafo.has_node(destino):
        print("Una o ambas ciudades no existen en el grafo.")
        return
    if nx.has_path(grafo.grafo, origen, destino):
        ruta = nx.shortest_path(grafo.grafo, origen, destino, weight='weight')
        distancia = nx.shortest_path_length(grafo.grafo, origen, destino, weight='weight')
        print(f"La ruta más corta entre {origen} y {destino} es de {distancia} horas.")
        print("Las ciudades intermedias en la ruta son: " + " -> ".join(ruta))
    else:
        print("No hay ruta disponible entre estas ciudades.")

# Función para modificar el grafo según las opciones especificadas
def modificar_grafo():
    print("Opciones de modificación:")
    print("a. Interrupción de tráfico entre un par de ciudades.")
    print("b. Establecer una conexión entre ciudad1 y ciudad2.")
    print("c. Indicar el clima entre un par de ciudades.")
    opcion = input("Seleccione una opción (a/b/c): ")
    if opcion == 'a':
        origen = input("Ingrese el nombre de la ciudad de origen: ").lower()
        destino = input("Ingrese el nombre de la ciudad de destino: ").lower()
        if not grafo.grafo.has_node(origen) or not grafo.grafo.has_node(destino):
            print("Una o ambas ciudades no existen en el grafo.")
            return
        if grafo.grafo.has_edge(origen, destino):
            grafo.eliminar_arco(origen, destino)
            print("Interrupción de tráfico establecida.")
        else:
            print("No hay tráfico entre estas ciudades para interrumpir.")
    elif opcion == 'b':
        origen = input("Ingrese el nombre de la ciudad de origen: ").lower()
        destino = input("Ingrese el nombre de la ciudad de destino: ").lower()
        peso = int(input("Ingrese el peso de la conexión: "))
        grafo.agregar_arco(origen, destino, peso)
        print("Conexión establecida.")
        # Sobrescribir el archivo con la nueva conexión
        escribir_archivo(archivo_grafo, grafo)
    elif opcion == 'c':
        origen = input("Ingrese el nombre de la ciudad de origen: ").lower()
        destino = input("Ingrese el nombre de la ciudad de destino: ").lower()
        clima = input("Ingrese el clima (normal/lluvia/nieve/tormenta): ").lower()
        if not grafo.grafo.has_node(origen) or not grafo.grafo.has_node(destino):
            print("Una o ambas ciudades no existen en el grafo.")
            return
        if clima not in ['normal', 'lluvia', 'nieve', 'tormenta']:
            print("Clima no válido.")
            return
        # Aquí se podría modificar el peso del arco según el clima
        print("Clima establecido.")
    else:
        print("Opción no válida.")

# Ciclo principal del programa
while True:
    print("\nOpciones:")
    print("1. Calcular ruta más corta entre dos ciudades.")
    print("2. Encontrar la ciudad que queda en el centro del grafo.")
    print("3. Modificar el grafo.")
    print("4. Mostrar matriz de adyacencia.")
    print("5. Finalizar el programa.")
    opcion = input("Seleccione una opción (1/2/3/4/5): ")
    if opcion == '1':
        ruta_mas_corta()
    elif opcion == '2':
        centro = encontrar_centro(grafo)
        print(f"La ciudad que queda en el centro del grafo es: {centro}")
    elif opcion == '3':
        modificar_grafo()
    elif opcion == '4':
        grafo.mostrar_matriz_adyacencia()
    elif opcion == '5':
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")
