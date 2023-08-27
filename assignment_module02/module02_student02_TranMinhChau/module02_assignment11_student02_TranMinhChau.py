#Bài tập 11 :
def diem_chu(thuongxuyen, giuaky, cuoiky):
    diem_tb = thuongxuyen * 0.2 + giuaky * 0.2 + cuoiky * 0.6
    if diem_tb > 9:
        return "A+"
    elif diem_tb > 8:
        return "A"
    elif diem_tb == 8:
        return "B+"
    elif diem_tb > 7:
        return "B"
    elif diem_tb > 6.5:
        return "C+"
    elif diem_tb > 5.5:
        return "C"
    elif diem_tb > 5:
        return "D+"
    elif diem_tb > 4:
        return "D"
    else:
        return "F"
thuongxuyen = float(input("Điểm thường xuyên là :"))
giuaky = float(input("Điểm giữa kỳ là:"))
cuoiky = float(input("Điểm cuối kỳ là:"))
print("Điểm:", diem_chu(thuongxuyen, giuaky, cuoiky) )

