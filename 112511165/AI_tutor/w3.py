def parse_numbers(tokens):
    total = 0
    bad_tokens = []

    for token in tokens:
        if not isinstance(token, str):
            raise TypeError("token must be str")

        try:
            total += int(token)
        except ValueError:
            bad_tokens.append(token)

    return (total, bad_tokens)
