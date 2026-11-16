"""Apply valid inventory changes and report rejected request indices."""


def process_inventory(initial_stock, requests):
    if initial_stock < 0:
        raise ValueError("Initial stock cannot be negative")

    stock = initial_stock
    rejected_indices = []

    for index, request in enumerate(requests):
        try:
            change = int(request)
        except ValueError:
            rejected_indices.append(index)
        else:
            if stock + change < 0:
                rejected_indices.append(index)
            else:
                stock += change

        assert stock >= 0, "Stock cannot be negative"

    return [stock, rejected_indices]


if __name__ == "__main__":
    print(process_inventory(5, ["-3", "4", "-7", "2"]))

