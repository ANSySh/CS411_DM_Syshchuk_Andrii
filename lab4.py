def dfs(C, F, s, t, paths=None):
    if paths is None:
        paths = {s: []}
    if s == t:
        return paths[s]
    for v in range(len(C)):
        if (C[s][v] - F[s][v] > 0) and v not in paths:
            flow_path = dfs(C, F, v, t, {**paths, v: paths[s]+[(s,v)]})
            if flow_path is not None:
                return flow_path
    return None

def max_flow(a, s, t):
    n = len(a)
    f = [[0] * n for i in range(n)]
    path = dfs(a, f, s, t)
    while path is not None:
        flow = min(a[u][v] - f[u][v] for u, v in path)
        for u, v in path:
            f[u][v] += flow
            f[v][u] -= flow
        path = dfs(a, f, s, t)
        print(path)
    return sum(f[s][i] for i in range(n))

array = [[float(j) if '.' in j else int(j) for j in i.split()] for i in open("matrix.txt", "r").read().splitlines()[1:]]
numberOfNodes = len(array)
print(*['\t'.join(map(str, row)) for row in array], sep='\n')
max_flow_value = max_flow(array, 0, numberOfNodes - 1)
print("\nmax flow value is:", max_flow_value)
