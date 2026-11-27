def signed_expr_ways(nums: list[int], target: int) -> int:
    """Return the number of ways to assign + and - signs to nums to reach the target."""

    memo = dict()

    def count_ways(index: int, current_sum: int) -> int:
        if index == len(nums):
            return 1 if current_sum == target else 0

        if (index, current_sum) in memo:
            return memo[(index, current_sum)]

        # Choose + or - for the current number
        positive = count_ways(index + 1, current_sum + nums[index])
        negative = count_ways(index + 1, current_sum - nums[index])

        memo[(index, current_sum)] = positive + negative
        return memo[(index, current_sum)]

    return count_ways(0, 0)
