class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade   # e.g., "A", "B", "C"

    def display(self):
        print(f"Student Name: {self.name}, Grade: {self.grade}")

    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"Grade updated for {self.name} to {self.grade}")

# --- Example Usage ---
student1 = Student("Ankita", "B")
student1.display()
student1.update_grade("A")
student1.display()
