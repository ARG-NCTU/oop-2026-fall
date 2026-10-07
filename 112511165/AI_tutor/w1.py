def clean_scores(records, low):
    original_len = len(records)

    for i in range(original_len - 1, -1, -1):
        if records[i][1] < low:
            del records[i]

    removed_count = original_len - len(records)

    if not records:
        min_remaining = None
    else:
        min_remaining = min(score for name, score in records)

    return (removed_count, min_remaining)
