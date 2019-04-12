import matplotlib.pyplot as plt
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
n = 20

# Initialize counter and declare maximum number of iterations
counter = 0
max_iter = 100

# Dictionary containing queens position
queens = dict()

# List of possible positions (used to put each queen in a unique row)
positions = list(range(n))

# Initialize Tabu list
tabu = []
tier1 = round(.2*n)
tier2 = round(.5*n)

# Create queens
for i in range(n):
    queens[i] = positions[np.random.randint(n - i)]
    positions.remove(queens[i])

# Calculate fitness of initial solution
J_best = (fitness(copy.copy(queens), None), copy.copy(queens))
J_cur = J_best

while J_best[0] > 0 and counter < max_iter:

    # Fitness vector
    J = []

    # Calculate fitness swapping each column to its neighbour
    for column in range(n):
        J.append(fitness(copy.copy(queens), column))

    # List containing positions to swap in order
    swappers = np.argsort(J)

    # Update current solution and add move to Tabu list
    for i in swappers:

        if i not in tabu:

            # Update queens position
            try:
                queens[i], queens[i + 1] = queens[i + 1], queens[i]
            except KeyError:
                queens[i], queens[0] = queens[0], queens[i]

            # Update current solution
            J_cur = (J[i], queens)

            # Add move to the end of Tabu list
            if len(tabu) >= round(.6*n):
                tabu = tabu[-round(.6*n):]
            tabu.append(i)

            # Exit loop
            break

        # In case move is not in tier1, but it is in Tabu list, and has solution better than J_best
        elif i not in tabu[-tier1:] and J[i] > J_best[0]:

            # Update queens position
            try:
                queens[i], queens[i + 1] = queens[i + 1], queens[i]
            except KeyError:
                queens[i], queens[0] = queens[0], queens[i]

            # Update current solution
            J_cur = (J[i], queens)

            # Remove move from middle of list and add it to the end of Tabu list
            tabu.remove(i)
            tabu.append(i)

            # Exit loop
            break

        # In case move is not in tier2, but it is in Tabu list, and has solution better than J_cur
        elif i not in tabu[-tier2:] and J[i] > J_cur[0]:

            # Update queens position
            try:
                queens[i], queens[i + 1] = queens[i + 1], queens[i]
            except KeyError:
                queens[i], queens[0] = queens[0], queens[i]

            # Update current solution
            J_cur = (J[i], queens)

            # Remove move from middle of list and add it to the end of Tabu list
            tabu.remove(i)
            tabu.append(i)

            # Exit loop
            break

    else:
        # This will occur if for loop ends without breaking
        print("All options are forbidden!")

    # Update best solution
    if J_cur[0] < J_best[0]:
        J_best = J_cur

    # Increase counter
    counter += 1

# Plot board for visual aid
board = np.zeros((n, n))
board[1::2, 0::2] = 1
board[0::2, 1::2] = 1

print("Solution for N-Queen Problem with n = %d" % n)
print("Number of restrictions: ", J_best[0])
print("Number of iterations: ", counter)

# Plot chessboard with queens
plt.figure()
plt.imshow(board.T, cmap='binary', interpolation='nearest')
plt.scatter(queens.keys(), queens.values())
plt.xticks(range(n))
plt.yticks(range(n))
plt.show()
