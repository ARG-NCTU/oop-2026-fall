def move_zeros(L):
    pos1 = 0 #note next non-zero number
    for pos2 in range(len(L)): #pos2 notes where you are scanning
        if L[pos2] != 0:
            L[pos1] = L[pos2]

            pos1 += 1
    for i in range(pos1, len(L)):
        L[i] = 0

L1 = [0, 3, 0, 1, 5]
move_zeros(L1)
print(L1)
assert L1 == [3, 1, 5, 0, 0]

L2 = [1, 2, 3]
move_zeros(L2)
print(L2)
assert L2 == [1, 2, 3]

L3 = [0, 0, 0]
move_zeros(L3)
print(L3)
assert L3 == [0, 0, 0]

L4 = []
move_zeros(L4)
print(L4)
assert L4 == []

L5 = [0, 1, 0, 2]
move_zeros(L5)
print(L5)
assert L5 == [1, 2, 0, 0]

L6 = [1, 0]
move_zeros(L6)
print(L6)
assert L6 == [1, 0]

print("All tests passed!")