import numpy as np
rng = np.random

class Matrix:
    def __init__(self, m, n):
        if m == n == 0:
            self.matrix = None
        else:
            self.matrix = Matrix.getMat(m, n)

    def swapRows(self, row1, row2) -> None:
        """
        Đổi chỗ hai hàng của một mảng 2 chiều.
        """
        self.matrix[[row1, row2]] = self.matrix[[row2, row1]]

    def mulRow(self, row, multiplier) -> None:
        """
        Nhân một hàng của một mảng 2 chiều với một số khác 0.
        """
        assert multiplier != 0
        self.matrix[row,] *= multiplier

    def addRow(self, row, addrow, mul) -> None:
        """
        Cho array matrix và hai hàng row, addrow.
        Cộng vào row một lượng bằng mul * addrow.
        """
        self.matrix[row,] += mul * self.matrix[addrow,]

    @staticmethod
    def getMat(m, n) -> np.ndarray:
        """
        Tạo một ma trận cỡ m*n, hệ số trong khoảng [0, 1),
        tạo theo phân bố đều.
        """
        return rng.rand(m, n)

    def roundMat(mat, round_digit) -> np.ndarray:
        """
        Làm tròn tất cả các hệ số với số chữ số sau dấu
        phẩy được cho bởi tham số round_digit.
        """
        def coeffRound(iter):
            return [round(i, round_digit) for i in iter]
        return np.apply_along_axis(coeffRound, 0, mat)

    def normalizeMat(mat, range: tuple = (-100, 100), round_digit: int = 0) -> np.ndarray:
        """
        Áp dụng cho ma trận tạo bởi method getMat().
        Giãn nở và tịnh tiến các hệ số của ma trận vào nửa khoảng [range[0], range[1]),
        đồng thời làm tròn các hệ số theo tham số round_digit. 
        Nếu range = None, không giãn nở các hệ số.
        """
        if range != None:
            def normalize(iter):
                return [round(i * (range[1] - range[0]) + range[0], round_digit) for i in iter]
            return np.apply_along_axis(normalize, 0, mat)
        else:
            Matrix.roundMat(mat, round_digit)

    def GaussElimination(mat, row_lim: tuple = None, col_lim: tuple = None) -> np.ndarray:
        """
        Khử Gauss ma trận mat bằng các phép biến đổi tuyến tính
        sơ cấp hàng, đưa về dạng bậc thang thu gọn. 
        Chỉ thực hiện khử Gauss trong khoảng hàng, cột xác định bởi tham số 
        row_lim (hàng) và col_lim (cột).
        Mặc định: row_lim = (1, mat.shape[0]), col_lim = (1, mat.shape[1]),
        tức là toàn bộ ma trận.
        # """
        mat_instance = Matrix(0, 0)
        mat_instance.matrix = np.ndarray.copy(mat)
        if row_lim == None: row_lim = (1, mat.shape[0])
        if col_lim == None: col_lim = (1, mat.shape[1])
        size = min(row_lim[1] - row_lim[0] + 1, col_lim[1] - col_lim[0] + 1)
        pos = (row_lim[0] - 1, col_lim[0] - 1)
        for _ in range(size):
            for row in range(pos[0], row_lim[1]):
                if mat_instance.matrix[row, pos[1]] != 0:
                    mat_instance.swapRows(row, pos[0])
                    break
            if mat_instance.matrix[pos[0], pos[1]] == 0: continue
            mat_instance.mulRow(pos[0], 1/mat_instance.matrix[pos[0], pos[1]])
            for row in range(row_lim[0] - 1, row_lim[1]):
                if row != pos[0]:
                    mat_instance.addRow(row, pos[0], -mat_instance.matrix[row, pos[1]])
            pos = (pos[0] + 1, pos[1] + 1)
        return mat_instance.matrix

    def solveGaussEliminatedMatrix(mat):
        """
        Biện luận nghiệm của hệ phương trình, 
        chỉ dùng khi ma trận hệ số đã được khử Gauss.
        Output là một tuple gồm các string, thể hiện không gian
        nghiệm của hệ. Nếu hệ vô nghiệm, trả về tuple rỗng.
        """
        rows, cols = mat.shape[0], mat.shape[1] - 1
        sol = ["" for i in range(cols)]
        for row in range(rows):
            if all(mat[row, i] == 0 for i in range(cols)) and mat[row, cols] != 0:
                return ()
        if rows >= cols:
            for index in range(cols, 0, -1):
                if all(mat[index - 1, i] == 0 for i in range(cols)):
                    sol[index - 1] = f"x{index} = Any"
                else:
                    sol[index - 1] = f"x{index} = {mat[index - 1, cols]}"
            return tuple(sol)
        else:
            for index in range(cols, rows, -1):
                sol[index - 1] = f"x{index} = Any"
            for index in range(rows, 0, -1):
                sol_string = f"x{index} = {mat[index - 1, cols]}"
                for i in range(rows + 1, cols + 1):
                    coeff = mat[index - 1, i - 1]
                    if coeff > 0:
                        sol_string += f" - {coeff}*x{i}"
                    elif coeff < 0:
                        sol_string += f" + {-coeff}*x{i}"
                sol[index - 1] = sol_string
            return tuple(sol)

    def solveLinearSystem(coeff_mat: np.ndarray, result: np.ndarray) -> dict:
        """
        Tìm nghiệm của hệ phương trình tuyến tính thực
        Ax = b, trong đó A là ma trận hệ số, cho bởi coeff_mat;
        b là cột hệ số tự do, cho bởi result.
        """
        system_mat = np.hstack((coeff_mat, result))
        Gauss_reduced_mat = Matrix.GaussElimination(system_mat, col_lim = (1, coeff_mat.shape[1]))
        refined_Gauss_reduced_mat = Matrix.roundMat(Gauss_reduced_mat, 3)
        sol = Matrix.solveGaussEliminatedMatrix(refined_Gauss_reduced_mat)
        system_info = {
            "System matrix": system_mat,
            "Gauss eliminated matrix": Gauss_reduced_mat,
            "Refined Gauss eliminated matrix": refined_Gauss_reduced_mat,
            "Solution": sol
        }
        return system_info

    def extractNumericalSolutions(tup):
        """
        Dùng cho nghiệm dạng string của method solveGaussEliminatedMatrix.
        Trong trường hợp ma trận hệ số là vuông, khả nghịch, trả về giá trị
        số của nghiệm.
        """
        sol = []
        for item in tup:
            sol.append(float(item.split("= ")[1]))
        return tuple(sol)

    def compareSolvingMethods(matrix_size: int = 4):
        """
        So sánh kết quả của hai cách giải 
        hệ phương trình không suy biến (số ẩn bằng số phương trình
        và nghiệm tồn tại duy nhất).
        """
        matrix = Matrix.normalizeMat(Matrix.getMat(matrix_size, matrix_size), round_digit = 3)
        result = Matrix.normalizeMat(Matrix.getMat(matrix_size, 1), round_digit = 3)
        system_info = Matrix.solveLinearSystem(matrix, result)
        for key, value in system_info.items():
            print(key)
            print(value)
            print("\n")
        assert system_info["Solution"] != (), "Hệ phương trình vô nghiệm."
        self_taught_sol = np.array(Matrix.extractNumericalSolutions(system_info["Solution"])).reshape((matrix_size, 1))
        numpy_sol = np.linalg.solve(matrix, result)
        print(f"Self-taught solution:\n{self_taught_sol}")
        print(f"Numpy solution:\n{numpy_sol}")
        print(f"Identical solutions (with 0.001 numpy tolerance): {np.allclose(numpy_sol, self_taught_sol, rtol = 0.001, atol = 0.001)}")        

Matrix.compareSolvingMethods()
print("---------------------------------------------------------------")

# Giải hệ phương trình cỡ bất kỳ
# matrix = Matrix.normalizeMat(Matrix.getMat(3, 6), round_digit = 3)
# result = Matrix.normalizeMat(Matrix.getMat(3, 1), round_digit = 3)
# system_info = Matrix.solveLinearSystem(matrix, result)
# for key, value in system_info.items():
#     print(key)
#     print(value)
#     print()

"""
Có thể làm việc với class Fraction để trả về kết quả chính xác cho
các bài toán giải hệ phương trình, tìm nghịch đảo,... trong trường hợp
các hệ số đều hữu tỷ.
"""