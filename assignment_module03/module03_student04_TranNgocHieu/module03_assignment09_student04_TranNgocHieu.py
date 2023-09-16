"""
Hình ảnh mô tả cách hoạt động của hai lệnh - "while" và "do...while"
trong C++. 
- Lệnh "while" sẽ kiểm tra điều kiện trước tiên, sau đó thực hiện các
câu lệnh bên trong nếu điều kiện được thoả mãn. Quá trình này được lặp
đi lặp lại.
- Lệnh "do...while" sẽ thực hiện các câu lệnh bên trong trước một lần,
sau đó lại hoạt động như lệnh "while".
Vì vậy, trong meme, lệnh "while" của roadrunner sẽ kiểm tra điều kiện
"not edge" ("không phải rìa núi") trước tiên. Điều kiện này không thoả
mãn, vì roadrunner đang ở rìa núi, nên câu lệnh "run" ("chạy") không
được thực hiện. Mặt khác, lệnh "do...while" của coyote yêu cầu thực hiện
lệnh "run" trước một lần, bất kể điều kiện, sau đó mới bắt đầu vào vòng
lặp "while" với điều kiện "not edge".
"""