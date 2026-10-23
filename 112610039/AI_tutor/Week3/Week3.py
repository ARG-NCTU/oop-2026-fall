def process_student_grades(class_data, min_passing_avg):

    if not isinstance(class_data, list):
        raise TypeError("Invalid class_data format")
    passed_student = []

    for student_data in class_data:

        name = student_data[0]
        grades = student_data[1]
        total = 0
        for grade in grades:
            total += grade        
        
        try:
            avg = total / len(grades)
        except ZeroDivisionError:
            avg = 0
            print(f"student {name} has no grades")

        assert 0.0 <= avg <= 100.0, "calculated average out of range"
        
        if avg >= min_passing_avg:
            passed_student.append(name)

    return passed_student



def main():
    class_data = data = [
    ["Alice", [80, 90, 100]],
    ["Bob", []],            
    ["Charlie", [60, 70]]
    ]
    min_passing_avg = 60
    passed_students = process_student_grades(class_data, min_passing_avg)
    print(passed_students)

if __name__ == "__main__":
    main()