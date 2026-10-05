"""
Object-Oriented Programming (OOP) Notes

- A class is a blueprint for creating objects.
- An object is an instance of a class.
- __init__ is the constructor; it initializes an object.
- self refers to the current object.
- Instance attributes belong to a particular object.
- Class attributes are shared by objects of the class.
- Methods are functions defined inside a class.
"""


class College:
    # Class attribute: shared by all College objects
    college_name = "Mind Power University"

    def __init__(self, student, year, course):
        # Instance attributes: each object has its own values
        self.student = student
        self.year = year
        self.course = course

    def display_details(self):
        """Display this student's details."""
        print(f"Student: {self.student}")
        print(f"Year: {self.year}")
        print(f"Course: {self.course}")


# Create objects from the College class
student1 = College("Adil", "2024", "BBA")
student2 = College("Dev", "2023", "ECE")
student3 = College("Amit", "2025", "CSE")

# Access the class attribute
print("College:", College.college_name)

# Call a method on each object
student1.display_details()
print()

student2.display_details()
print()

student3.display_details()
