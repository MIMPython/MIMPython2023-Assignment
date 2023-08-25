"""
Bài tập 1:
(a) Những kí tự nào không được phép xuất hiện trong tên biến trong Python?
    + Tên biến phải bắt đầu bằng một chữ cái (a-z, A-Z) hoặc dấu gạch dưới (_)
    + Tên biến không thể bắt đầu bằng một con số (0-9).
    + Tên biến chỉ có thể chứa các kí tự chữ cái (a-z, A-Z), con số (0-9) và 
dấu gạch dưới (_).
    + Tên biến không được chứa các kí tự đặc biệt như !, @, #, $, %, ^, & và
    những kí tự tương tự.
    + Tên biến không được trùng với các từ khóa (keywords) đã được định nghĩa
    trong Python như "if", "else", "for", "while", v.v.
(b) Cho ví dụ về tên biến hợp lệ và ví dụ về tên biến không hợp lệ.
    + Tên biến hợp lệ:
	my_variable
	count
	result123
	data_set
    + Tên biến không hợp lệ:
	01_variable
	result(^.^)
	:))
	@if
(c) Hãy cho ví dụ về cách đặt tên biến tốt kèm theo tình huống sử dụng những
biến này.
    + Tên biến liên quan đến thông tin:
	customer_name = "Shelby"
	customer_age = 40
	customer_email = "Thomas@example.com"
    + Tên biến cho các hằng số:
	MAX_RETRY_ATTEMPTS = 3
	ERROR_CODE_NOT_FOUND = 404
(d) Hãy mô tả các phong cách đặt những tên biến trên.
    Nhận xét các tên biến trong câu hỏi:
    1. numberofcollegestudents: tên biến được đặt không phạm bất kì quy tắc
nào nhưng nó cần có các gạch nối (underscore) để dễ đọc và dễ hiểu ý nghĩa
biến hơn.
    2. NUMBEROFCOLLEGESTUDENTS: nếu tên biến này đóng vai trò là một const
thì cách đặt tên nên viết hoa như vậy, nhưng giữa các từ vẫn cần "_" để tách
biệt.
    3. numberOfCollegeStudents: cách đặt tên này không sai nhưng không được
khuyến khích. (type Camel Case)
    4. NumberOfCollegeStudents: cách đặt tên này không sai nhưng cũng không
được khuyến khích. (type Pascal Case)
    5. number_of_college_students: đây là cách đặt tên biến chuẩn nhất và
được khuyến khích để đặt tên cho một biến. (type Snake Case)
(e) Phân biệt các phong cách đặt tên biến Camel Case, Pascal Case và Snake
Case. Cho ví dụ.
    + Camel Case: viết hoa chữ đầu của mỗi từ (trừ từ đầu tiên) và không sử
dụng dấu gạch hoặc khoảng trắng.
	ví dụ: numberOfCollegeStudent, nameOfCustomer,...
    + Pascal Case: viết hoa chữ đầu của mỗi từ và không sử dụng khoảng trắng.
	ví dụ: NumberOfCollegeStudent, NameOfCustomer,...
    + Snake Case: các từ trong tên được viết thường và được nối với nhau bằng
các dấu gạch nối "_".
	ví dụ: number_of_college_students, name_of_customer,...
(f) Bạn chọn phong cách đặt tên biến nào?
    + mình thường sử dụng kiểu đặt tên Snake Case, vì nó dễ đọc và dễ viết.
"""
