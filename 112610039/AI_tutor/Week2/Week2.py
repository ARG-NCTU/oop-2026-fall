def target_sum(target, candidates, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == 0:
        return True
    if target < 0:
        return False

    for candidate in candidates:
        remainder = target - candidate
        if target_sum(remainder, candidates, memo):
            memo[target] = True
            return True

    memo[target] = False
    return False

def main():
    target = 7
    candidates = [2, 4]
    print(target_sum(target, candidates))

if __name__ == "__main__":
    main()