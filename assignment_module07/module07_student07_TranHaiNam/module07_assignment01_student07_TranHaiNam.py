def list_average(list):
    try:
        l = len(list)
        average = sum(list) / l
        return average
    except ZeroDivisionError:
        return f'List is empty'
    except TypeError:
        return f'List must cotain just number type'

list = [1]
print(list_average(list))

    