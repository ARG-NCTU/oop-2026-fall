def find_pair(nums, target):
    seen = {}

    for j in range(len(nums)):
        val = nums[j]
        complement = target - val

        # 如果前面已經看過需要的互補數，且那個 index 就是 i (< j)
        if complement in seen:
            return (seen[complement], j)

        # 只記錄每個數值「第一次」出現的 index，確保 i 最小
        if val not in seen:
            seen[val] = j

    return None
