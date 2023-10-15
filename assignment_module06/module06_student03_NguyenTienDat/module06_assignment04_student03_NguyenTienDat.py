from PIL import Image
import numpy as np

def image():
    input_image = Image.open("D:/Optima_Lab/Python/assignment_module06/module06_student03_NguyenTienDat/additionalFolder/SD_mooncake.png") # size = (505,498)
    
    # Kích thước mới của từng phần ảnh
    new_size = (252, 249)
    
    # Cắt ảnh thành 4 phần bằng nhau
    image_1 = input_image.crop((0, 0, new_size[0], new_size[1]))
    image_2 = input_image.crop((0, new_size[1], new_size[0], 2 * new_size[1]))
    image_3 = input_image.crop((new_size[0], 0, 2 * new_size[0], new_size[1]))
    image_4 = input_image.crop((new_size[0], new_size[1], 2 * new_size[0], 2 * new_size[1]))
    
    # Lưu các phần ảnh
    image_1.save("D:/Optima_Lab/Python/assignment_module06/module06_student03_NguyenTienDat/additionalFolder/SD_mooncake_1.png")
    image_2.save("D:/Optima_Lab/Python/assignment_module06/module06_student03_NguyenTienDat/additionalFolder/SD_mooncake_2.png")
    image_3.save("D:/Optima_Lab/Python/assignment_module06/module06_student03_NguyenTienDat/additionalFolder/SD_mooncake_3.png")
    image_4.save("D:/Optima_Lab/Python/assignment_module06/module06_student03_NguyenTienDat/additionalFolder/SD_mooncake_4.png")
    
    img1 = np.array(image_1)
    img2 = np.array(image_2)
    img3 = np.array(image_3)
    img4 = np.array(image_4)
    
    row_1 = np.hstack((img3, img4))
    row_2 = np.hstack((img1, img2))
    result = np.vstack((row_1, row_2))
    final_result = Image.fromarray(result)
    final_result.save("D:/Optima_Lab/Python/assignment_module06/module06_student03_NguyenTienDat/additionalFolder/SD_mooncake_result.png")
    final_result.show()  

print(image())
