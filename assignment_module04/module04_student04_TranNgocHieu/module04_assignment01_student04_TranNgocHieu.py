a = [[1, 2], [3, 0, 4], [2], [4, 5], ["abc"], ["an", 1]]

def checkList(my_list: list) -> list:
    """
    Check if a list contains non-float elements, return False if so.
    """
    for value in my_list:
        try:
            value = float(value)
        except ValueError:
            return False
    return True

def filterList(my_list: list) -> list:
    """
    Remove list elements (smaller lists) with non-float elements.
    Return a filtered copy of input list.
    """
    list_copy = my_list.copy()
    for list in my_list:
        if not checkList(list):
            list_copy.remove(list)
    return list_copy

def sortList1(my_list: list) -> list:
    """
    Sort a list by (rule 1) sum of list elements.
    Return a sorted copy of input list.
    """
    filtered_list_copy = filterList(my_list)
    filtered_list_copy.sort(key = lambda list: sum(float(num) for num in list))
    return filtered_list_copy
print(sortList1(a))

def compareInDictOreder(a: list, b: list) -> bool:
    """
    Compare two float strings in dictionary order.
    Return True if a < b, False otherwise.
    """
    ab = list(zip(a, b))
    for pair in ab:
        if pair[0] < pair[1]:
            return True
        elif pair[0] > pair[1]:
            return False
    return len(a) < len(b)

def findMinimumInDictOrder(my_list: list) -> list:
    """
    Find the minimum list in a list of float lists, in dictionary order.
    """
    min = my_list[0]
    for list in my_list:
        if compareInDictOreder(list, min):
            min = list
    return min

def sortInDictOrder1(my_list: list) -> list:
    """
    Sort a list by dictionary order.
    Return a sorted copy of input list.
    """
    list_copy = filterList(my_list.copy())
    sorted_list = []
    for _ in range(len(list_copy)):
        min = findMinimumInDictOrder(list_copy)
        sorted_list.append(min)
        list_copy.remove(min)
    return sorted_list
print(sortInDictOrder1(a))

def sortInDictOrder2(my_list: list) -> list:
    """
    Sort a list by the same dictionary order, using a different
    algorithm. Credits to Na Na.
    """
    list_copy = filterList(my_list.copy())
    for i in range(len(list_copy)):
        for j in range(i):
            if compareInDictOreder(list_copy[i], list_copy[j]):
                list_copy[i], list_copy[j] = list_copy[j], list_copy[i]
    return list_copy
print(sortInDictOrder2(a))


    
