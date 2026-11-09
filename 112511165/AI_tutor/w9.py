def fractional_knapsack(items, capacity):
    # 依照單位價值 (value / weight) 由大到小排序，使用 sorted 確保不修改原串列
    sorted_items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0.0
    remaining_capacity = capacity

    for val, weight in sorted_items:
        if remaining_capacity == 0:
            break

        if weight <= remaining_capacity:
            # 整件裝進去
            total_value += val
            remaining_capacity -= weight
        else:
            # 只能切一部分裝滿剩餘空間
            fraction = remaining_capacity / weight
            total_value += val * fraction
            remaining_capacity = 0
            break

    return round(total_value, 2)
