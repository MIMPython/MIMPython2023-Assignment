# Bài tập 3:

import string

def main(input):
    input = sorted(input)
    data = list(string.ascii_uppercase)
    result = []
    index = 0
    while (index < len(input)):
        element = list(input[index])
        sum = 0
        for i in range(len(element)):
            for j in range(len(data)):
                if element[i] == data[j]:
                    sum += j + 1
        result.append(sum * (index + 1))
        index += 1
        
    print (result)
        

# bộ data sets mẫu (10 tên)
input = ["JAMES", "MARY", "JOHN", "PATRICIA", "ROBERT", "JENNIFER", "MICHAEL", "LINDA", "WILLIAM", "ELIZABETH"]
main(input)        