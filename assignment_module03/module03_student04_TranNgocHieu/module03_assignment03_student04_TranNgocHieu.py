f = open("./additionalFolder/module03_assignment03_student04_TranNgocHieu_data.txt", "r")
name_list_quoted = f.read().split(",")
name_list = []
for i in name_list_quoted:
    i = i.replace('"', '')
    name_list.append(i)
name_list.sort()

full_score = 0
for i in range(len(name_list)):
    name_score = 0
    for letter in name_list[i]:
        name_score += ord(letter) - 64
    full_score += name_score * (i + 1)

print(full_score) # 871198282
    