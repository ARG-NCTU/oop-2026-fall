def move_zeros(L):
    pos1 = 0 #note next non-zero number
    for pos2 in range(len(L)): #pos2 notes where you are scanning
        if L[pos2] != 0:
            L[pos1] = L[pos2]

            pos1 += 1
    for i in range(pos1, len(L)):
        L[i] = 0