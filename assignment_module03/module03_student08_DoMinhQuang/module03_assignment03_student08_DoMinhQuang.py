f = open('additionalFolder/module03_assignment03_student08_DoMinhQuang_data.txt', 'r')
names = f.read().split(",")
f.close()
names.sort()


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def findScore(str):
    s = 0
    for letter in str:
        index = int(alphabet.find(letter) + 1)
        s += index
    return s

def findPosition(str):
    for i in range(len(names)):
        if names[i] == str:
            return i + 1


if __name__ == '__main__':
    result = 0
    for i in range(len(names)):
        result += findScore(names[i]) * findPosition(names[i])

    print(result)


"module03_assignment03_student08_DoMinhQuang_data.txt"