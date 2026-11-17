from collections import deque


def degrees(friends, a, b):
    if a == b:
        return 0
    seen = {a: True}
    queue = deque([(a, 0)])
    while queue:
        person, d = queue.popleft()
        for f in friends[person]:
            if f == b:
                return d + 1
            if f not in seen:
                seen[f] = True
                queue.append((f, d + 1))
    return -1


if __name__ == "__main__":
    friends = {
        "Amy": ["Ben", "Cat"],
        "Ben": ["Amy", "Dan"],
        "Cat": ["Amy", "Dan"],
        "Dan": ["Ben", "Cat", "Eve"],
        "Eve": ["Dan"],
        "Frank": [],
    }
    print(degrees(friends, "Amy", "Ben"))
    print(degrees(friends, "Amy", "Dan"))
    print(degrees(friends, "Amy", "Eve"))
    print(degrees(friends, "Amy", "Amy"))
    print(degrees(friends, "Amy", "Frank"))
