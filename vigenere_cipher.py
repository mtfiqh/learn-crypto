# Muhammad Taufiq Hidayat
# 14116162
# mtfiqh[at]gmail[dot]com

# --------------------------------CORE-------------------------------
def charToDecimal(char):
    return ord(char)

def decimalToChar(decimal):
    return chr(decimal)

def charKeyToDecimal(charKey):
    decimalKey = ord(charKey)
    if decimalKey>=65 and decimalKey<=90:
        decimalKey = decimalKey - 65
    elif decimalKey>=97 and decimalKey<=122:
        decimalKey = decimalKey - 97
    return decimalKey

def encrypt(plainText, key):
    key = key.replace(' ','')
    idxText = 0
    encryptText = ""
    idxKey  = 0
    for idxText in range (len(plainText)):
        if plainText[idxText]==' ':
            encryptText=encryptText+' '
            continue
        
        decimalText = charToDecimal(plainText[idxText])
        
        decimalCipher = decimalText + charKeyToDecimal(key[idxKey])

        if decimalText >= 65 and decimalText <= 90:
            if decimalCipher > 90 :
                decimalCipher = decimalCipher - 26
        elif decimalText >= 97 and decimalText <= 122:
            if decimalCipher > 122 :
                decimalCipher = decimalCipher - 26

        encryptText = encryptText + decimalToChar(decimalCipher)
        idxKey = idxKey + 1
        if idxKey >= len(key):
            idxKey = 0
    
    return encryptText

def decrypt(encryptText, key):
    key = key.replace(' ','')
    idxEncrypt = 0
    decryptText = ""
    idxKey = 0

    for idxEncrypt in range (len(encryptText)):
        if encryptText[idxEncrypt]==' ':
            decryptText = decryptText + ' '
            continue
        decimalEncrypt = charToDecimal(encryptText[idxEncrypt])
        decimalDecrypt = decimalEncrypt - charKeyToDecimal(key[idxKey])
        if decimalEncrypt >= 65 and decimalEncrypt <= 90:
            if decimalDecrypt < 65 :
                decimalDecrypt = decimalDecrypt + 26
        elif decimalEncrypt >= 97 and decimalEncrypt <= 122:
            if decimalDecrypt < 97 :
                decimalDecrypt = decimalDecrypt + 26

        decryptText = decryptText + decimalToChar(decimalDecrypt)
        idxKey = idxKey + 1
        if idxKey >= len(key):
            idxKey = 0
    
    return decryptText

# ---------------------------------- END CORE ---------------------------
def saveFile(nama, isi):
    # save file
    file = open(nama+'.txt', "w+")
    file.write(isi)
    file.close()
    print('saved in ',nama,'.txt"')

def encryptFromFile():
    try:
        file_name = input("Your file name, include extension (ex: file.txt): ")
        file = open(file_name, 'r')
        plainText = file.read()
        file.close()
        if plainText:
            print('Loaded')
        else:
            print('The file is empty!')
            print('')
            return None
    except Exception as e:
        print('error: ', e)
        print('')
        return None
    key = input('Key  : ')
    encrypted = encrypt(plainText, key)
    print('Text :', plainText)
    print('Encrypted    :', encrypted)
    saveFile('Vigenere_encrypted', encrypted)

def encryptFromText():
    text = input('Text  : ')
    key = input('Key : ')
    encrypted = encrypt(text, key)
    print('Encrypted    :', encrypted)
    saveFile('Vigenere_encrypted', encrypted)

def decryptFromFile():
    try:
        file_name = input("Your file name, include extension (ex: file.txt): ")
        file = open(file_name, 'r')
        plainText = file.read()
        file.close()
        if plainText:
            print('Loaded')
        else:
            print('The file is empty!')
            print('')
            return None
    except Exception as e:
        print('error: ', e)
        print('')
        return None
    key = input('Key  : ')
    decrypted = decrypt(plainText, key)
    print('Text :', plainText)
    print('Decrypted    :', decrypted)
    saveFile('Vigenere_decrypted', decrypted)

def decryptFromText():
    text = input('Text  : ')
    key = input('Key : ')
    decrypted = decrypt(text, key)
    print('Decrypted    :', decrypted)
    saveFile('Vigenere_decrypted', decrypted)

while(1):
    print('Vigenere Cipher!! -- github.com/mtfiqh/learn-crypto --')
    print('1.   Load text from file [Encrypt]')
    print('2.   Input text from keyboard [Encrypt]')
    print('3.   Input text from file [Decrypt]')
    print('4.   Input text from keyboard [Decrypt]')
    print('5.   Exit')
    choice = input('Choice: ')
    if choice == '1':
        encryptFromFile()
    elif choice == '2':
        encryptFromText()
    elif choice == '3':
        decryptFromFile()
    elif choice == '4':
        decryptFromText()
    else:
        print('Your choice is wrong !')
    print('\n\n')
