# Student Grade Management System

students = {}

def add_student():
    name = input("Enter student name: ")
    marks = list(map(float, input("Enter marks (space-separated): ").split()))
    students[name] = marks
    print(f"{name} added successfully!\n")

def display_students():
    if not students:
        print("No student records found.\n")
        return

    print("\nStudent Report")
    print("-" * 40)

    for name, marks in students.items():
        average = sum(marks) / len(marks)
        
        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        else:
            grade = "D"

        print(f"Name    : {name}")
        print(f"Marks   : {marks}")
        print(f"Average : {average:.2f}")
        print(f"Grade   : {grade}")
        print("-" * 40)

while True:
    print("\nStudent Grade Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.\n")