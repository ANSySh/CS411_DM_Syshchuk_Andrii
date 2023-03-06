import networkx as nx
import matplotlib.pyplot as plt

matrix = [
    [0, 0, 38, 95, 0, 1, 57, 0],
    [0, 0, 0, 0, 79, 0, 36, 19],
    [38, 0, 0, 51, 0, 0, 44, 0],
    [95, 0, 51, 0, 0, 44, 0, 0],
    [0, 79, 0, 0, 0, 93, 41, 48],
    [1, 0, 0, 44, 93, 0, 1, 0],
    [57, 36, 44, 0, 41, 1, 0, 0],
    [0, 19, 0, 0, 48, 0, 0, 0]
]

A = nx.Graph()
A.add_nodes_from(range(len(matrix)))

# Додавання зважених ребер
for i in range(len(matrix)):
    for j in range(i + 1, len(matrix[i])):
        weight = matrix[i][j]
        if weight > 0:
            A.add_edge(i, j, weight=weight)

# Візуалізація графа
pos = nx.spring_layout(A)
edge_labels = nx.get_edge_attributes(A, "weight")
nx.draw_networkx_edge_labels(A, pos, edge_labels=edge_labels, font_color='green')
nx.draw(A, pos, with_labels=True)
plt.show()


def boruvka_mst(graph):
    # Ініціалізація порожнього списку для збереження ребер
    mst = []

    # Отримання кількості вершин в графі
    n = len(graph)
    # Ініціалізація списку для відстеження найменшого ребра для кожної компоненти
    cheapest = [None] * n

    # Ініціалізація списку для відстеження компоненти кожної вершини
    component = [i for i in range(n)]

    while len(set(component)) > 1:
        # Для кожної компоненти знайти найменше ребро, що з'єднує її з іншою компонентою
        for i in range(n):
            min_edge = None
            for j in range(n):
                if graph[i][j] > 0 and component[i] != component[j]:
                    if min_edge is None or graph[i][j] < graph[min_edge[0]][min_edge[1]]:
                        min_edge = (i, j)
            cheapest[i] = min_edge

        for i, edge in enumerate(cheapest):
            if edge is not None:
                if component[edge[0]] != component[edge[1]]:
                    weight = graph[edge[0]][edge[1]]
                    mst.append((edge[0], edge[1], weight))
                    old_component = component[edge[1]]
                    new_component = component[edge[0]]
                    for j in range(n):
                        if component[j] == old_component:
                            component[j] = new_component
    return mst

mst = boruvka_mst(matrix)
for edge in mst:
    print(f"({edge[0]}, {edge[1]}) weight={edge[2]}")
#[(0, 5), (1, 7), (2, 0), (3, 5), (4, 6), (6, 5), (1, 6)]