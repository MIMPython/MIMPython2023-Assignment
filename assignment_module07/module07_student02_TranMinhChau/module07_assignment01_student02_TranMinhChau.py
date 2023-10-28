# Bài tập 1:  (list average)
def average(input_list):
  try:
    if len(input_list) == 0:
      raise ValueError("List rỗng")
    total = sum(input_list)
    return total / len(input_list)
  except Exception as e:
    return f"Có lỗi xảy ra: {e}"

A = [1, 2, 3, 4, 5]
print(average(A))
B = []
print(average(B))