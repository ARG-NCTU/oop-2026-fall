# Week 2: branching and iteration; enter four integers, one per line.
days = int(input())
first_amount = int(input())
daily_increase = int(input())
target = int(input())

total = 0
first_day = 0
for day in range(1, days + 1):
    total = total + first_amount + (day - 1) * daily_increase
    if total >= target and first_day == 0:
        first_day = day

print(total, first_day)
