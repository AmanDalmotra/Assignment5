student_details = {
    "John": 81.5,
    "Doe": 92.4,
    "Alice": 87.6
}

Student_name = input("Enter student's name : ")
Student_name = Student_name.title()

if Student_name in student_details:
    print(f"{Student_name} marks: {student_details[Student_name]}")

else:
    print("Student not found")