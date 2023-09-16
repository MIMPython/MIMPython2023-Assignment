# '''Chưa hoàn thành'''
#
# '''Nếu ở cuối n! xuất hiện số 0 nghĩa là trong tích của n! có chứa tích (2.5), nghĩa là ta chỉ cần đi tìm số lượng số
# 2 và số 5 rồi lấy số nhỏ hơn, nhưng dễ thấy số số 2 trong tích của n! luôn lớn hon số số 5, do đó chỉ cần tìm số lần
# xuất hiện của số 5'''
#
# def count_zero1(n: int) -> int :
#     s = 0
#     for i in range(5, n + 1, 5) :
#         tmp = i
#         while tmp % 5 == 0 :
#             s = s + 1
#             tmp = tmp / 5
#     return s
#
# print(count_zero1(50))
#
# def factorial(n) :
#     s = 1
#     for i in range(1,n + 1) :
#         s = s * i
#     return s
# print(factorial(50))

