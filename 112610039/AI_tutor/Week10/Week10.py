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

def solve_knapsack_dp(items, max_weight):
    def fast_max_val(to_consider, avail, memo={}):
        # base case
        if len(to_consider) == 0 or avail == 0:
            return (0, ())
        
        # try reading memo
        node = (len(to_consider), avail)
        if node in memo:
            return memo[node]

        if to_consider[0].get_weight() > avail:
            memo[node] = fast_max_val(to_consider[1:], avail, memo)
            return memo[node]
        else:
            with_res = fast_max_val(to_consider[1:], avail - to_consider[0].get_weight(), memo)
            with_val = with_res[0] + to_consider[0].get_value()
            with_take = with_res[1] + (to_consider[0], )
            without_res = fast_max_val(to_consider[1:], avail, memo)
            without_val = without_res[0]
            without_take = without_res[1]

            # write memo and return
            if(with_val > without_val):
                memo[node] = (with_val, with_take)
                return memo[node]
            else:
                memo[node] = (without_val, without_take)
                return memo[node]

            
    if not isinstance(items, list):
        raise TypeError
    for item in items:
        if not isinstance(item, Item):
            raise TypeError

    if not isinstance(max_weight, (int, float)):
        raise TypeError
    if max_weight < 0:
        raise ValueError
    
    res = fast_max_val(items, max_weight)
    (best_val, best_items) = res
    return best_val, best_items


def main():
    items = [
    Item("a", 6, 3),
    Item("b", 7, 3),
    Item("c", 8, 2),
    Item("d", 9, 5)
    ]

    best_val, best_items = solve_knapsack_dp(items, 5)
    print(f"best_val: {best_val}\n")
    print([item.name for item in best_items])

    # 最佳組合為 b (val=7, w=3) + c (val=8, w=2)
    # best_val -> 15
    # [item.name for item in best_items] -> ['c', 'b'] (順序可為 ['b', 'c'] 或 ['c', 'b'])

if __name__ == "__main__":
    main()