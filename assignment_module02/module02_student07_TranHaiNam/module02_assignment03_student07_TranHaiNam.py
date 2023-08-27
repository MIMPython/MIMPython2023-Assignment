
a=str(input(" Tên học viên:"))
b=int(input(" id học viên:"))
c=int(input(" Số thứ tự tuần học:"))
d=int(input(" Số thứ tự bài tập:"))

def file(a,b,c,d):
    print(f"week{c}_assignment{d}_student{b}_{a}.py")
file(a,b,c,d)
    
