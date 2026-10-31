def binary_search_index(L, target):
    if not isinstance(L, list):
        raise TypeError("L must be a list")

    left = 0
    right = len(L) - 1
    while(left <= right):
    
        mid = (left + right) // 2
        
        if L[mid] == target:
            return mid
        elif L[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

def main():
    nums = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search_index(nums, 7))  
    print(binary_search_index(nums, 2))  

if __name__ == "__main__":
    main()