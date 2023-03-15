import math
from itertools import permutations

def tsp(matrix):
    n = len(matrix)
    min_cost = math.inf
    best_path = []
    for perm in permutations(range(n)):
        cost = 0
        for i in range(n - 1):
            cost += matrix[perm[i]][perm[i + 1]]
        cost += matrix[perm[n - 1]][perm[0]]
        if cost < min_cost:
            min_cost = cost
            best_path = perm
    return min_cost, best_path


with open('matrix.txt', 'r') as f:
    matrix = [[int(num) for num in line.split()] for line in f.readlines()]

t=tsp(matrix)
print(t)