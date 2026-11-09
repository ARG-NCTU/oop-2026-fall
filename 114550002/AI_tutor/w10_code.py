def sortSquares(nums):
    n = len(nums)
    ans = []
    pos = 0
    while pos < n and nums[pos] < 0:
        pos = pos + 1
    neg = pos - 1
    for _ in range(n):
        if pos == n:
            ans.append(nums[neg] * nums[neg])
            neg = neg - 1
        elif neg == -1:
            ans.append(nums[pos] * nums[pos])
            pos = pos + 1
        else:
            if nums[neg] * nums[neg] <= nums[pos] * nums[pos]:
                ans.append(nums[neg] * nums[neg])
                neg = neg - 1
            else:
                ans.append(nums[pos] * nums[pos])
                pos = pos + 1
    return ans