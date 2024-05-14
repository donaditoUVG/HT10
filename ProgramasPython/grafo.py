class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.matriz = [[float('inf')] * vertices for _ in range(vertices)]

    def agregar_arco(self, origen, destino, peso):
        self.matriz[origen][destino] = peso

    def eliminar_arco(self, origen, destino):
        self.matriz[origen][destino] = float('inf')

    def imprimir_grafo(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.matriz[i][j] != float('inf'):
                    print(f'{i} -> {j}: {self.matriz[i][j]}')

    def imprimir_matriz_adyacencia(self):
        print("Matriz de Adyacencia:")
        for fila in self.matriz:
            print(fila)

def leer_archivo(nombre_archivo, grafo, ciudades):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            origen, destino, normal, lluvia, nieve, tormenta = linea.split()
            normal = int(normal)
            grafo.agregar_arco(ciudades[origen], ciudades[destino], normal)

def floyd_warshall(grafo):
    distancias = grafo.matriz
    for k in range(grafo.vertices):
        for i in range(grafo.vertices):
            for j in range(grafo.vertices):
                if distancias[i][j] > distancias[i][k] + distancias[k][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]
    return distancias

def encontrar_centro(grafo):
    suma_minima = float('inf')
    centro = -1
    for i in range(grafo.vertices):
        suma_actual = sum(grafo.matriz[i])
        if suma_actual < suma_minima:
            suma_minima = suma_actual
            centro = i
    return centro

# Crear el diccionario para mapear nombres de ciudades a índices
ciudades = {}
with open("C:\\Users\\lirof\\OneDrive\\Escritorio\\DONADO UVG YESSIR! HT10\\HT10\\lib\\grafos.txt", 'r') as archivo:
    lineas = archivo.readlines()
    for i, linea in enumerate(lineas):
        origen, destino, _, _, _, _ = linea.split()
        if origen not in ciudades:
            ciudades[origen] = len(ciudades)
        if destino not in ciudades:
            ciudades[destino] = len(ciudades)

# Crear un grafo con el número correcto de vértices
grafo = Grafo(len(ciudades))

# Leer el archivo y construir el grafo
leer_archivo("C:\\Users\\lirof\\OneDrive\\Escritorio\\DONADO UVG YESSIR! HT10\\HT10\\lib\\grafos.txt", grafo, ciudades)

# Aplicar el algoritmo de Floyd-Warshall
distancias_minimas = floyd_warshall(grafo)


# Función para preguntar la ciudad de origen y destino y mostrar la ruta más corta
def ruta_mas_corta():
    origen = input("Ingrese el nombre de la ciudad de origen: ")
    destino = input("Ingrese el nombre de la ciudad de destino: ")
    if origen not in ciudades or destino not in ciudades:
        print("Una o ambas ciudades no existen en el grafo.")
        return
    origen_idx = ciudades[origen]
    destino_idx = ciudades[destino]
    distancia = distancias_minimas[origen_idx][destino_idx]
    if distancia == float('inf'):
        print("No hay ruta disponible entre estas ciudades.")
        return
    print(f"La ruta más corta entre {origen} y {destino} es de {distancia} unidades.")

# Función para encontrar la ciudad en el centro del grafo
def ciudad_centro():
    centro_idx = encontrar_centro(grafo)
    for ciudad, idx in ciudades.items():
        if idx == centro_idx:
            print(f"La ciudad que queda en el centro del grafo es: {ciudad}")
            break

# Función para modificar el grafo según las opciones especificadas
def modificar_grafo():
    print("Opciones de modificación:")
    print("a. Interrupción de tráfico entre un par de ciudades.")
    print("b. Establecer una conexión entre ciudad1 y ciudad2.")
    print("c. Indicar el clima entre un par de ciudades.")
    opcion = input("Seleccione una opción (a/b/c): ")
    if opcion == 'a':
        origen = input("Ingrese el nombre de la ciudad de origen: ")
        destino = input("Ingrese el nombre de la ciudad de destino: ")
        if origen not in ciudades or destino not in ciudades:
            print("Una o ambas ciudades no existen en el grafo.")
            return
        grafo.eliminar_arco(ciudades[origen], ciudades[destino])
        print("Interrupción de tráfico establecida.")
    elif opcion == 'b':
        origen = input("Ingrese el nombre de la ciudad de origen: ")
        destino = input("Ingrese el nombre de la ciudad de destino: ")
        peso = int(input("Ingrese el peso de la conexión: "))
        if origen not in ciudades:
            ciudades[origen] = len(ciudades)
        if destino not in ciudades:
            ciudades[destino] = len(ciudades)
        grafo.agregar_arco(ciudades[origen], ciudades[destino], peso)
        print("Conexión establecida.")
    elif opcion == 'c':
        origen = input("Ingrese el nombre de la ciudad de origen: ")
        destino = input("Ingrese el nombre de la ciudad de destino: ")
        clima = input("Ingrese el clima (normal/lluvia/nieve/tormenta): ")
        if origen not in ciudades or destino not in ciudades:
            print("Una o ambas ciudades no existen en el grafo.")
            return
        if clima not in ['normal', 'lluvia', 'nieve', 'tormenta']:
            print("Clima no válido.")
            return
        # Aquí se podría modificar el peso del arco según el clima
        print("Clima establecido.")
    else:
        print("Opción no válida.")

# Función para mostrar la matriz de adyacencia
def mostrar_matriz_adyacencia():
    grafo.imprimir_matriz_adyacencia()

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
        ciudad_centro()
    elif opcion == '3':
        modificar_grafo()
    elif opcion == '4':
        mostrar_matriz_adyacencia()
    elif opcion == '5':
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")
# Calculate the center of the graph
centro = encontrar_centro(grafo)

