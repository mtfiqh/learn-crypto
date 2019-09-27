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

while (1):
    print('1.   Load text from file [Encrypt]')
    print('2.   Input text from keyboard [Encrypt]')
    choice = input('Choice: ')
    if choice == '1':
        try:
            file_name = input("Your file name, include extension (ex: file.txt): ")
            file = open(file_name, 'r')
            plainText = file.read()
            file.close()
            if plainText:
                break
            else:
                print('The file is empty!')
                print('')
        except Exception as e:
            print('error: ', e)
            print('')

    elif choice == '2':
        plainText = input("Enter text to encrypt: ")
        break
    else:
        print('Your choice is wrong !')
    

key = input("Enter the key: ")
# removing spaces in key
key = key.replace(' ','')
print('')
print('')
print('Plain Text   = ', plainText)
print('Key          =', key)
print('=============================')
encrypted = (encrypt(plainText, key))
print('Encrypt Text = ', encrypted)
decrypted = decrypt(encrypted, key)
print('Decrypt Text = ',decrypted)

# save file
file = open('Vigenere Encrypt Text.txt', "w+")
file.write(encrypted)
file.close()
print('Encrypted text saved in "Vigenere Encrypt Text.txt"')