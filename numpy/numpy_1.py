# NumPy is a Python library used for fast numerical computations.
# basically used for array 1d 2d or 3d
import numpy as np

marks = np.array([1,2,3,4,5,6])

print(marks+5)

print(marks.shape)
print(marks[3])
print(marks[-3])
print(marks[1:4])

# new = marks.reshape(3,2)
# print(new)
print(marks.sum())
print(marks.max())
print(marks.min())
print(marks.mean())
rand = np.random.randint(1,10)
print(rand)


