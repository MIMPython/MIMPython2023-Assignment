#Bài tập 4: 
paragragh = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."

#a.Kiểm tra xem các từ khóa Python, contains, experience, difficult có tồn tại trong đoạn văn trên hay không?
print("Python" in paragragh)
print("contains" in paragragh)
print("experience" in paragragh)
print("difficult" in paragragh)

#b.Đếm số lần xuất hiện của từ khóa Python trong đoạn văn.
print(paragragh.count("Python"))

#c.Tính số từ trong đoạn văn trên.
words = paragragh.split()
print("Số từ trong đoạn văn là:", len(words))

#d.Viết lại đoạn văn trên, trong đó viết hoa tất cả các chữ cái trong câu đầu tiên của đoạn văn.
dot_index = paragragh.find(".")
first_sentence = paragragh[: dot_index + 1].upper()
new_paragraph = first_sentence + paragragh[dot_index + 1:]
print("Đoạn văn mới là :", new_paragraph)

