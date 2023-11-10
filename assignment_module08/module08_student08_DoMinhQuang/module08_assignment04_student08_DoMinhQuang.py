import pandas as pd

data = pd.read_csv('additionalFolder/data.csv')
cls_list = list(data['class'].value_counts().index)  #data['class'].value_counts() sẽ cho ta các level của cột [class], thêm .index(như ta đã biết trong pd.Series)
# df_k64 = df.loc[df['class'] == 'K64']              #và ép kiểu thành list, ta lấy ra được các level của cột [class], cụ thể ở đây list là [K66,K64,K67,K65]
# print(df_k64)
def data_classify(data, cls: str):
    '''This method is used to return a dataframe of a specified class

        Parameter
        ---------

        data: DataFrame
                a dataframe of students of HUS
        cls: str
                class, example: K67, K66,...


        Return
        ------

        result: DataFrame


        Exception
        ---------

        Raise exception if the parameter cls is not included in the cls_list, which contains every single class of the DataFrame
        '''

    try:
        if cls not in cls_list:
            raise Exception('Dataframe does not contain this class!')
    except Exception as error:
        print(error)
    else:
        class_df = data.loc[data['class'] == cls]   #lấy ra các hàng có giá trị tại cột [class] là cls
        num_of_students = class_df.shape[0] #lấy ra số hàng của dataframe ở trên
        mean_score = class_df['scores'].mean()  #tính giá trị trung bình của cột [scores]
        new_df = pd.DataFrame({'class': [cls], 'nStudents': [num_of_students], 'meanScores': [mean_score]})
        return new_df


df_K64 = data_classify(data, 'K64')
df_K65 = data_classify(data, 'K65')
df_K66 = data_classify(data, 'K66')
df_K67 = data_classify(data, 'K67')
total_df = pd.concat([df_K64, df_K65, df_K66, df_K67])

print(data)
print(total_df)











