class password_check():
    def __init__(self, password):
        self.password = password

    def check_num(self):
        return any(char.isdigit() for char in self.password)

    def check_upper(self):
        return any(char.isupper() for char in self.password)

    def check_special(self):
        special = "[@_!#$%^&*()<>?/|}{~:]"
        return any(char in special for char in self.password)

    def password_error(self):
        if self.check_num() == False:
            print("Password must contain a number.")
        if self.check_upper() == False:
            print("Password must contain an uppercase character.")
        if self.check_special() == False:
            print("Password must contain a special character.")

    def check_password(self):
        return all([self.check_num(), self.check_special(), self.check_upper()])

def password_enter(): 
    import getpass 
    password = getpass.getpass(prompt = "Enter your password: ")
    password_instance = password_check(password)
    if password_instance.check_password():
        print("Password accepted.")
    else:
        while password_instance.check_password() == False:
            print("\nPassword missing requirements.\n")
            password_instance.password_error()
            print()
            password = getpass.getpass(prompt = "Enter your password again: ")
            password_instance = password_check(password)
        print("Password accepted.\n")
    return password

def password_recheck(password):
    import getpass
    confirm = getpass.getpass(prompt = "Confirm your password: ") 
    while confirm != password:
        print("\nPassword mismatched.")
        confirm = getpass.getpass(prompt = "Reconfirm your password: ") 
    print("Confirmation complete.")

def greet_user(user):
    print(f"Hello {user} !")

def main():
    user = input("Enter a username: ")
    greet_user(user)

    password = password_enter()
    password_recheck(password)

if __name__ == "__main__":
    main()