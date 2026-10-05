def most_frequent(nums):
    freqs = {}

    for n in nums:
        if n in freqs:
            freqs[n] += 1
        else:
            freqs[n] = 1

    highest = max(freqs.values())
    result = []

    for n in freqs:
        if freqs[n] == highest:
            result.append(n)

    return (result, highest)


# Test 1
print(most_frequent([1, 2, 2, 3]))
# Expected: ([2], 2)


# Test 2
print(most_frequent([1, 1, 2, 2, 3]))
# Expected: ([1, 2], 2)


# Edge case
print(most_frequent([5]))
# Expected: ([5], 1)