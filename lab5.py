import itertools
import numpy as np

def read_matrix(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    n = len(lines)
    A = np.zeros((n, n))
    for i in range(n):
        row = lines[i].strip().split()
        for j in range(n):
            A[i,j] = int(row[j])
    return A

def is_isomorphic(A, B):
    # Перевірка, чи матриці мають однакову кількість вершин
    if A.shape[0] != B.shape[0]:
        return False
    n = A.shape[0]

    # Створив усі можливі перестановки вершин A
    perms = itertools.permutations(range(n))

    for perm in perms:
        #Створив матрицю перестановок P на основі поточної перестановки
        P = np.zeros((n, n))
        for i in range(n):
            P[i, perm[i]] = 1

        if np.array_equal(P.dot(A).dot(P.T), B):
            return True

    return False

A = read_matrix("matrix1.txt")
B = read_matrix("matrix2.txt")
print(A, '\n\n', B)

if is_isomorphic(A, B):
    print("The matrixes are isomorphic.")
else:
    print("The matrixes are not isomorphic.")
