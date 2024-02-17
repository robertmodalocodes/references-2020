import numpy as np
# array operation

# flattening
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = np.ravel(a)

print("matrix a: \n", a)
print("")
print("matrix a flattened: \n", b)
print("")

# reshape the flattened matrix
c = np.reshape(b, (3, 3))
print("matrix a reshaped: \n", c)
print("")

# replicate an array/vector into a matrix
d = np.tile(a, 2)  # a is for the matrix, 2 is for the number of replication
print("matrix a replicated: \n", d)
print("")

# transposing
e = np.transpose(a)
print("matrix a transposed: \n", e)
print("")

# selection
data = [[1,   3,  4],
        [5,   6,  7],
        [9,  10, 11],
        [14, 16, 17],
        [20, 25, 30],
        [35, 37, 45]]

f = np.array(data)
print("matrix f: \n", f)
print("")


# [row, column]
g = np.array(f[0:4, 0:2])  # selecting data in a matrix
print("selected f: [0:3], [0,1]\n", g)
print("*"*100)

# stacking matrix
# stacking vertically
h = np.vstack((a, f))
print("matrix a vertically stacked with f:\n", h)
print("")

# stacking horizontally
i = np.hstack((a, np.transpose(f)))
print("matrix a horizontally stacked with f:\n", i)
print("")

j = np.dot(h, i)
print("matrix i multiplied by j\n", j)
print("")
