# name scores 
with open('additionalFolder/module03_assignment03_student06_NguyenThiMen_names.txt','r') as file:
    data = file.read() # read data from a file, return string 
    names = data.replace('"','').split(',') # return list string 
sorted_name = sorted(names)
alpha_list = {}
for value in range(1, 27):
    key = chr(value + 64)
    alpha_list[key] = value 
# print(alpha_list) A is assigned 1, Z:26

def get_score_by_name(name):
    sum = 0
    for i in name:
        sum = sum + alpha_list[i]
    return sum

total_sum = 0
for i in range(len(sorted_name)):
    name = sorted_name[i]
    total_sum += (i+1)*(get_score_by_name(name))
print(total_sum)
