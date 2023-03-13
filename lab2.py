def dijkstra(graph, source, dest):
    distances = [float('inf') for i in range(len(graph))]
    visited = [False for i in range(len(graph))]
    distances[source] = 0

    if source == dest:
        return 0

    for i in range(len(graph)):

        # Знайдіть невідвіданий вузол із найменшою орієнтовною відстанню
        min_dist = float('inf')
        min_index = None
        for j in range(len(graph)):
            if not visited[j] and distances[j] < min_dist:
                min_dist = distances[j]
                min_index = j
        #print(min_index)
        #print(min_dist)
        # Позначити поточний вузол як відвіданий
        visited[min_index] = True
        # Оновити відстані до своїх сусідів
        for j in range(len(graph)):
            if graph[min_index][j] != 0 and not visited[j]:
                new_dist = distances[min_index] + graph[min_index][j]
                if new_dist < distances[j]:
                    distances[j] = new_dist

    return distances[dest]

def sum_edges(graph):
    return sum([graph[i][j] for i in range(len(graph)) for j in range(i, len(graph))])

# Знаходження вершин непарного степеня в графі

def get_unpair(graph):
    degree = [0 for i in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if (graph[i][j] != 0):
                degree[i] += 1

    print(degree)
    unpair = [i for i in range(len(degree)) if degree[i] % 2 != 0]
    print('unpair are:',unpair)
    return unpair

def gen_pairs(odds):
    pairs = []
    for i in range(len(odds) - 1):
        pairs.append([])
        for j in range(i + 1, len(odds)):
            pairs[i].append([odds[i], odds[j]])

    print('pairs are:',pairs)
    print('\n')
    return pairs

def Postman(graph):
    odds = get_unpair(graph)
    if (len(odds) == 0):
        return sum_edges(graph)
    pairs = gen_pairs(odds)
    l = (len(pairs) + 1) // 2

    pairing = []

    def get_pairs(pairs, done=[], final=[]):

        if (pairs[0][0][0] not in done):
            done.append(pairs[0][0][0])

            for i in pairs[0]:
                f = final[:]
                val = done[:]
                if (i[1] not in val):
                    f.append(i)
                else:
                    continue

                if (len(f) == l):
                    pairing.append(f)
                    return
                else:
                    val.append(i[1])
                    get_pairs(pairs[1:], val, f)

        else:
            get_pairs(pairs[1:], done, final)

    get_pairs(pairs)
    min_sums = []

    for i in pairing:
        s = 0
        for j in range(len(i)):
            s += dijkstra(graph, i[j][0], i[j][1])
        min_sums.append(s)

    added_dis = min(min_sums)

    chinese_dis = added_dis + sum_edges(graph)
    return chinese_dis
with open('matrix.txt', 'r') as f:
    matrix = [[int(num) for num in line.split()] for line in f.readlines()]

print('Postman Distance is:', Postman(matrix))