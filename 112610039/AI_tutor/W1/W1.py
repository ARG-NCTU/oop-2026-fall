def duplicate_evens(nums):
    
    copied_nums = nums[:]
    new_index = 0
    for num in copied_nums:
        if new_index >= len(copied_nums) - 1:
            break
        
        if num % 2 != 0:
            new_index += 1
        else:
            for i in range(len(copied_nums) - 1, new_index + 1, -1):
                nums[i] = nums[i-1]
            nums[new_index + 1] = nums[new_index]
            new_index += 2
    return None

def main():
    nums = [2, 1, 4, 3]
    duplicate_evens(nums)
    print(nums)

if __name__ == "__main__":
    main()