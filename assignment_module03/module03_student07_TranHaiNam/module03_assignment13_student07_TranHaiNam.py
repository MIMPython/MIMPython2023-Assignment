def main(n):
    a = 2 ** n
    b = 5 ** n
    c = str(a+b)
    return str("Số có số chữ số là: ") + str(len(c)+1)

print(main(3)) #4
