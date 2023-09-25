def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Define the Student class
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Example usage:
# Create some student objects
student1 = Student("Alice", "A123", 3.9)
student2 = Student("Bob", "B456", 3.7)
student3 = Student("Charlie", "C789", 4.0)

# Put them in a list
student_list = [student1, student2, student3]

# Sort the students by CGPA in descending order
sorted_students = sort_students(student_list)

# Print the sorted list
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")