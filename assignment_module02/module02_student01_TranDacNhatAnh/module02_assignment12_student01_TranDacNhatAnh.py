# Test các biến
foo = ('a'),
bar = 'a',
ham = ('a', )
print(type(foo), type(bar), type(ham)) # <class 'tuple'> <class 'tuple'> <class 'tuple'>
print(foo == bar) # True
# Các biến trên là giống nhau

foo = 'Đà Nẵng'
bar = 'Đà Nẵng'
print(foo == bar) #False 
# --> Có nhiều hơn 1 cách để gõ ra kí tự có dấu, các cách này sẽ cho ra các kí tự được coi là khác nhau
