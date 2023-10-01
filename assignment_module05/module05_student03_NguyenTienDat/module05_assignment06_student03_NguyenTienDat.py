import sys

def infor_student(studentName, studentIndex, weekIndex, assignmentIndex):
    print("Student Name:", studentName)
    print("Student Index:", studentIndex)
    print("Week Index:", weekIndex)
    print("Assignment Index:", assignmentIndex)
infor_student(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

