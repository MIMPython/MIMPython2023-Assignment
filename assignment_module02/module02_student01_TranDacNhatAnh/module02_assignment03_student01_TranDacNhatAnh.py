#Gọi hàm
def filename(studentName: str, studentIndex: int, weekIndex: int, assignmentIndex: int): 
    return f"week{weekIndex:02d}_assignment{assignmentIndex:02d}_student{studentIndex:02d}_{studentName}.py"

#test
studentName = "TranDacNhatAnh" 
studentIndex = 1 
weekIndex = 2
assignmentIndex = 3

print(filename(studentName, studentIndex, weekIndex, assignmentIndex)) #week02_assignment03_student01_TranDacNhatAnh.py