# Original nested list
a = [[1, 2], [3, 4]]

# Make a shallow copy
b = a.copy()

# Modify the inner list through b
b[0][0] = 99

# Display both lists
print("a =", a)
print("b =", b)