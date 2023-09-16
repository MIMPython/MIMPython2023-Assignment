# Bài tập 11
input = [10, 10, 10]
print (f"Điểm thường xuyên: {input[0]}")
print (f"Điểm giữa kỳ: {input[1]}")
print (f"Điểm cuối kỳ: {input[2]}")

def main(input):
    average_score = input[0]*0.1 + input[1]*0.3 + input[2]*0.6
    if average_score <= 10 and average_score >= 9:
        print ("Điểm chữ: A+")
    elif average_score < 9 and average_score >= 8.5:
        print ("Điểm chữ: A")
    elif average_score < 8.5 and average_score >= 8:
        print ("Điểm chữ: B+")
    elif average_score < 8 and average_score >= 7:
        print ("Điểm chứ: B")
    elif average_score < 7 and average_score >= 6.5:
        print ("Điểm chữ: C+")
    elif average_score < 6.5 and average_score >= 5.5:
        print ("Điểm chữ: C")
    elif average_score < 5.5 and average_score >= 5:
        print ("Điểm chữ: D+")
    elif average_score < 5 and average_score >= 4:
        print ("Điểm chữ: D")
    else:
        print ("Điểm chữ: F")


main(input)