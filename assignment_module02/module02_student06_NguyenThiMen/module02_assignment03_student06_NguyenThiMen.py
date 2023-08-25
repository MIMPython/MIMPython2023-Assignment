import unidecode


def generate_file_name(moduleIndex, assignmentIndex, studentId, fullName):
    formattedName = unidecode.unidecode(fullName).replace(" ", "")
    fileName = (
        f"module{moduleIndex:02}_assignment{assignmentIndex:02}_"
        f"student{studentId:02}_{formattedName}.py"
    )
    return fileName


moduleIndex = 2
assignmentIndex = 3
studentId = 6
fullName = 'Nguyễn Thị Mến'

print(generate_file_name(moduleIndex, assignmentIndex, studentId, fullName))
