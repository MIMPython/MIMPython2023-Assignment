def calculate_average(input_list: list) -> float:

    try:
        total = sum(input_list)
        average = total/len(list)
    except ValueError:
        print('Empty list. Cannot calculate the average.')
    except Exception as e:
        print(f'Error: {e}')
    else:
        print(average)


if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 'hello']
    calculate_average(input_list)
