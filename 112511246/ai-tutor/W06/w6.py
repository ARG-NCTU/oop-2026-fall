def has_pair_slow(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i]+nums[j] == target:
                return True
    return False



def has_pair_fast(nums, target):
    pair = {}
    for i in nums:
        if i in pair:
            return True
        pair[target-i] = None
    return False



if __name__ == "__main__":
    print(has_pair_slow([3, 8, 1, 5], 9))
    print(has_pair_slow([4, 2, 7], 8))
    print(has_pair_slow([4, 2, 4], 8))
    print(has_pair_slow([], 5))

    print(has_pair_fast([3, 8, 1, 5], 9))
    print(has_pair_fast([4, 2, 7], 8))
    print(has_pair_fast([4, 2, 4], 8))
    print(has_pair_fast([], 5))
