import networkx as nx
import matplotlib.pyplot as plt

# Definir el grafo como un diccionario de listas de adyacencia
graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F', 'D'],
    'F': ['C']
}

# Crear el grafo dirigido y añadir nodos y aristas
G = nx.DiGraph() # se crea el grafo dirigido
for node, edges in graph.items():
    for edge in edges:
        G.add_edge(node, edge) # se agregan nodos y aristas al grafo dirigido

# Construir el árbol BFS y calcular las distancias
bfs_tree = nx.bfs_tree(G, 'A') # se construye el árbol BFS
distances = nx.shortest_path_length(G, 'A') # se calculan las distancias desde el nodo inicial

# Dibujar el grafo con las distancias y el color del nodo inicial
node_colors = ['red' if node == 'A' else 'lightblue' for node in G.nodes] # se asigna el color rojo al nodo inicial y celeste a los demás nodos
pos = nx.spring_layout(G) # se define la disposición de los nodos del grafo
nx.draw(G, pos=pos, with_labels=True, node_color=node_colors, node_size=500, font_size=16) # se dibuja el grafo con las opciones definidas

# Añadir las distancias a cada nodo como etiquetas
labels = {node: str(distances[node]) for node in G.nodes} # se crea un diccionario con las distancias de cada nodo
for node, label in labels.items():
    x, y = pos[node]
    dx, dy = x , y 
    dx *= 0.25
    dy *= 0.25
    align = 'center'
    if dy > 0:
        align = 'bottom'
    elif dy < 0:
        align = 'top'
    nx.draw_networkx_labels(G, {node: (x - dx, y - dy)}, labels={node: label}, font_size=12, horizontalalignment='center', verticalalignment=align,font_color='blue') # se añaden las etiquetas de las distancias a cada nodo del grafo


plt.show() # se muestra la figura

# Mostrar el recorrido BFS y las distancias en consola
visited = []
queue = ['A']

while queue:
    vertex = queue.pop(0)
    if vertex not in visited:
        visited.append(vertex)
        queue.extend(graph[vertex])

print('Recorrido BFS:', visited) # se imprime el recorrido BFS en consola

