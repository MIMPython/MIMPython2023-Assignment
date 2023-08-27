listOfa = ['a', 'à', 'á', 'ả', 'ã', 'ạ', 'ă', 'ằ', 'ắ', 'ẳ', 'ẵ', 'ặ', 'â', 'ầ', 'ấ', 'ẩ', 'ẫ', 'ậ']
listOfd = ['d', 'đ']
listOfe = ['e', 'è', 'é', 'ẻ', 'ẽ', 'ẹ', 'ê', 'ề', 'ế', 'ể', 'ễ', 'ệ']
listOfi = ['i', 'ì', 'í', 'ỉ', 'ĩ', 'ị']
listOfo = ['o', 'ò', 'ó', 'ỏ', 'õ', 'ọ', 'ô', 'ồ', 'ố', 'ổ', 'ỗ', 'ộ', 'ơ', 'ờ', 'ớ', 'ở', 'ỡ', 'ợ']
listOfu = ['u', 'ù', 'ú', 'ủ', 'ũ', 'ụ', 'ư', 'ừ', 'ứ', 'ử', 'ữ', 'ự']
listOfy = ['y', 'ỳ', 'ý', 'ỷ', 'ỹ', 'ỵ']
listOfA = ['A', 'À', 'Á', 'Ả', 'Ã', 'Ạ', 'Ă', 'Ằ', 'Ắ', 'Ẳ', 'Ẵ', 'Ặ', 'Â', 'Ầ', 'Ấ', 'Ẩ', 'Ẫ', 'Ậ']
listOfD = ['D', 'Đ']
listOfE = ['E', 'È', 'É', 'Ẻ', 'Ẽ', 'Ẹ', 'Ê', 'Ề', 'Ế', 'Ể', 'Ễ', 'Ệ']
listOfI = ['I', 'Ì', 'Í', 'Ỉ', 'Ĩ', 'Ị']
listOfO = ['O', 'Ò', 'Ó', 'Ỏ', 'Õ', 'Ọ', 'Ô', 'Ồ', 'Ố', 'Ổ', 'Ỗ', 'Ộ', 'Ơ', 'Ờ', 'Ớ', 'Ở', 'Ỡ', 'Ợ']
listOfU = ['U', 'Ù', 'Ú', 'Ủ', 'Ũ', 'Ụ', 'Ư', 'Ừ', 'Ứ', 'Ử', 'Ữ', 'Ự']
listOfY = ['Y', 'Ỳ', 'Ý', 'Ỷ', 'Ỹ', 'Ỵ']
checkList = [listOfa, listOfA, listOfD, listOfd, listOfE, listOfe, listOfI, listOfi, listOfO, listOfo, listOfU, listOfu, listOfY, listOfy]

def transfer(word):
    newWordLettersList = []
    count = 0
    for char in word:
        if char == ' ':
            continue
        else:
            for lst in checkList:
                if char in lst:
                    newWordLettersList.append(lst[0])
                    count = 0
                    break
                else:
                    count += 1
            if count == 14:
                newWordLettersList.append(char)
                count = 0
        newWord = ''.join(newWordLettersList)
    return newWord

print(transfer('Hà Nội')) #HaNoi

# Nhược điểm của cách làm: các list trên mới chỉ chứa những kí tự được tạo ra bởi Telex - Unicode, chúng sẽ không 
# nhận diện được những kí tự lấy từ bên ngoài

# Khắc phục: tìm cách bổ sung các kí tự nêu trên