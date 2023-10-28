# Bài tập 1:

def list_average(input):
    try:
        return sum(input)/len(input)
    except ZeroDivisionError:
        return "Cannot caculate average of empty list"
    except Exception as e:
        return e

input_1 = [1,2,3,4,5]
input_2 = [] 
input_3 = ["t",1,2,3,4]
print (list_average(input_1)) # 3.0
print (list_average(input_2)) # Cannot caculate average of empty list 
print (list_average(input_3)) # unsupported operand type(s) for +: 'int' and 'str'
                