def remove_target(nums, target):
    new_list = [x for x in nums if x != target]
    ans = len(nums) - len(new_list)
    nums[:] = new_list
    return ans


# Normal case
nums = [2, 1, 2, 3, 2, 4]
print(remove_target(nums, 2), nums)

# Aliasing test
nums = [2, 1, 2, 3]
alias = nums

removed = remove_target(nums, 2)

print(removed)
print(nums)
print(alias)
print(nums is alias)