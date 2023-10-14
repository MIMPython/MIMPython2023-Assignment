# Bài tập 6:
def generate_python_file(student_name, student_id, week_number, exercise_number):
    file_name = f"module{week_number:02d}_assignment{exercise_number:02d}_student{student_id:02d}_{student_name}.py"
    command_line = f"python {file_name}"
    return file_name, command_line
student_name = "TranMinhChau"
student_id = 2
week_number = 5
exercise_number = 6 
file_name, command_line = generate_python_file(student_name, student_id, week_number, exercise_number)
print(file_name)
print(command_line)

