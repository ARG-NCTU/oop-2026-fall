def defensive_merge_sort(L):
    def merge(L1, L2):
        result = []
        tracer1 = 0
        tracer2 = 0

        while tracer1 != len(L1) and tracer2 != len(L2):
            if(L1[tracer1] > L2[tracer2]):
                result.append(L2[tracer2])
                tracer2 += 1
            else:
                result.append(L1[tracer1])
                tracer1 += 1

        while tracer1 != len(L1):
            result.append(L1[tracer1])
            tracer1 += 1
        while tracer2 != len(L2):
            result.append(L2[tracer2])
            tracer2 += 1

        return result

    
    if not isinstance(L, list):
        raise TypeError("Input must be list")
    for num in L:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements in the list must be numbers")
    
    if len(L) <= 1:
        return L

    middle = len(L) // 2
    sorted_left = defensive_merge_sort(L[:middle])
    sorted_right = defensive_merge_sort(L[middle:])
    return merge(sorted_left, sorted_right)


def main():
    nums = [8, 4, 1, 6, 5, 9, 2, 0]
    sorted_nums = defensive_merge_sort(nums[:])
    print(nums)
    print(sorted_nums)

if __name__ == "__main__":
    main()