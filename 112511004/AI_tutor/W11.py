def min_presses(start, target):
    if start == target:
        return 0

    queue = [start]
    head = 0
    distance = {start: 0}

    while head < len(queue):
        state = queue[head]
        head += 1

        if state == target:
            return distance[state]

        for i in range(len(state) - 1):
            lights = list(state)

            # 同時反轉兩盞相鄰的燈
            lights[i] = "1" if lights[i] == "0" else "0"
            lights[i + 1] = "1" if lights[i + 1] == "0" else "0"

            next_state = "".join(lights)

            # 避免重複搜尋相同狀態
            if next_state not in distance:
                distance[next_state] = distance[state] + 1
                queue.append(next_state)

    return -1


if __name__ == "__main__":
    cases = [
        ("000", "101", 2),
        ("00", "01", -1),
        ("101", "101", 0),
        ("00", "11", 1),
        ("11", "00", 1),
        ("000", "011", 1),
        ("101", "000", 2),
        ("000", "001", -1),
        ("00000000", "11111111", 4),
        ("00000000", "10000001", 7),
        ("00000000", "00000001", -1),
    ]

    for start, target, expected in cases:
        actual = min_presses(start, target)
        assert actual == expected, (start, target, expected, actual)
        print(f"{start} -> {target}: expected={expected}, actual={actual}")

    print(f"Passed all {len(cases)} tests.")
