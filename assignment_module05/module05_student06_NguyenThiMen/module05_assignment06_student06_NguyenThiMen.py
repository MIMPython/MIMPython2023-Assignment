import sys
import unidecode
import argparse


def generate_file_name(moduleIndex: int, assignmentIndex: int, studentId: int, fullName: str):
    formattedName = unidecode.unidecode(fullName).replace(' ', '')

    fileName = (f'module{moduleIndex:02}_assignment{assignmentIndex:02}_'
                f'student{studentId:02}_{formattedName}.py')
    return fileName


if __name__ == '__main__':
    print(sys.argv)
    print(sys.argv[0])
    if len(sys.argv) != 5:
        message_error = ("You need four parameters after .py.\n"
                         "First parameter is moduleIndex(int), second is assignmentIndex(int), third is studentId(int) and last parameter is studentName(str)")
        sys.exit(message_error)
    moduleIndex = int(sys.argv[1])
    assignmentIndex = int(sys.argv[2])
    studentId = int(sys.argv[3])
    fullName = sys.argv[4]
    file_name = generate_file_name(
        moduleIndex, assignmentIndex, studentId, fullName)
    print(file_name)

    # # sử dụng module argparse để xử lý đối số dòng lệnh với hướng dẫn tự tạo, cung cấp lỗi, đưa ra trợ giúp...
    # parser = argparse.ArgumentParser(description='Get file name')
    # # định nghĩa các đối số dòng lệnh
    # parser.add_argument('moduleIndex', type = int, help='moduleIndex\'s type is integer')
    # parser.add_argument('assignmentIndex', type = int, help ='assignmentIndex\'s type is integer')
    # parser.add_argument('studentId', type = int, help = 'studentId\'s type is integer')
    # parser.add_argument('fullName', type = str, help = 'fullName\'s is string which should write in \" \"' )
    # args = parser.parse_args()
    # file_name = generate_file_name(args.moduleIndex, args.assignmentIndex, args.studentId, args.fullName)
    # print(file_name)
