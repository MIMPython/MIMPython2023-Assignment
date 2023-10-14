from PIL import Image
image_of_asg = Image.open('C:\module06_student07_TranHaiNam\Additional folder\SD_Mooncake.png')
width, height = image_of_asg.size

#Chia ảnh ra làm 4 phần theo như đề bài
img1 = image_of_asg.crop((0, 0, width/2, height/2)) #lef,top,right,bottom
img2 = image_of_asg.crop((width/2,0,width,height/2))
img3 = image_of_asg.crop((0,width/2,height/2,height))
img4 = image_of_asg.crop((width/2,height/2,width,height))

#Chỉnh vị trí phù hợp cho từng ảnh
new_img = Image.new('RGB',(width,height)) #tạo một ảnh 'rỗng' tương ứng với thông số ảnh đã cho.
new_img.paste(img2,(0, 0)) #left,top
new_img.paste(img4,(img4.width,0))
new_img.paste(img1,(0,img1.height))
new_img.paste(img3,(img3.width,img3.height))
new_img.show()
#new_img.save('Assignment04.png')