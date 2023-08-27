

# Ý a)
paragraph="Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."


print("Python" in paragraph)
print("contains" in paragraph)
print("experience" in paragraph)
print("difficult" in paragraph)


# Ý b)

countPython=0   #Biến đếm tính số từ khóa xuất hiện độc lập
countPython1=0  #Biến đếm tính số từ khóa Python có xuất hiện một dấu ở đằng sau, vì các dấu ở đằng trước đều được ngăn cách bởi khoảng trắng
countPython2=0  #Biến đếm nếu từ khóa Python nằm trong 1 cặp dấu nào đó
list=paragraph.split(" ")
for word in list:
    if word=="Python":
        countPython+=1  #countPython=4

for word in list:
    if word[0:len(word)-1]=="Python":
        countPython1+=1 #countPython1=1

for word in list:
    if word[1:len(word)-1]=="Python":
        countPython2+=1 #countPython2=0

#c)
print(len(list))

#d)
list1=paragraph.split(".")
list2=list1[0].split(" ")
for word in list2:
    print(word.title(), end=' ')
                            






