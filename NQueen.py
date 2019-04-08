import numpy as np

n = 15

queens = dict()

positions = list(range(n))

print(positions)

# Create queens
for i in range(n):
    queens[i] = positions[np.random.randint(n - i)]
    positions.remove(queens[i])
