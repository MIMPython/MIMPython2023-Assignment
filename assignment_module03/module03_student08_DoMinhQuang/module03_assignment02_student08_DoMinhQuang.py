f = open('additionalFolder/module03_assignment02_student08_DoMinhQuang_data.txt', 'r')
allLines = f.read().splitlines()
f.close()

s=0
for i in allLines:
    s=s+int(i)
str=str(s)
print(str[0:10])

"module03_assignment02_student08_DoMinhQuang_data.txt"

