from getpass import getpass
import math


def infinityLoop():
    while True:
        print("Input something: ")
        x = input()
        try:
            if int(x) >= 0 and int(x) <= 9:
                print("Finish: input=", x)
                break
        except:
            pass


def game():
    print(
        "Choose one item: [\"rock\", \"paper\", \"scissors\"] and type its name in the terminal")
    a = getpass(prompt="A: ")
    print("B: ")
    b = input()
    print("A choose: ", a)
    if a == b:
        print("Equal")
    else:
        if a == "rock":
            if b == "paper":
                print("B win")
            else:
                print("A win")
        elif a == "paper":
            if b == "rock":
                print("A win")
            else:
                print("B win")
        else:
            if b == "rock":
                print("B win")
            else:
                print("A win")


if __name__ == "__main__":
    # infinityLoop()
    game()
# Mô tả: Yêu cầu 1): Tạo chương trình chỉ dừng khi người dùng nhập vào một chữ số 2) Tạo chương trình để 2 người chơi oẳn tù tì
# Chạy code: python module03_assignment05_student05_NguyenQuocHieu.py
