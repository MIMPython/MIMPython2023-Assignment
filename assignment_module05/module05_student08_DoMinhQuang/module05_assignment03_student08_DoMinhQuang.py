'''Bài 3: Thực hiện các yêu cầu về việc tạo thư mục, tạo file, sao chép, di chuyển, xóa file

cd Documents
cd Bai3                                 chuyển đường dẫn đến thư muục Bai3
cd foo                                  chuyển đường dẫn đến thư mục foo
code data.txt                           tạo một thư mục data.txt và viết bằng VSCode
copy data.txt newData.txt               copy file data.txt thành newData.txt
copy data.txt newData_2.txt             copy file data.txt thành newData_2.txt
cd ..                                   chuyển vị trí về thư mục cha, ở đây là thư mục Bai3
mkdir bar                               tạo thư mục bar
move foo/newData.txt bar/newData.txt    chuyển file newData.txt từ thư mục foo sang thư mục bar( em bị lẫn dấu \ với dấu /)
move foo\newData.txt bar\newData.txt    chuyển file newData.txt từ thư mục foo sang thư mục bar
del foo\newData_2.txt                   xóa file newData_2 ở thư mục foo


echo Hello World! > tryecho.txt         Còn một cách khác để tạo file đuôi .txt bằng cú pháp
                                        echo <content> > <filename>.txt
                                        Do vị trí hiện tại đang ở thư mục Bai3 nên ta sẽ thấy file này ở trong thư mục Bai3

doskey/history                          Câu lệnh để xem lịch sử các lệnh đã gõ                           '''