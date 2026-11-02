def add(a, b):
    """回傳兩個數值的和。"""
    return a + b


def divide(a, b):
    """回傳商；依教材的例外測試約定，除數為零時拋出 ValueError。"""
    if b == 0:
        raise ValueError("divisor must not be zero")
    return a / b
