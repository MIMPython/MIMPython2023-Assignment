"""
Bài tập 1
a) 
- Tên biến chỉ gồm các ký tự chữ và số, không được dùng ký tự đặc biệt
(trừ dấu gạch dưới "_"), không dùng ký tự trắng (dấu cách). Ngoài ra, 
tên biến không thể bắt đầu bằng ký tự số.
- Theo PEP8, các ký tự "l" (chữ "L" viết thường), "O" (chữ "o" viết 
hoa) và "I" (chữ "i" viết hoa) không bao giờ được dùng cho các biến
chỉ gồm một ký tự, vì trong một số phông chữ, các ký tự này không thể 
phân biệt được với "số 0" và "số 1".

b) 
- Ví dụ về tên biến đúng: a, var_name, foo123, v.v.
- Ví dụ về tên biến sai: 1a, var-name, foo 123, v.v.

c) 
Ví dụ: Khi tìm hiểu thông tin về một bộ phim, ta có thể sử dụng những
biến với ý nghĩa sau:
- movie_name    # Tên bộ phim
- main_actors    # Các diễn viên chính

d) Các kiểu đặt tên biến:
- numberofcollegestudents: lowercase - các ký tự in thường, liền nhau.
- NUMBEROFCOLLEGESTUDENTS: UPPERCASE - các ký tự in hoa, liền nhau.
- numberOfCollegeStudents: mixedCase - in hoa chữ cái đầu của mỗi từ, 
trừ từ thứ nhất; các ký tự liền nhau.
- NumberOfCollegeStudents: CapWords (hoặc CamelCase) - in hoa chữ cái 
đầu của mỗi từ, kể cả từ thứ nhất; các ký tự liền nhau.
- number_of_college_students: lower_case_with_underscores -  các ký tự 
in thường; các từ ngăn cách nhau bởi dấu gạch dưới.

Nguồn: PEP 8 - https://peps.python.org/pep-0008/#descriptive-naming-styles

e) 
- Theo PEP 8, Camel Case là kiểu in hoa chữ cái đầu của mỗi từ, kể cả
từ thứ nhất, với các ký tự liền nhau. Nó cũng được gọi là kiểu CapWords
(viết tắt của Capitalized Words). 
- Tuy nhiên, theo tham khảo từ những nguồn khác, Camel Case lại được
dùng cho kiểu in hoa chữ cái đầu của mỗi từ, ngoại trừ từ thứ nhất, với
các ký tự liền nhau (ứng với tên gọi Mixed Case ở trên). Để phân biệt 
chúng, ta có thể gọi tên cụ thể hơn: dạng đầu tiên lấy tên Upper Camel
Case, và dạng thứ hai là Lower Camel Case.
- Vẫn ở ngoài phạm vi PEP 8, Pascal Case ứng với dạng CapWords (hay 
Upper Camel Case), và Snake Case ứng với dạng Lower Case With 
Underscores.

Thêm ví dụ: Điểm trung bình
- Camel Case (hiểu theo nghĩa Lower Camel Case): gradePointAverage
- Pascal Case: GradePointAverage
- Snake Case: grade_point_average

Nguồn tham khảo:
https://khalilstemmler.com/blogs/camel-case-snake-case-pascal-case/
https://en.wikipedia.org/wiki/Camel_case

f) Hiện tại, em thường sử dụng kiểu Snake Case.
"""



