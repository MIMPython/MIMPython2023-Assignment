# Bài tập 4:
from PIL import Image
# 1. Cắt ảnh 
# Đọc ảnh gốc 
img = Image.open("SD_mooncake.png")
# Kích thước ảnh gốc
width, height = img.size
# Tính toán kích thước của mỗi phần cắt
middle_x = width // 2
middle_y = height // 2
# Cắt ảnh thành 4 phần
top_left = img.crop((0, 0, middle_x, middle_y))
top_right = img.crop((middle_x, 0, width, middle_y))
bottom_left = img.crop((0, middle_y, middle_x, height))
bottom_right = img.crop((middle_x, middle_y, width, height))

# 2. Ghép lại
# Kích thước của các phần đã cắt
width, height = top_left.size
# Tạo ảnh mới có kích thước gấp đôi chiều rộng và cao của các phần đã cắt
new_width = width * 2
new_height = height * 2
result_image = Image.new("RGB", (new_width, new_height))
# Paste từng phần vào ảnh mới
result_image.paste(top_right, (0, 0))
result_image.paste(bottom_right, (width, 0))
result_image.paste(top_left, (0, height))
result_image.paste(bottom_left, (width, height))
# Lưu 
result_image.save("Banhtrungthuankieng.png")
result_image.show()