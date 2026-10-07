# W1 AI Tutor Part B: convert seconds to hours, minutes, seconds
# Uses only Lecture 1 concepts: variables, arithmetic operators, int(), print

total_seconds = 3725

hours = int(total_seconds / 3600)          # / always gives a float, int() truncates it
remaining = total_seconds - hours * 3600   # seconds left after removing whole hours
minutes = int(remaining / 60)
seconds = remaining - minutes * 60

print(hours, minutes, seconds)
