import pandas as pd
import random
# a)
random.seed(55)
names = ['Minh', 'An', 'Gia', 'Hoa', 'Thanh', 'Cong', 'Trung', 'Dung', 'Thai', 'Duong', 'Thong', 'Dat', 'Tai', 'Duc',
         'Manh', 'Hung', 'Bao', 'Khanh', 'Dang', 'Khoa', 'Nhan', 'Nghia', 'Quoc', 'Lap',
         'Dieu', 'Anh', 'Tram', 'Nguyet', 'Anh', 'Ngoc', 'Bich', 'Minh', 'Chau', 'Ngoc', 'Diep', 'My', 'Duyen']
classes = ['K65', 'K66', 'K67', 'K68']

# create dataframe

class_ = [random.choice(classes) for _ in range(len(names))]
scores = [random.randint(0, 10) for _ in range(len(names))]

df = pd.DataFrame({'name': names, 'class': class_ , 'score': scores})
# print(df)

# b)

nStudents = df.groupby('class').size()
# print(nStudents)
meanScore = df.groupby('class')['score'].mean()
# print(meanScore)
new_df = pd.DataFrame(
    {'class': classes, 'nStudents': nStudents, 'meanScore': meanScore})
print(new_df)
json_data = new_df.to_json(orient='records', indent=2)
json_file_path = 'additionalFolder/module08_assignment04_student06_NguyenThiMen.json'
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)
print(json_data)
