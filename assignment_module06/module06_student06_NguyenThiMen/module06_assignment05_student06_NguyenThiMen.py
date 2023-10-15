import os


def list_files_and_folders(path):
    '''
     liệt kê tất cả tệp tin và thư mục con của một thư mục cho trước
     mỗi đối tượng là tệp tin hay thư mục?
    '''
    if os.path.exists(path):
        if os.path.isdir(path):
            for item in os.listdir(path):
                item_path = path + '\\' + item
                if os.path.isfile(item_path):
                    print(f'object {item}, type file')
                elif os.path.isdir(item_path):
                    print(f'object {item}, type folder')
        else:
            print(f'The {path} is not a directory')
    else:
        print(f'The {path} doesn\'t exist')


path = r'C:\Users\Men\StudioCode\VSC\Python\module04_student06_NguyenThiMen'
list_files_and_folders(path)
# kết quả chạy
'''
object .vscode, type folder
object additionalFolder, type folder
object module04_assignment01_student06_NguyenThiMen.py, type file
object module04_assignment02_student06_NguyenThiMen.py, type file
object module04_assignment03_student06_NguyenThiMen.py, type file
object module04_assignment04_student06_NguyenThiMen.py, type file
object module04_assignment05_student06_NguyenThiMen.py, type file
object module04_assignment08_student06_NguyenThiMen.py, type file
object test.py, type file
'''
