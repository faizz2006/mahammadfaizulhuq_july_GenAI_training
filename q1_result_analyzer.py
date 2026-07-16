# q1_result_analyzer.py

def analyze_result(name, roll, marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print("\n------ Student Result ------")
    print(f"Student Name : {name}")
    print(f"Roll Number  : {roll}")
    print(f"Marks        : {marks}")
    print(f"Total Marks  : {total}")
    print(f"Average      : {average:.2f}")
    print(f"Grade        : {grade}")

    print("\nSubjects Below 40:")
    found = False
    for i in range(len(marks)):
        if marks[i] < 40:
            print(f"Subject {i+1} : {marks[i]}")
            found = True

    if not found:
        print("None")


# Main Program
name = input("Enter Student Name: ")
roll = int(input("Enter Roll Number: "))

marks = []
print("Enter marks of 5 subjects:")
for i in range(5):
    mark = float(input(f"Subject {i+1}: "))
    marks.append(mark)

analyze_result(name, roll, marks)