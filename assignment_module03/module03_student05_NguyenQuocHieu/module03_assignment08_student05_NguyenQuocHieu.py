import json
from getpass import getpass
import os


class Database:
    """
    Class xử lý dữ liệu tài khoản của người dùng
    """

    def __init__(self) -> None:
        self.path = os.getcwd() + \
            "\\additionFolder\\module03_assignment08_student05_NguyenQuocHieu_accounts.json"

    def isExist(self, username: str) -> bool:
        """
        Kiểm tra một username đã tồn tại hay chưa
        """
        with open(self.path, "r") as file:
            data = json.load(file)
        return username in data

    def checkPassword(self, username: str, password: str) -> bool:
        """
        Kiểm tra mật khẩu nhập vào đúng hay sai
        """
        with open(self.path, "r") as file:
            data = json.load(file)
        checkPass = data[username]
        return checkPass == password

    def update(self, username: str, password: str) -> None:
        """
        Cập nhật mật khẩu và tên đăng nhập mới
        """
        with open(self.path, "r") as file:
            data = json.load(file)
        data[username] = password
        with open(self.path, "w") as file:
            json.dump(data, file)


class SignUpProcess:
    """
    Class xử lý các vấn đề liên quan đến đăng ký
    """

    def __init__(self) -> None:
        self.datatabase = Database()
        self.signinProcess = None
        self.bank = None

    def checkPassword(self, password: str) -> bool:
        """
        Some rules for a password which is called strong:
        - Contains at least 8 character
        - Contains at least 1 special character
        - Contains both upper and lower letter
        - Contains digits
        """
        def check(array: list[int], lower: int, upper: int) -> bool:
            for i in array:
                if i >= lower and i <= upper:
                    return True
            return False
        if len(password) < 8:
            return False
        else:
            asciiCode = []
            for char in password:
                asciiCode.append(ord(char))
            if check(array=asciiCode, lower=65, upper=90) and check(array=asciiCode, lower=97, upper=122) and check(array=asciiCode, lower=48, upper=57):
                return True
            else:
                return False

    def createNewAccount(self, username: str) -> None:
        if self.datatabase.isExist(username=username):
            print("Username exists in database. Direct to Sign In")
            password = getpass()
            self.signinProcess = SignInProcess()
            self.signinProcess.signIn(username=username, password=password)
        else:
            password = getpass()
            if self.checkPassword(password=password):
                rePassword = getpass(prompt="Input password again: ")
                if password != rePassword:
                    print("Sign up again: ")
                    exit()
                else:
                    self.datatabase.update(
                        username=username, password=password)
                    self.bank = Bank(username=username)
                    self.signinProcess = SignInProcess()
                    self.signinProcess.signIn(
                        username=username, password=password)
            else:
                print("Password is weak! Try again? \n Y/N")
                request = input()
                if request == "Y":
                    self.createNewAccount(username=username)
                else:
                    exit()


class SignInProcess:
    """
    Class xử lý các vấn đề liên quan đến đăng nhập
    """

    def __init__(self) -> None:
        self.database = Database()
        self.request = None
        self.bank = None

    def signIn(self, username: str, password: str) -> None:
        if self.database.checkPassword(username=username, password=password):
            print("Sign in sucessfully")
            # Send message to bank
            self.bank = Bank(username=username)
            self.bank.initialize()
        else:
            print("Wrong password! Try again? \n Y/N")
            message = input()
            if message == "Y":
                self.request = Request()
                self.request.signIn()
            else:
                exit()


class Bank:
    """
    App mô tả các tính năng cơ bản của ngân hàng, bao gồm gửi tiền, rút tiền và chuyển tiền
    """

    def __init__(self, username: str) -> None:
        self.path = os.getcwd() + \
            "\\additionFolder\\module03_assignment08_student05_NguyenQuocHieu_bank.json"
        self.handleConflict()
        self.username = username
        self.moneyAccount = self.get()

    def handleConflict(self) -> None:
        """
        Xử lý xung đột dữ liệu
        """
        accountPath = os.getcwd() + \
            "\\additionFolder\\module03_assignment08_student05_NguyenQuocHieu_accounts.json"
        with open(self.path, "r") as bankFile:
            bankData = json.load(bankFile)
        with open(accountPath, "r") as accountFile:
            accountData = json.load(accountFile)
        for username in accountData:
            if username not in bankData:
                bankData[username] = 0.0
        with open(self.path, "w") as file:
            json.dump(bankData, file)

    def get(self) -> float:
        """
        Trả về số tiền của một username cụ thể
        """
        with open(self.path, "r") as file:
            data = json.load(file)
        return data[self.username]

    def initialize(self) -> None:
        """
        Khởi tạo và cung cấp cho người dùng 3 tính năng: gửi tiền, rút tiền hoặc chuyển tiền
        """
        print("Choose one feature to use MIMPython Bank: ")
        print("Type 1 to deposit")
        print("Type 2 to withdraw")
        print("Type 3 to transfer")
        request = input()
        if request == "1":
            self.deposit()
        elif request == "2":
            self.withdraw()
        elif request == "3":
            self.transfer()
        else:
            print("Shut down...")
            exit()

    def deposit(self):
        """
        Gửi tiền
        """
        amount = float(input("Input money you want to deposit: "))
        with open(self.path, "r") as file:
            data = json.load(file)
        data[self.username] += amount
        with open(self.path, "w") as file:
            json.dump(data, file)
        print("Deposit successfully!")

    def withdraw(self):
        """
        Rút tiền
        """
        amount = float(input("Input money you want to withdraw: "))
        with open(self.path, "r") as file:
            data = json.load(file)
        if data[self.username] >= amount:
            data[self.username] -= amount
            with open(self.path, "w") as file:
                json.dump(data, file)
            print("Withdraw successfully!")
        else:
            print("Not enough money to withdraw. Try again? \n Y/N")
            request = input()
            if request == "Y":
                self.withdraw()
            else:
                print("Exit program...")
                exit()

    def transfer(self):
        """
        Chuyển tiền
        """
        destination = input("Input username who gives money: ")
        with open(self.path, "r") as file:
            data = json.load(file)
        if destination not in data:
            print("Error! Username not found")
            exit()
        else:
            amount = float(input("Input money you want to transfer: "))
            if data[self.username] >= amount:
                data[self.username] -= amount
                data[destination] += amount
                with open(self.path, "w") as file:
                    json.dump(data, file)
                print("Transfer successfully!")
            else:
                print("Not enough money!")
                exit()


class Request:
    def __init__(self) -> None:
        self.signinProcess = None
        self.signupProcess = None

    def signIn(self) -> None:
        """
        Đăng nhập
        """
        print("Sign in: ")
        username = input("Username: ")
        password = getpass()
        self.signinProcess = SignInProcess()
        self.signinProcess.signIn(
            username=username, password=password)

    def signUp(self) -> None:
        """
        Đăng ký
        """
        print("Sign up: ")
        username = input("Username: ")
        self.signupProcess = SignUpProcess()
        self.signupProcess.createNewAccount(
            username=username)

    def initialize(self) -> None:
        """
        Cung cấp 2 tính năng cho người dùng lựa chọn: đăng nhập hoặc đăng ký
        """
        print("Welcome to MIMPython Bank")
        print("Type 1 to sign in")
        print("Type 2 to sign up")
        request = input()
        if request == "1":
            self.signIn()
        elif request == "2":
            self.signUp()
        else:
            print("Shut down...")
            exit()


class Program:
    def __init__(self) -> None:
        self.request = Request()

    def run(self):
        """
        Khi chạy run(), gửi yêu cầu đến Request()
        """
        self.request.initialize()


if __name__ == "__main__":
    program = Program()
    program.run()

# Mô tả: Tạo chương trình mô phỏng một ứng dụng ngân hàng, bao gồm các tính năng: đăng ký, đăng nhập, chuyển tiền, rút tiền, gửi tiền
# Chạy code: python module03_assignment08_student05_NguyenQuocHieu.py
