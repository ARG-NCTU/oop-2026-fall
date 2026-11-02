def greedy_inspections(jobs, budget):
    """Select jobs by descending value/time, preserving input order on ties."""
    ranked = sorted(range(len(jobs)), key=lambda i: jobs[i][1] / jobs[i][0],
                    reverse=True)
    chosen = []
    used = total = 0
    for index in ranked:
        duration, value = jobs[index]
        if used + duration <= budget:
            chosen.append(index)
            used += duration
            total += value
    return chosen, total
