def find_target_pairs(numbers, target_sum):
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")
    if not isinstance(target_sum, (int, float)):
        raise TypeError("target_sum must be a number")

    result = []
    for num1 in numbers:
        for num2 in numbers:
            if(num1 + num2 == target_sum):
                pair = (min(num1, num2), max(num1, num2))
                if not pair in result:
                    result.append(pair)

    return result

# time complexity: O(len(numbers)), there are two nested loop with length len(numbers) 

def main():
    nums = [2, 4, 3, 5, 7, 2]
    target = 7
    result = find_target_pairs(nums, target)
    print(result)

if __name__ == "__main__":
    main()