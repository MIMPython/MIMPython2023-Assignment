# Tạo hàm tính điểm trung bình môn
def universityScoring(thuongXuyen, giuaKy, cuoiKy):
    score = thuongXuyen/5 +giuaKy/5 +3*cuoiKy/5
    point = [0.0, 4.0, 5.0, 5.5, 6.5, 7.0, 8.0, 8.5, 9.0, 10.1]
    letter = ['F','D','D+','C','C+','B','B+','A','A+']
    for i in range(len(point)):
        if point[i]<=score and score<point[i+1]:
            return letter[i]
# Test
print(universityScoring(10, 10, 2)) #D+