def sort_student_scores(scores, threshold):
    # Step 1: Sort scores in descending order using Selection Sort
    suffixSt = 0

    while suffixSt != len(scores):
        # Find the maximum score in the unsorted portion
        for i in range(suffixSt, len(scores)):
            if scores[i] > scores[suffixSt]:
                scores[suffixSt], scores[i] = scores[i], scores[suffixSt]

        suffixSt += 1

    # Step 2: Count the number of students who passed
    passed = 0

    for score in scores:
        if score >= threshold:
            passed += 1

    # Step 3: Return the sorted scores and the number of students who passed
    return (scores, passed)


# Example 1
scores = [65, 90, 75, 90, 40]
threshold = 70
print(sort_student_scores(scores, threshold))
# Expected output: ([90, 90, 75, 65, 40], 3)

# Example 2
scores = [50, 30, 20, 10]
threshold = 60
print(sort_student_scores(scores, threshold))
# Expected output: ([50, 30, 20, 10], 0)

# Example 3
scores = [100, 100, 80, 80, 60]
threshold = 80
print(sort_student_scores(scores, threshold))
# Expected output: ([100, 100, 80, 80, 60], 4)

# Edge case
scores = [100]
threshold = 100
print(sort_student_scores(scores, threshold))
# Expected output: ([100], 1)
