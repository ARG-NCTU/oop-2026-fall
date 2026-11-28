# W9 AI Tutor Part B: Menu Picker (MIT 6.0002 Lec 1: Introduction and Optimization Problems)
#
# Food(name, value, calories)
# greedy(foods, max_cal, key)  -> (total value, list of chosen foods), take items in order of key
# brute_force(foods, max_cal)  -> (best total value, chosen foods), try all 2^n subsets


class Food(object):
    def __init__(self, name, value, calories):
        self.name = name
        self.value = value
        self.calories = calories

    def get_value(self):
        return self.value

    def get_cost(self):
        return self.calories

    def density(self):
        return self.value / self.calories

    def __str__(self):
        return self.name + ": <" + str(self.value) + ", " + str(self.calories) + ">"


def greedy(foods, max_cal, key):
    items = sorted(foods, key=key, reverse=True)     # O(n log n), input not changed
    result, total_value, total_cost = [], 0, 0
    for f in items:
        if total_cost + f.get_cost() <= max_cal:
            result.append(f)
            total_cost += f.get_cost()
            total_value += f.get_value()
    return total_value, result


def brute_force(foods, max_cal):
    best_value, best_set = 0, []
    n = len(foods)
    for mask in range(2 ** n):                       # every subset, O(n * 2^n)
        chosen = [foods[i] for i in range(n) if mask >> i & 1]
        cost = sum(f.get_cost() for f in chosen)
        value = sum(f.get_value() for f in chosen)
        if cost <= max_cal and value > best_value:
            best_value, best_set = value, chosen
    return best_value, best_set


if __name__ == "__main__":
    # provided example: greedy by density is NOT optimal here
    menu = [Food("salad", 6, 5), Food("soup", 6, 5), Food("steak", 7, 5.5)]
    g_value, g_items = greedy(menu, 10, Food.density)
    b_value, b_items = brute_force(menu, 10)
    assert [f.name for f in g_items] == ["steak"] and g_value == 7
    assert b_value == 12 and sorted(f.name for f in b_items) == ["salad", "soup"]

    # different keys can give different answers
    by_value = greedy(menu, 10, Food.get_value)[0]
    by_cost = greedy(menu, 10, lambda f: 1 / f.get_cost())[0]
    assert by_value == 7 and by_cost == 12

    # edge cases
    assert greedy([], 10, Food.density) == (0, [])
    assert brute_force([], 10) == (0, [])
    assert greedy(menu, 0, Food.density) == (0, [])          # nothing fits
    assert brute_force(menu, 0)[0] == 0
    assert brute_force(menu, 100)[0] == 19                    # everything fits
    assert [f.name for f in menu] == ["salad", "soup", "steak"]  # input not reordered

    # greedy is never better than the optimum
    import random
    for _ in range(200):
        foods = [Food(str(i), random.randint(1, 20), random.randint(1, 10))
                 for i in range(random.randint(0, 7))]
        cap = random.randint(0, 25)
        for key in (Food.density, Food.get_value):
            assert greedy(foods, cap, key)[0] <= brute_force(foods, cap)[0]

    print("all tests passed")
