import numpy as np
import copy


# This function calculates fitness of solution pivoting 2 columns if needed
def fitness(queen_list, pivot):

    if isinstance(pivot, int):
        try:
            queen_list[pivot], queen_list[pivot + 1] = queen_list[pivot + 1], queen_list[pivot]
        except KeyError:
            queen_list[pivot], queen_list[0] = queen_list[0], queen_list[pivot]

    J = 0

    for key in queen_list.keys():
        for q in range(key + 1, len(queen_list)):
            if abs(key - q) == abs(queen_list[key] - queen_list[q]):
                print("SAME DIAGONAL", key, q)
                J += 1

    return J


n = 15

queens = dict()

positions = list(range(n))

# Create queens
for i in range(n):
    queens[i] = positions[np.random.randint(n - i)]
    positions.remove(queens[i])

J = fitness(copy.copy(queens), None)

board = np.zeros((n, n))

for key in queens.keys():
    board[key, queens[key]] = 1

print(board.T)
print(J)
