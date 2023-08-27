# Hàm đếm số chữ số cần dùng để dánh số n trang sách - Cách 1: ghép các số vào rồi đếm độ dài
def countDigit(n):
    pages = []
    for i in range(1,n+1):
        pages.append(str(i))
    series = ''.join(pages)
    return len(series)
print(countDigit(10000)) #38894
# Cách 2: Cộng số chữ số dùng để đánh từng trang một
def digits(n):
    sum =0
    page =1
    while page<=n:
        sum += len(str(page))
        page += 1
    return sum
print(digits(10000)) #38894
# Cách 3: Lần lượt đếm số chữ số dùng để đánh số các trang có 1 chữ số, 2 chữ số,...
def count(n):
    sum =0
    t =1
    while 10**t<=n:
        t+=1
    for i in range(1,t):
        sum+= i*9*(10**(i-1))
    sum +=t*(n+1-10**(t-1))
    return sum
print(count(10000)) #38894
# Hàm đếm số trang có thể đánh số với n chữ số
def numberOfPages(n):
    pages =0
    while n>0:
        pages+=1
        n -= len(str(pages))
    return pages
print(numberOfPages(38894)) #10000