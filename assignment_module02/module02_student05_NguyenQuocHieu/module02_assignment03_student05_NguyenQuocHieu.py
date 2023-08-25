def createFileName(studentName: str, studentIndex: int, weekIndex: int, assignmentIndex: int) -> str:
    fileName = "module" + createName(weekIndex) + "_assignment" + createName(
        assignmentIndex) + "_student" + createName(studentIndex) + "_" + studentName + ".py"
    return fileName


def createName(number: int) -> str:
    if number < 10:
        return "0" + str(number)
    else:
        return str(number)


if __name__ == "__main__":
    studentName = "NguyenQuocHieu"
    studentIndex = 5
    assignmentIndex = 3
    weekIndex = 2
    print(createFileName(studentName=studentName, studentIndex=studentIndex,
          weekIndex=weekIndex, assignmentIndex=assignmentIndex))
