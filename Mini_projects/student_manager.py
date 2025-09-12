import csv
import os

CSV_FILE = "data/students.csv"

# ----------------------
# Student Class
# ----------------------
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = int(age)
        self.grade = grade.upper()  # Ensure grade is uppercase

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def update_grade(self, new_grade):
        self.grade = new_grade.upper()
        print(f"Updated {self.name}'s grade to {self.grade}")

# ----------------------
# CSV Functions
# ----------------------
def load_students():
    """Load students from CSV and return a list of Student objects."""
    students = []
    if not os.path.exists(CSV_FILE):
        print("⚠️ students.csv not found. Starting with empty list.")
        return students

    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(row["Name"], row["Age"], row["Grade"])
                students.append(student)
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
    return students

def save_students(students, filename=CSV_FILE):
    """Save Student objects to CSV."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "Grade"])
            for s in students:
                writer.writerow([s.name, s.age, s.grade])
        print(f"Students saved to {filename}")
    except Exception as e:
        print(f"Error saving CSV: {e}")

# ----------------------
# Utility Functions
# ----------------------
def show_students(students):
    if not students:
        print("No students found.")
        return
    print("\n--- Student List ---")
    for idx, s in enumerate(students, start=1):
        print(f"{idx}. Name: {s.name}, Age: {s.age}, Grade: {s.grade}")
    print("-------------------\n")

def filter_top_students(students):
    top = [s for s in students if s.grade in ("A", "B")]
    return top

# ----------------------
# Main Program
# ----------------------
def main():
    students = load_students()

    while True:
        print("\n--- Student Manager ---")
        print("1. Show all students")
        print("2. Update student grade")
        print("3. Filter top students (A/B) and save")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            show_students(students)
        elif choice == "2":
            show_students(students)
            try:
                idx = int(input("Enter student number to update grade: "))
                if 1 <= idx <= len(students):
                    new_grade = input("Enter new grade (A/B/C/D/F): ").upper()
                    students[idx - 1].update_grade(new_grade)
                    save_students(students)
                else:
                    print("Invalid student number!")
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "3":
            top_students = filter_top_students(students)
            save_students(top_students, filename="data/top_students.csv")
            print(f" Top students saved to data/top_students.csv")
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
