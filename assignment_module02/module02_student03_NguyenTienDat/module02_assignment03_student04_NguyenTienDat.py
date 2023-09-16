# Bài tập 3: Viết một hàm nhận vào tên học viên (kiểu string),
# id học viên (kiểu nguyên), số thứ tự tuần học (kiểu nguyên),
# số thứ tự bài tập (kiểu nguyên) và trả về tên file .py tương ứng.

student_name = 'NguyenTienDat'
student_index = 3
week_index = 2
assignment_index = 3

def infor_student(student_name, student_index, week_index, assignment_index):
    print(f'week{week_index:02}_assignment{assignment_index:02}_student'
          f'{student_index:02}_{student_name}')

if __name__ == '__main__':
    infor_student(student_name, student_index, week_index, assignment_index)
