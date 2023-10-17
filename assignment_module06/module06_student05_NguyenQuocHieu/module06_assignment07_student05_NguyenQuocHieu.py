import numpy
import time


def read_data(text_path: str):
    matrix = []
    with open(text_path, mode="r") as file:
        raw_data = file.readlines()
        for row in raw_data:
            row = row.replace("\n", "")
            row_data = row.split(" ")
            new_row = []
            for number in row_data:
                new_row.append(int(number))
            matrix.append(new_row)
    return numpy.array(matrix, dtype=numpy.uint32)


def evaluate(region: numpy.ndarray):
    rows = numpy.product(region, axis=0, dtype=numpy.int64)
    columns = numpy.product(region, axis=1, dtype=numpy.int64)
    first_diag = numpy.diagonal(region).prod(dtype=numpy.int64)
    second_diag = numpy.rot90(region).diagonal().prod(dtype=numpy.int64)
    values = numpy.concatenate(
        (rows, columns), dtype=numpy.int64)
    return numpy.max((numpy.max(values), first_diag, second_diag))


def sliding_region(matrix: numpy.ndarray):
    start = time.time()
    width, height = matrix.shape
    result = 0
    for index_w in range(width - 4):
        for index_h in range(height - 4):
            region = matrix[index_w: index_w + 4, index_h: index_h + 4]
            value = evaluate(region)
            if value > result:
                result = value
    end = time.time()
    print("Elapsed time: ", end - start)
    return result


if __name__ == "__main__":
    matrix = read_data(
        r"module06_student05_NguyenQuocHieu\additionFolder\module06_assignment07_student05_NguyenQuocHieu_data.txt")
    result = sliding_region(matrix)
    print(result)  # 70600674
