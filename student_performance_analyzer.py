
"""
STUDENT PERFORMANCE ANALYZER
Created by: Priyanka Pradhan
Project: Python Beginner Portfolio
"""

def calculate_average(marks):
    return sum(marks) / len(marks)


def get_grade(average):
    if average >= 90:
        return "A+ - Excellent"
    elif average >= 80:
        return "A - Very Good"
    elif average >= 70:
        return "B - Good"
    elif average >= 60:
        return "C - Satisfactory"
    elif average >= 40:
        return "D - Needs Improvement"
    return "F - Keep Practising"


def main():
    print("=" * 45)
    print("       STUDENT PERFORMANCE ANALYZER")
    print("=" * 45)

    name = input("\nEnter student name: ")

    subjects = ["Python", "SQL", "Data Science", "HTML"]
    marks = []

    for subject in subjects:
        while True:
            try:
                score = float(input(f"Enter {subject} marks (0-100): "))
                if 0 <= score <= 100:
                    marks.append(score)
                    break
                print("Please enter marks between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    average = calculate_average(marks)
    grade = get_grade(average)

    print("\n" + "=" * 45)
    print("             PERFORMANCE REPORT")
    print("=" * 45)

    print(f"\nStudent Name : {name}")

    for subject, score in zip(subjects, marks):
        print(f"{subject:<18}: {score:>6.1f}/100")

    print("-" * 45)
    print(f"Average      : {average:.2f}%")
    print(f"Highest      : {max(marks):.1f}")
    print(f"Lowest       : {min(marks):.1f}")
    print(f"Grade        : {grade}")
    print("=" * 45)

    print("\nThank you for using the analyzer!")


if __name__ == "__main__":
    main()
