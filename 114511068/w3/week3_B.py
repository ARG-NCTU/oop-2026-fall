def clean_numbers(n):
    clean = [2]

    for num in range(3, n + 1):
        is_div = False

        for x in clean:
            if num % x == 0:
                is_div = True
                break

        if not is_div:
            clean.append(num)

    return clean


print(clean_numbers(2))
print(clean_numbers(10))
print(clean_numbers(20))