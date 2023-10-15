'''Bài 4: cắt ảnh để thu được ảnh đúng'''

'''Em không tìm được cách nào ngoài cách này và cách sử dụng thư viện cv2'''

from PIL import Image

img = Image.open('additionalFolder/SD_mooncake.png')
print(img.size)

new_img = img.resize((500, 500))#do ảnh có chiều dài là số lẻ nên em resize lại để dễ chia cắt
new_img.save('additionalFolder/newSDMooncake.png')

img = Image.open('additionalFolder/newSDMooncake.png')
print(img.size)

#crop ảnh
An = img.crop((0,0,250,250))
Banh = img.crop((250, 0, 500, 250))
Kieng = img.crop((0, 250, 250, 500 ))
TrungThu = img.crop((250, 250, 500, 500))

#ghép cách ảnh vừa cắt
edited_img = Image.new('RGB', (500, 500))
edited_img.paste(Banh, (0, 0))
edited_img.paste(TrungThu, (250, 0))
edited_img.paste(An, (0, 250))
edited_img.paste(Kieng, (250, 250))
print(edited_img.size)
edited_img.show()



