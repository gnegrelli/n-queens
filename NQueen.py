import numpy as np
import copy


# This function calculates fitness of solution pivoting 2 columns if needed
def fitness(queen_list, pivot):

    if isinstance(pivot, int):
        try:
            queen_list[pivot], queen_list[pivot + 1] = queen_list[pivot + 1], queen_list[pivot]
        except KeyError:
            queen_list[pivot], queen_list[0] = queen_list[0], queen_list[pivot]

    fit = 0

    for key in queen_list.keys():
        for q in range(key + 1, len(queen_list)):
            if abs(key - q) == abs(queen_list[key] - queen_list[q]):
                # print("SAME DIAGONAL", key, q)
                fit += 1
    # print(50*"*")
    return fit


# Number of queens and size of chessboard
n = 15

# Dictionary containing queens position
queens = dict()

# List of possible positions (used to put each queen in a unique row)
positions = list(range(n))

# Initialize Tabu list
tabu = []
tier1 = 4
tier2 = 10

# Create queens
for i in range(n):
    queens[i] = positions[np.random.randint(n - i)]
    positions.remove(queens[i])

# Calculate fitness of initial solution
J_best = fitness(copy.copy(queens), None)

# Fitness vector
J = []

# Calculate fitness swapping each column to its neighbour
for column in range(n):
    J.append(fitness(copy.copy(queens), column))

# List containing positions to swap in order
swappers = np.argsort(J)

# Update queens position and add move to Tabu list
for i in swappers:

    # Update queens position
    if i not in tabu:
        try:
            queens[i], queens[i + 1] = queens[i + 1], queens[i]
        except KeyError:
            queens[i], queens[0] = queens[0], queens[i]

        # Add move to the end of Tabu list
        tabu.append(i)

        # Exit loop
        break

    # In case move is not in tier1, but it is in Tabu list, and has solution better than J_best
    elif i not in tabu[-tier1:] and J[i] > J_best:
        try:
            queens[i], queens[i + 1] = queens[i + 1], queens[i]
        except KeyError:
            queens[i], queens[0] = queens[0], queens[i]

        # Remove move from middle of list and add it to the end of Tabu list
        tabu.remove(i)
        tabu.append(i)

        # Exit loop
        break

else:
    # This will occur if for loop ends without breaking
    print("All options are forbidden!")

# Plot board for visual aid
# board = np.zeros((n, n))
# for key in queens.keys():
#     board[key, queens[key]] = 1
# print(board.T)

# print(J_best)
# print(J)
# print(np.argsort(J))
