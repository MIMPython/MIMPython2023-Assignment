'''Bài 6: Làm lại bài 3 module02 với các truyền tham số qua dòng lệnh'''

import sys
def info(studentName: str,studentIndex: str,weekIndex: str,assignmentIndex: str) -> None:
    # file_name = f"week{weekIndex:02}_assignment{assignmentIndex:02}_student{studentIndex:02}_{studentName}.py" #khi dùng cú phaáp này và chạy trong Terminal thi số 0 sẽ bị đảo về sau
    #week80_assignment60_student80_DoMinhQuang.py

    file_name: str = f"week0{weekIndex}_assignment0{assignmentIndex}_student0{studentIndex}_{studentName}.py"
    print(file_name)

studentName = sys.argv[1]
studentIndex = sys.argv[2]
weekIndex = sys.argv[3]
assignmentIndex = sys.argv[4]

# studentName = 'DoMinhQuang'
# weekIndex = 5
# studentIndex = 8
# assignmentIndex = 6

info(studentName, studentIndex, weekIndex, assignmentIndex) #week08_assignment06_student08_DoMinhQuang.py

#Chạy code :python  module05_assignment06_student08_DoMinhQuang.py DoMinhQuang 8 5 6



import argparse


def info(studentName: str,studentIndex: str,weekIndex: str,assignmentIndex: str) -> None:
    # file_name = f"week{weekIndex:02}_assignment{assignmentIndex:02}_student{studentIndex:02}_{studentName}.py" #khi dùng cú phaáp này và chạy trong Terminal thi số 0 sẽ bị đảo về sau
    #week80_assignment60_student80_DoMinhQuang.py

    file_name: str = f"week0{weekIndex}_assignment0{assignmentIndex}_student0{studentIndex}_{studentName}.py"
    print(file_name)

parser = argparse.ArgumentParser(description = 'Chương trình yêu cầu nhập thông tin cá nhân của học viên')

parser.add_argument('studentName', type = str, help = 'Nhập tên học viên')
parser.add_argument('studentIndex', type = int, help = 'Nhập mã học viên')
parser.add_argument('weekIndex', type = int, help = 'Nhập tuần học')
parser.add_argument('assignmentIndex', type = int, help = 'Nhập số bài tập')

args = parser.parse_args()
studentName = args.studentName
studentIndex = args.studentIndex
weekIndex = args.weekIndex
assignmentIndex = args.assignmentIndex

info(studentName, studentIndex , weekIndex , assignmentIndex)

#Xem hướng dẫn truyền tham số : python  module05_assignment06_student08_DoMinhQuang.py DoMinhQuang --help
#Chạy code :python  module05_assignment06_student08_DoMinhQuang.py DoMinhQuang 8 5 6
