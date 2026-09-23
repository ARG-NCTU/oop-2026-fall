def count_paths(rows, cols):
    if rows == 1 or cols == 1:
        return 1
    
    return count_paths(rows - 1, cols) + count_paths(rows, cols - 1)

def count_paths_multi(rows, cols, memo):
    if rows == 1 or cols == 1:
        return 1

    if (rows, cols) in memo:
        return memo[(rows, cols)]

    ans = count_paths(rows - 1, cols, memo) + count_paths(rows, cols - 1, memo)

    memo[(rows, cols)] = ans

    return ans


memo = {}
print(count_paths(3, 4, memo))