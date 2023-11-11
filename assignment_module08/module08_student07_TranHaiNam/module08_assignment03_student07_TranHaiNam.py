import pandas as pd

path = f'C:\\Users\\TUF\\Downloads\\data.xlsx'
df = pd.read_excel(path)
class_student = ['K67','K68','K65','K66','K64']
list_scores = []
for i in class_student:
     list_scores.append(df.loc[df['Class'] == i]['Score'].mean())
     
nk67 = 0
nk68 = 0
nk65 = 0
nk66 = 0
nk64 = 0

for i in range(len(df)):
    if df['Class'].iloc[i] == 'K67':
        nk67 += 1
    elif df['Class'].iloc[i] == 'K68':
        nk68 += 1
    elif df['Class'].iloc[i] == 'K65':
        nk65 += 1
    elif df['Class'].iloc[i] == 'K66':
        nk66 += 1
    else:
        nk64 += 1
nstudent = [nk67,nk68,nk65,nk66,nk64]
    
new_df = pd.DataFrame({'class':['K67','K68','K65','K66','K64'],
                       'nStudents': nstudent,
                       'meanScore': list_scores
                       })
print(new_df)
