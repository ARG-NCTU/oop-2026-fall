def column_averages(matrix):
    if matrix == []:
        return []

    expected_length = len(matrix[0])

    # validate input structure first
    for row in matrix:
        if len(row) != expected_length:
            raise ValueError("all rows must have the same length")

    result = []

    for col in range(expected_length):
        total = 0

        for row in matrix:
            total += row[col]

        average = total / len(matrix)
        result.append(average)

    return result