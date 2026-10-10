
def first_duplicate(transactions):
    min = -1
    min_index = 20000

    for i in range(len(transactions)):
        temp = transactions[i]

        for j in range(i + 1, len(transactions)):
            if transactions[j] == temp and j < min_index:
                min = transactions[j]
                min_index = j

    return min
