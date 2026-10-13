def pass_list(scores, limit):
    passed = []
    count = 0

    for i in scores:
        if i >= limit:
            passed.append(i)
        else:
            count += 1

    passed.sort()
    return (passed, count)


if __name__ == "__main__":
    scores = [70, 45, 90, 60]
    print(pass_list(scores, 60))
    print(scores)

    print(pass_list([50, 80, 50], 60))
    print(pass_list([], 60))
