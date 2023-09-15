from getpass import getpass
import pickle
import re

#tạo tài khoản
def creat_account():
    account = input("Creat your account: ")
    while len(account) <= 8:
        account = input("Your acoount is unvalid, try another char: ")
    return account

#yếu tố cần có để mật khẩu mạnh
def upper_char(password):
    return re.search("[A-Z]", password) 
def number_char(password):
    return re.search("[0-9]", password) 
def lower_char(password):
    return re.search("[a-z]", password) 
def special_char(password):
    return re.search(r'[!@#$%^&*?]', password)

#kiểm tra độ mạnh mật khẩu
def strong_pass(password):
    if not upper_char(password):
        print("password must contain at least one uppercase letter")
        return False
    elif not number_char(password):
        print("password must contain at least one number")
        return False
    elif not lower_char(password):
        print("password must contain at least one lowercase letter")
    elif not special_char(password):
        print("password must contain at least special letter") 
        return False
    else:
        print("Your password is strong enough")
        return True
    return True   

#tạo mật khẩu
def creat_password():
    password = getpass("Creat your password: ")
    while len(password) <= 8:
        password = getpass("Your password is too short, try another.")
    while not strong_pass(password):
        password = getpass("Try stronger password: ")
    check_password = getpass("Verify your password: ") 
    while password != check_password:
        check_password = getpass("Try again: ")     
    return password
  
#giao diện   
def display_screen():
    print("Your account is already.")
    print("Option 1: Update information")
    print("Option 2: Deposit ")
    print("option 3: Banking ")
    print("Option 4: Exit ")

#lưu trữ thông tin
def Store_infor():    
    name = input("Your full name is:")
    adress = input("Your address is: ")
    pin_code = input("Creat your pin code: ")
    phone = input("Update your phone number: ")
    infor = {"full name:" : [name], "Adress:": [adress], "Pin code:":[pin_code], "Phone number:":[phone]}
    with open("infor_customer","wb") as f:
        pickle.dump(infor, f)
    return f

def run():
    print("Welcome to Bank ABCXYZ")
    creat_account()
    creat_password()
    display_screen()
    while True:
        choice = input("Slecet your option: ")
        if choice == "1":
             Store_infor()
        else:
            break
run()


#bài làm còn thiếu chức năng: 
# Cho phép người dùng sửa đổi thông tin của bản thân.
# Cho phép gửi/rút tiền, chuyển tiền giữa các tài khoản.
# Ghi nhận số tiền người dùng có trong tài khoản.
# Bảo đảm bí mật những thông tin của người dùng.


# Tìm kiếm thông tin khách hàng bằng cách:
# import pickle
# with open("infor_customer","rb") as data:
#     infor = pickle.load(data)
# print(infor)

