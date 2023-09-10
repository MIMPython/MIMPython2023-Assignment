#Bài tập 3:(names scores)
def calculate_name_score(name, position):
# Tính giá trị của một tên dựa trên thứ tự chữ cái và vị trí của nó
    score = sum(ord(char) - ord('A') + 1 for char in name)
    return score * position

# Đọc nội dung từ tệp văn bản
path = 'names.txt'
with open(path, 'r') as file:
    names = file.read().replace('"', '').split(',')

# Sắp xếp danh sách tên theo thứ tự bảng chữ cái
names.sort()

# Tính tổng điểm của tất cả các tên
total_score = 0
for position, name in enumerate(names, start=1):
    name_score = calculate_name_score(name, position)
    total_score += name_score

print("Tổng điểm của tất cả các tên là:", total_score) #Tổng điểm của tất cả các tên là: 871198282
