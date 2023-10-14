import os

def iterating(path):
    list = []
    for directory_or_files in os.listdir(path):
        isfile_True = os.path.isfile('module05_student07_TranHaiNam\{directory_or_files}')
        if isfile_True == True:
            list.append(f'{directory_or_files}: type files')
        elif isfile_True == False:
            list.append(f'{directory_or_files}: type folder')
    return list
        
    
path = 'C:\module05_student07_TranHaiNam'
for i in iterating(path):
    print(i)

"web tham khảo: https://www.geeksforgeeks.org/os-module-python-examples/ "