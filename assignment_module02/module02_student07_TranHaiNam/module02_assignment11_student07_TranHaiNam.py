a= float(input("Điểm thường xuyên là: "))
b= float(input("Điểm giữa kì là: "))
c= float(input("Điểm cuối kì là:"))

average_point= ( a*2 +b*2 + c*6)/ 10

def diem_tb(a,b,c):
   if average_point < 4:
      print("Điểm tổng kết là:",average_point,"Điểm chữ tương ứng là: F")
   elif average_point <= 4.9:
      print("Điểm tổng kết là:",average_point,"Điểm chữ tương ứng là: D")
   elif average_point <= 5.4:
      print("Điểm tổng kết là:",average_point,"Điểm chữ tương ứng là: D+")
   elif average_point <= 6.4:
      print("Điểm tổng kết là:",average_point,"Điểm chữ tương ứng là: C")
   elif average_point <= 6.9:
      print("Điểm tổng kết là:",average_point,"Điểm chữ tương ứng là: C+")
   elif average_point <=7.9:
      print("Điểm tổng kết là:",average_point,"Điểm chữ tương ứng là: B")
   elif average_point <=8.4:
      print("Điểm tổng kết là:",average_point,"Điểm chữ tương ứng là: B+")
   elif average_point <=8.9:
      print("Điểm tổng kết là:",average_point,"Điểm chữ tương ứng là: A")
   else: 
      print("Điểm tổng kết là:",average_point,"Điểm chữ tương ứng là: A+")

diem_tb(a,b,c)


