string=" Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."

#a
string1=["Python","contains","experience","difficult"]
for i in range(len(string1)):
    if string1[i] in string:
        print(string1[i]+" có tồn tại trong đoạn văn.")
    else:
        print(string1[i]+" không tồn tại trong đoạn văn:")
        
#b
a= string.count("Python")
print("Số lần xuất hiện của 'Python' trong đoạn văn trên:", a)

#c
so_tu=string.split()

print("Số từ trong đoạn văn là:",len(so_tu))

#d
string2= "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it)."
string3=string2.upper()

print(string3)

