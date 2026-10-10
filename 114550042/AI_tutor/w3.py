type value = int | float | str


def safe_batch_evaluate(expressions: list[tuple[str, value, value]]):
    results = []
    success_count = 0

    for op, raw_a, raw_b in expressions:
        # because unsupported operator will raise ValueError too, we need to catch ValueError of InvalidOperand here
        try:
            a = float(raw_a)
            b = float(raw_b)
        except ValueError:
            results.append((None, "InvalidOperand"))
            continue

        try:
            result = None
            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                result = a / b
            else:
                raise ValueError(f"Unsupported operator: {op}")
            results.append((result, "Success"))
            success_count += 1
        except ValueError:
            results.append((None, "UnsupportedOperator"))
        except ZeroDivisionError:
            results.append((None, "DivisionByZero"))
        except Exception as e:
            results.append((None, f"Error: {e}"))

    error_count = len(results) - success_count

    return {
        "success_count": success_count,
        "error_count": error_count,
        "results": results,
    }
