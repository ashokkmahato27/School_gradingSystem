
# School Grading System - Essential Version

def get_marks():
    subjects = ["Mathematics", "Science", "English", "Health", "Computer"]    # Getting Marks of 5 subjects
    marks = {}
    
    print("\nEnter marks (0-100):")
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"{subject}: "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Enter marks between 0-100")
            except ValueError:
                print("Enter a valid number")
    
    return marks


def calculate_total_percentage(marks):
    total = sum(marks.values())
    percentage = (total / 500) * 100
    return total, percentage


def determine_grade(percentage):
    if percentage >= 60:
        if percentage >= 80:
            if percentage >= 90:
                return 'A'
            else:
                return 'B'
        else:
            if percentage >= 70:
                return 'C'
            else:
                return 'D'
    else:
        return 'F'


def save_report(name, roll_no, marks, total, percentage, grade, distinction):
    #....Save report to .txt file
    filename = f"Report_{roll_no}.txt"
    
    with open(filename, 'w') as file:
        file.write("=" * 40 + "\n")
        file.write(" STUDENT REPORT CARD\n")
        file.write("=" * 40 + "\n\n")
        file.write(f"Name: {name}\n")
        file.write(f"Roll No: {roll_no}\n\n")
        file.write("-" * 40 + "\n")
        file.write("SUBJECT              MARKS\n")
        file.write("-" * 40 + "\n")
        
        for subject, mark in marks.items():
            file.write(f"{subject:<20} {mark:.1f}\n")
        
        file.write("-" * 40 + "\n")
        file.write(f"Total: {total:.1f}/500\n")
        file.write(f"Percentage: {percentage:.2f}%\n")
        file.write(f"Grade: {grade}\n")
        file.write(f"Distinction: {'Yes' if distinction else 'No'}\n")
        file.write("=" * 40 + "\n")
    
    return filename


def main():
    print("\n=== SCHOOL GRADING SYSTEM ===")
    
    # Get input
    name = input("\nStudent Name: ")
    roll_no = input("Roll Number: ")
    marks = get_marks()
    
    # Calculate results
    total, percentage = calculate_total_percentage(marks)
    grade = determine_grade(percentage)
    
    # Display results
    print("\n" + "=" * 40)
    print("RESULTS")
    print("=" * 40)
    print(f"Total: {total:.1f}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    
    # Save to file
    filename = save_report(name, roll_no, marks, total, percentage, grade)
    print(f"\nReport saved to: {filename}")


if __name__ == "__main__":
    main()