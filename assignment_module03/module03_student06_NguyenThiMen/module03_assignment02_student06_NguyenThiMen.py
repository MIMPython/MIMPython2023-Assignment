# large sum
with open('additionalFolder/module03_assignment02_student06_NguyenThiMen_data.txt', 'r') as data:
    lines = data.readlines() # .readlines() returns a list of lines in the file
# use with open(file_name, 'mode') as alias to ensure the file closes automatically. 
line_sum = 0 
for line in lines:
    line_sum += int(line.strip())
result = str(line_sum)[0:10]
print(result) #5537376230
