class Item():
    def __init__(self, name, value, weight):
        if not isinstance(name, str):
            raise TypeError
        self.name = name

        if not isinstance(value, (int, float)) or not isinstance(weight, (int, float)):
            raise TypeError
        if value < 0 or weight <= 0:
            raise ValueError
        self.value = value
        self.weight = weight

    def get_value(self):
        return self.value
    
    def get_weight(self):
        return self.weight
    
    def get_density(self):
        return self.value / self.weight
    
    def __str__(self):
        return f"<{self.name}>: <{self.value}, {self.weight}>"


def flexible_greedy(items, max_weight, key_func):
    if not isinstance(items, list):
        raise TypeError
    for item in items:
        if not isinstance(item, Item):
            raise TypeError
    
    if not isinstance(max_weight, (int, float)):
        raise TypeError
    if max_weight < 0:
        raise ValueError

    if not callable(key_func):
        raise TypeError

    sorted_items = sorted(items, key=key_func, reverse=True)

    total_weight = 0
    total_value = 0
    taken_items = []
    for item in sorted_items:
        if total_weight + item.get_weight() <= max_weight:
            total_value += item.get_value()
            total_weight += item.get_weight()
            taken_items.append(item)

    return taken_items, total_value

def main():
    items = [
    Item("wine", 89, 123),
    Item("beer", 90, 154),
    Item("pizza", 95, 258),
    Item("burger", 100, 354),
    Item("apple", 50, 95)
    ]

    # 策略 1：依照價值最高優先 (Method reference)
    taken1, val1 = flexible_greedy(items, 500, Item.get_value)

    # 策略 2：依照重量最輕優先 (Lambda function)
    taken2, val2 = flexible_greedy(items, 500, lambda x: 1 / x.get_weight())

    # 策略 3：依照價值密度最高優先 (Method reference)
    taken3, val3 = flexible_greedy(items, 500, Item.get_density)

if __name__ == "__main__":
    main()