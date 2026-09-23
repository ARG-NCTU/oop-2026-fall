def score_summary(scores):
    min_score = min(scores)
    max_score = max(scores)
    unique_scores = []
    for score in scores:
        if score not in unique_scores:
            unique_scores.append(score)
    ans = (min_score, max_score, unique_scores)
    return ans