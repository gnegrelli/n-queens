import numpy as np
import copy

n = 15

queens = dict()

positions = list(range(n))

# Create queens
for i in range(n):
    queens[i] = positions[np.random.randint(n - i)]
    positions.remove(queens[i])

J = 0

# print(queens)

# Calculate fitness of solution
for key in queens.keys():
    for q in range(key + 1, n):
        if abs(key - q) == abs(queens[key] - queens[q]):
            # print("SAME DIAGONAL", key, q)
            J += 1

board = np.zeros((n, n))

for key in queens.keys():
    board[key, queens[key]] = 1

print(board.T)
print(J)
