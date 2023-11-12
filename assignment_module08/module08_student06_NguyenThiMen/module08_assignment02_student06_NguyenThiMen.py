import numpy as np
import matplotlib.pyplot as plt
import time
np.random.seed(55)


def gauss_elimination(A):
    m, n = A.shape
    # khử gauss
    for i in range(min(m, n)):
        if A[i, i] != 0:
            for j in range(i+1, m):
                t = A[j, i]/A[i, i]
                A[j, i:] -= t*A[i, i:]
        else:
            # tìm A[j,i] != 0 và hoán đổi
            for j in range(i+1, m):
                if A[j, i] != 0:
                    A[[i, j]] = A[[j, i]]
                    break
    return A


def get_rank(A):
    rank = 0
    for i in range(A.shape[0]):
        if np.any(A[i, :] != 0):
            rank += 1
    return rank


def get_roots(A):
    m, n = A.shape
    x = [0]*(n-1)
    for i in range(m - 1, -1, -1):
        x[i] = A[i, -1] / A[i, i]
        for j in range(i):
            A[j, -1] -= A[j, i] * x[i]
    return x


def return_the_solution(A, b):
    m, n = A.shape
    A_ = np.zeros((m, n + 1), dtype=np.float64)
    A_[:, : -1] = A
    A_[:, -1] = b
    rank_A = get_rank(gauss_elimination(A))
    rank_A_ = get_rank(gauss_elimination(A_))
    if rank_A == rank_A_ == n:
        print(f'Hệ có nghiệm duy nhất: {get_roots(A_)}')
    elif rank_A_ == rank_A < n:
        print('Hệ có vô số nghiệm')
    elif rank_A_ != rank_A:
        print('Hệ vô nghiệm')


def solve_linear_system_with_numpy(A, b):
    try:
        x = np.linalg.solve(A, b)
        print(x)
    except np.linalg.LinAlgError:
        print('Hệ phương trình có vô số nghiệm hoặc vô nghiệm')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # array = np.random.randint(0, 11, size=(4, 3))
    # A = np.array(array, dtype = float)
    # print(A)
    # b = np.random.randint(0, 11, size = (4,))
    # print(b)
    # A = np.array([[-3, 4, 6], [0, 1, 1], [2, -3, -4]], dtype=float)
    # b = [2, 3, 5]  # [ 18. -19.  22.]
    A = np.array([[1, 2, 3, 4, 5], [1, -2, -3, -4, -5],
                 [1, 4, 6, 8, 10], [2, 2, 3, 4, 5]], dtype=float)
    b = [0, 2, -1, 1]
    start_time1 = time.perf_counter()
    solve_linear_system_with_numpy(A, b)
    end_time1 = time.perf_counter()
    start_time2 = time.perf_counter()
    return_the_solution(A, b)
    end_time2 = time.perf_counter()

    fig, ax = plt.subplots()
    ax.bar(['Numpy', 'Manual'], [end_time1 - start_time1,
           end_time2 - start_time2], color='blue')
    ax.set(title='Compare implement time', ylabel='Time(s)')
    plt.savefig(
        'additionalFolder/module08_student06_NguyenThiMen_ex1.png', format='png')
    plt.show()
