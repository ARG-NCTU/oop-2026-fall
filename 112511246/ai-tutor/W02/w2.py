def group_by_grade(grades):
    new_grades = {}
    for i in grades:
        if grades[i] in new_grades:
            new_grades[grades[i]].append(i)
        else:
            new_grades[grades[i]] = [i]
    for j in new_grades:
        new_grades[j].sort()
    return new_grades


if __name__ == "__main__":
    grades = {'Ana': 'B', 'John': 'A', 'Kyle': 'A'}
    print(group_by_grade(grades))
    print(grades)

    print(group_by_grade({'Zoe': 'C', 'Amy': 'C', 'Max': 'C'}))
    print(group_by_grade({}))
