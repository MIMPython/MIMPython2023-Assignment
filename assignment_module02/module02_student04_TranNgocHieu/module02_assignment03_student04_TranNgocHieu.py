def make_file_name(student_name, student_index, week_index,
                    assignment_index):
    # Tạo tên file từ các đầu vào Tên học viên (kiểu string), id học 
    # viên (kiểu số), số thứ tự tuần học (kiểu số), số thứ tự bài tập 
    # (kiểu số).

    string_stud_id = str(student_index)
    string_week_id = str(week_index)
    string_asg_id = str(assignment_index)

    if student_index < 10:
        string_stud_id = '0' + string_stud_id
    if week_index < 10:
        string_week_id = '0' + string_week_id
    if assignment_index < 10:
        string_asg_id = '0' + string_asg_id

    file_name = (
        f"Week{string_week_id}" 
        f"_Assignment{string_asg_id}" 
        f"_Student{string_stud_id}" 
        f"_{student_name}.py"
    )
    return file_name

print(make_file_name('NguyenVanA', 7, 2, 1))
# Week02_Assignment01_Student07_NguyenVanA.py