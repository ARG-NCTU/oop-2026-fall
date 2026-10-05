def safe_average(values):
    try:
        nums = []

        for value in values:
            nums.append(float(value))

        return sum(nums) / len(nums)

    except ZeroDivisionError:
        return 0.0

    except (ValueError, TypeError):
        raise ValueError("invalid value")


# Test
print(safe_average([80, 90, 100]))
# Expected: 90.0

print(safe_average([]))
# Expected: 0.0