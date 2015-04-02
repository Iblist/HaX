"""
Takes a file name as an argument, opens file and saves as string to a variable.
Splits string into numbers.  Takes groups of three, adds them together. 
Finds the lowest sum, sets as the the limit for password brute forcing.
"""
def decrypt():
    file = open('encrypted.txt')
    fileString = str(file.read())
    file.close()
    #Divides and cleans string
    fileString = fileString.replace('\n', '').split('.')
    fileString = [(i) for i in fileString if i != '']
    fileString = [int(i) for i in fileString]

    a, b, c = 0, 1, 2

    length = (int(len(fileString)/3))
    #Adds groups of three.
    shrunkString = []
    for n in range(0, length):
        shrunkString.append(fileString[a] + fileString[b] + fileString[c])
        a += 3
        b += 3
        c += 3

    limit = min(shrunkString)

    x = limit - 1

    check = False
    clearText = []

    while x > 0 and check == False:
        clearText = []
        for n in shrunkString:
            clearText.append(chr(n - x))
        for i in range (0, len(clearText)):
            if clearText[i] == 't':
                if clearText[i+1] == 'h':
                    if clearText[i+2] == 'e':
                        check = True
        x -= 1
    x = str(x)
    clearText = ''.join(clearText)
    f = open('decrypted.txt', 'w')
    f.write('*' * 20)
    f.write('\n' * 2)
    f.write('Key is: ')
    f.write(x)
    f.write('\n' * 2)
    f.write('*' * 20)
    f.write('\n' * 2)
    f.write(clearText)
