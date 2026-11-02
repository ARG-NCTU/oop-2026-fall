def letter_grade(score):
    """將 0～100 的數值分數轉為 A、B、C、D 或 F。"""
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")

    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def average(scores):
    """回傳非空數值 list 的算術平均；空 list 時拋出 ValueError。"""
    if not scores:
        raise ValueError("scores must not be empty")
    return sum(scores) / len(scores)
