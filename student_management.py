import json
import os

FILE_NAME = "students.json"

def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student(students):
    student_id = input("Enter student ID: ").strip()

    if any(s["id"] == student_id for s in students):
        print("Student ID already exists!")
        return

    name = input("Enter student name: ").strip()
    course = input("Enter course name: ").strip()

    if not student_id or not name or not course:
        print("All fields are required!")
        return

    students.append({
        "id": student_id,
        "name": name,
        "course": course
    })

    save_students(students)
    print("Student added successfully!")

def view_students(students):
    if not students:
        print("No students found.")
        return

    print("\n--- Student List ---")
    for student in students:
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("-" * 20)

def search_student(students):
    student_id = input("Enter student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            return

    print("Student not found!")

def main():
    students = load_students()

    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
