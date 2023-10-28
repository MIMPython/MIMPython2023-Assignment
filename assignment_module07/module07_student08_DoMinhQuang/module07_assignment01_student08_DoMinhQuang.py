def mean_compute(list: list):
    try:
        return sum(list) / len(list)
    except TypeError:
        return 'Invalid list'
    except ZeroDivisionError:
        return 'List is empty'

list_1 = []
list_2 = ['a', 'b', 1]
list_3 = ['a', 'b', 'c']
list_4 = [1,2,3,4]
print(mean_compute(list_1)) #List is empty
print(mean_compute(list_2)) #Invalid list
print(mean_compute(list_3)) #Invalid list
print(mean_compute(list_4)) #2.5


def omit_invalid_value(list: list) -> list:
    new_list = []
    for i in list:
        if type(i) is int or type(i) is float:
            new_list.append(i)
    return new_list

print(omit_invalid_value(list_2)) #[1]
print(omit_invalid_value(list_3)) #[]
