import sys
def createFile(studentName: str, studentIndex: int, weekIndex: int, assignmentIndex:int):
    filename = f'week{weekIndex:02d}_assignment{assignmentIndex:02d}_student{studentIndex:02d}_{studentName}.py'
    with open(filename, 'w') as file:
        True
    return None
createFile(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
# Tùy thuộc vào input, dòng lệnh trên sẽ tạo ra một file mới có tên week{ww}_assignment{aa}_student{ss}_{studentName}.py
