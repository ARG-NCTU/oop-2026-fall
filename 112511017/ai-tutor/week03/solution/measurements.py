"""New AI-assisted Lecture 7 transfer exercise prepared on 2026-10-05."""


def parse_measurements(lines):
    totals = {}
    errors = []
    for index, line in enumerate(lines):
        fields = line.split(",")
        if len(fields) != 2 or not fields[0].strip():
            errors.append((index, "format"))
            continue
        name = fields[0].strip()
        try:
            value = int(fields[1].strip())
        except ValueError:
            errors.append((index, "number"))
            continue
        if value < 0 or value > 100:
            errors.append((index, "range"))
            continue
        totals[name] = totals.get(name, 0) + value
    return totals, errors
