# Bài tập yêu cầu ta "làm gì đó" với một mã Morse
MorseDictionary = { '.-':'A', '-...':'B',
                    '-.-.':'C', '-..':'D', '.':'E',
                    '..-.':'F', '--.':'G', '....':'H',
                    '..':'I', '.---':'J', '-.-':'K',
                    '.-..':'L', '--':'M', '-.':'N',
                    '---':'O', '.--.':'P','--.-':'Q',
                    '.-.':'R', '...':'S', '-':'T',
                    '..-':'U', '...-':'V', '.--':'W',
                    '-..-':'X', '-.--':'Y', '--..':'Z',
                    '.----':'1', '..---':'2', '...--':'3',
                    '....-':'4', '.....':'5', '-....':'6',
                    '--...':'7', '---..':'8', '----.':'9',
                    '-----':'0', '--..--':', ', '.-.-.-':'. ',
                    '..--..':'? ', '-..-.':'/ ', '-....-':'-',
                    '-.--.':'(', '-.--.-':')'}
letterMorseDictionary = {
    'DOT' : '.',
    'SPACE' : ' ',
    'DASH' : '-'
}
MorseMessage = '.- .-.. .-.. .. .-- .- -. - - --- ... .- -.-- .. ... -.. --- - -.. --- - ... .--. .- -.-. . -.. --- - -.. .- ... .... -.. --- - -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. --- - -.. .- ... .... ... .--. .- -.-. . -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. --- - -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. .- ... ....'
# Khá tự nhiên, việc đầu tiên là đưa dãy trên về 1 dãy kí tự "quen thuộc hơn"...
def translateMorse(MorseMessage: str):
    result = []
    letters = []
    head = 0
    for i in range(len(MorseMessage)):
        if MorseMessage[i] == '.' or MorseMessage[i] == '-' or MorseMessage[i] == ' ':
            if MorseMessage[i]==' ': # Nếu gặp ' ' thì tức là chuyển sang kí tự mới
                tail = i
                letters.append(MorseMessage[head:tail])
                head = tail+1
            elif i == len(MorseMessage)-1:
                tail = i+1
                letters.append(MorseMessage[head:tail])
        else:
            head = i+1
            letters.append(MorseMessage[i])
    for letter in letters:
        if letter in MorseDictionary:
            for key in MorseDictionary.keys():
                if letter == key:
                    result.append(MorseDictionary.get(key))
                    break
        else:
            result.append(letter)
    return ''.join(result)

doubleMorseMessage = translateMorse(MorseMessage)
print(doubleMorseMessage) # ALLIWANTTOSAYISDOTDOTSPACE...

# Từ việc nhận được một dãy kí tự dài gồm 'DOT', 'SPACE' và 'DASH', đây có thể là mã Morse 2 tầng (phải giải một lần nữa 
# mới nhận được thông điệp). Từ đây nghĩ đến việc tiếp tục giải mã :v
def translateDoubleMorse(doubleMorseMessage: str):
    for word in letterMorseDictionary:
        doubleMorseMessage = doubleMorseMessage.replace(word, letterMorseDictionary[word])
    return doubleMorseMessage

tripleMorseMessage = translateDoubleMorse(doubleMorseMessage)
print(tripleMorseMessage) # ALLIWANTTOSAYIS.. .-.. --- ...- . -.-- --- ..-

finalMessage = translateMorse(tripleMorseMessage)
print(finalMessage) # ALLIWANTTOSAYISILOVEYOU
