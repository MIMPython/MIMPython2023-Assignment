# Bài tập 12

foo = ('a'),
bar = 'a',
ham = ('a', )

print(foo, bar, ham)

# sau khi chạy lệnh trên thì mình nhận ra cả ba cách viết kia đều dùng để tạo
# một tuple dạng (a, ) (biết thêm các cách tạo tuple, tránh hiểu nhầm khi đọc
# code)

foo = 'Đà Nẵng'
bar = 'Đà Nẵng' 
foo_chars = list(foo)
bar_chars = list(bar)
for char in foo_chars: 
    print(char)
print("\n")
for char in bar_chars:
    print(char)


# sau khi chạy chương trình này thì thấy sự khác biệt giữa số lượng ký tự ở
# 2 biến foo và bar mặc dù trực quan thì 2 biến giống nhau.
# Lý do vì sao thì không hiểu.

