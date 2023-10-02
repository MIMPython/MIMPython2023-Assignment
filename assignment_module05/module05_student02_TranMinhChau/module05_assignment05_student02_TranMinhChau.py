# Bài tập 5: (infinite loop)
#(a) Dùng vòng lặp while.
while True:
    print("Câu a")

# #(b) Dùng vòng lặp for mà không cần vòng lặp while.
from itertools import count

for _ in count():
    print("Câu b")

#(c) Dùng vòng lặp for với đối tượng không phải là list, tuple, set, hay dictionary.
class InfiniteLoop:
    def __iter__(self):
        return self
    
    def __next__(self):
        return "Câu c"
infinite_iter = InfiniteLoop()
for _ in infinite_iter:
    print(_)

