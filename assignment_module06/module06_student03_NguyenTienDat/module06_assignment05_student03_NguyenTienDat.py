# Bài tập 5:
import os

def list_files_and_folders(directory_path):
    # Tạo danh sách các đối tượng con
    objects = os.listdir(directory_path)

    for obj in objects:
        if os.path.isdir(directory_path + '\\' + obj):
            print(f"object {obj}, type folder")
        elif os.path.isfile(directory_path + '\\' + obj):
            print(f"object {obj}, type file")

if __name__ == "__main__":
    folder_path = "D:/Optima_Lab/Python/assignment_module06/module06_student03_NguyenTienDat/additionalFolder/assignment02"
    list_files_and_folders(folder_path)
    
    
    
