#Bài tập 3:
def create_file_name(ten, id, baitap, tuan):
  if tuan < 10:
    tuan = f'{tuan:02d}'
  if id < 10:
    id = f'{id:02d}'
  if baitap < 10:
    baitap = f'{baitap:02d}'
  file_name = f"week{tuan}_assignment{baitap}_student{id}_{ten}.py"
  return file_name
print(create_file_name("TranMinhChau", 2, 3, 2))
print(create_file_name("NguyenVanA", 12, 1, 2))


