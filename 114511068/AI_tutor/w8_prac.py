
def find_closest_score(scores, target):
    # Handle an empty list
    if len(scores) == 0:
        return None

    # Recursively find the target or its insertion position
    def binary_search(low, high):
        # Base case: target is not in the list
        if low > high:
            return low

        mid = (low + high) // 2

        if scores[mid] == target:
            return mid
        elif scores[mid] < target:
            return binary_search(mid + 1, high)
        else:
            return binary_search(low, mid - 1)

    # Find the target's position or insertion position
    pos = binary_search(0, len(scores) - 1)

    # Target would be inserted before the first element
    if pos == 0:
        return scores[0]

    # Target would be inserted after the last element
    if pos == len(scores):
        return scores[-1]

    # Compare the two neighboring candidates
    left = scores[pos - 1]
    right = scores[pos]

    # Return the closer score; choose the smaller one in a tie
    if abs(target - left) <= abs(right - target):
        return left
    else:
        return right


# Test cases
print("Example 1:")
print(find_closest_score([10, 20, 35, 50, 80], 36))
# Expected output: 35

print("Example 2:")
print(find_closest_score([10, 20, 35, 50, 80], 42))
# Expected output: 35

print("Example 3:")
print(find_closest_score([], 25))
# Expected output: None

print("Edge case 1:")
print(find_closest_score([5], 8))
# Expected output: 5

print("Edge case 2:")
print(find_closest_score([10, 20], 15))
# Expected output: 10

print("Edge case 3:")
print(find_closest_score([10, 20, 30], 5))
# Expected output: 10

print("Edge case 4:")
print(find_closest_score([10, 20, 30], 40))
# Expected output: 30

print("Edge case 5:")
print(find_closest_score([10, 20, 35, 50, 80], 50))
# Expected output: 50
