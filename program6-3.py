import numpy as np
matrix = np.array([[8, 1, 6],
                   [3, 5, 7],
                   [4, 9, 2]])
column_sum = matrix.sum(axis = 0)
row_sum = matrix.sum(axis = 1)

print(f"Column:{column_sum}")
print(f"Row:{row_sum}")