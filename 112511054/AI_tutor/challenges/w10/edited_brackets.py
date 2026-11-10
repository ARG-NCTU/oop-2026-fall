"""Check bracket balance after # removes the latest retained character."""


def balanced_after_edits(text):
    retained = []
    for char in text:
        if char == "#":
            if retained:
                retained.pop()
        else:
            retained.append(char)

    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for char in retained:
        if char in "([{":
            stack.append(char)
        elif not stack or stack.pop() != pairs[char]:
            return False
    return not stack


if __name__ == "__main__":
    import sys
    text = sys.stdin.readline().rstrip("\r\n")
    print(str(balanced_after_edits(text)).lower())
