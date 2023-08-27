foo = ('a'),
bar = 'a',
ham = ('a', )
print(type(foo))# tuple
print(type(bar))# tuple
print(type(ham))# tuple

print(foo==bar)#true
print(bar==ham)#true
print(foo==ham)#true

#Vậy 3 biến là bằng nhau và cùng có kiểu tuple

foo = 'Đà Nẵng'
bar = 'Đà Nẵng'
print(foo==bar)

for letter in bar:
    if ord(letter) > 127:
        print(f"{letter} is a Unicode character.")
print()

for letter in foo:
    if ord(letter) > 127:
        print(f"{letter} is a Unicode character.")
#Vậy foo và bar khác nhau vì foo có chữa khoảng trắng là kí tự Unicode