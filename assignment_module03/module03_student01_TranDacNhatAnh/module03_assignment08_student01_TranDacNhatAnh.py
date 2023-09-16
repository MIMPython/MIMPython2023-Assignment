from getpass import getpass
uppercase = [chr(i) for i in range(65, 91)]
lowercase = [chr(i) for i in range(97, 123)]
number = [str(i) for i in range(10)]
username = str(input('Please enter your username'))
password = getpass(prompt=f'{username}, please enter your password')
def checkPassword(password): # Điều kiện cần của một mật khẩu "mạnh"
    checkedLetters = 0
    for char in password:
        if char in uppercase:
            break
        elif char in lowercase:
            break
        elif char in number:
            break
        else:
            checkedLetters += 1
    return checkedLetters
while len(password)<8 or len(password) == checkPassword(password): # Ngoài các điều kiện trên, mật khẩu cũng cần đủ dài nữa :v
    print(f'{username}, your password is weak. A strong password should have at least 8 characters, with 1 uppercase, 1 lowercase and 1 number in it')
    password = getpass(prompt=f'{username}, please enter your password')
print('Your password is accepted')
doubleCheck = getpass(prompt='Please re-enter your password')
while doubleCheck != password:
    print('This is different from your password')
    doubleCheck = getpass(prompt='Please re-enter your password')
print(f'Re-entered successfully. Thank you very much, {username}!')
