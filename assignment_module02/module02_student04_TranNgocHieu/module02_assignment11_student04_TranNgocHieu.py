def gpa(tx, gk, ck):
    """
    Đầu vào là 3 điểm thành phần theo thang 10. Đầu ra là điểm trung 
    bình bằng chữ.
    """
    import pandas
    dtb = round(tx*0.2 + gk*0.2 + ck*0.6, 1)
    dc = pandas.cut([dtb], bins = [0, 4, 5, 5.5, 6.5, 7, 8, 8.5, 9, 10.1],
                    include_lowest = True, right = False,
                    labels = ['F', 'D', 'D+', 'C', 'C+',
                              'B', 'B+', 'A', 'A+'])
    return dc[0]

print(gpa(9.5, 8, 9))    # A (dtb: 8.9)
print(gpa(8, 9, 10))    # A+ (dtb: 9.4)
print(gpa(8, 8, 8))    # B+ (dtb: 8.0)