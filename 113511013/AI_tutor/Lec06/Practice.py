def total_items(name, packages, memo):
    """
    name: a string
    packages: dictionary mapping package names to lists of contents
    memo: dictionary storing package counts already calculated

    Returns the total number of individual items contained in name.
    If name is not a package key, it is treated as one individual item.
    """

    # Base case: this is an individual item, not another package
    if name not in packages:
        return 1

    # Reuse an answer that was already calculated
    if name in memo:
        return memo[name]

    total = 0

    # Recursive case: count every component inside this package
    for component in packages[name]:
        total += total_items(component, packages, memo)

    memo[name] = total
    return total


# -------------------------------------------------
# Tests
# -------------------------------------------------

packages1 = {
    "starter": ["pen", "notebook"],
    "school": ["starter", "starter", "ruler"]
}

memo1 = {}

# starter = pen + notebook = 2
assert total_items("starter", packages1, memo1) == 2

# school = starter + starter + ruler = 2 + 2 + 1 = 5
assert total_items("school", packages1, memo1) == 5

# Edge case: an individual item is not a key in the dictionary
assert total_items("pen", packages1, memo1) == 1


packages2 = {
    "mini": ["coin"],
    "box": ["mini", "mini", "mini"]
}

memo2 = {}

assert total_items("mini", packages2, memo2) == 1
assert total_items("box", packages2, memo2) == 3


# Empty package
packages3 = {
    "empty": []
}

memo3 = {}

assert total_items("empty", packages3, memo3) == 0


print("All tests passed!")
