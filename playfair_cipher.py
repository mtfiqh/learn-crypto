# Muhammad Taufiq Hidayat
# 14116162
# playfair_cipher.py
# Repository : github.com/mtfiqh/learn-crypto

# ====================================================== START CORE ====================================================
def createKey(keyText):
    beginKey=['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    newKey=[]
    for c in keyText:
        if c in beginKey:
            newKey.append(c)
            beginKey.remove(c)
    newKey=newKey+beginKey
    return newKey

def createMatrixKey(keyText):
    newKey = createKey(keyText)
    return[
        newKey[:5],
        newKey[5:10],
        newKey[10:15],
        newKey[15:20],
        newKey[20:25]
    ]
# huruf sama disisipkan 'X'
# huruf J diganti dengan I
# Jika huruf berjumlah ganjil sisipkan Z
def splitterText(text):
    text = text.replace(" ","")
    idx = 0
    split=[]
    while idx in range (len(text)):
        temp = text[idx]
        if text[idx] =='J':
            temp='I'
        if idx+1 != (len(text)) and text[idx] == text[idx+1]:
            split.append(temp+'X')
            idx=idx+1
        elif idx==(len(text)-1):
            split.append(temp+'Z')
            idx=idx+1
        else:
            temp2 = text[idx+1]
            if text[idx+1] == 'J':
                temp2 = 'I'
            split.append(temp+text[idx+1])
            idx=idx+2
    
    return split


def encrypt(text, key):
    splitText = splitterText(text)
    key = createKey(key)
    matrixKey = createMatrixKey(key)

    encrypt=""
    for st in splitText:
        barisSatu = key.index(st[0])//5
        kolomSatu = key.index(st[0])%5

        barisDua = key.index(st[1])//5
        kolomDua = key.index(st[1])%5

        # jika sama kolom
        # maka, diganti dengan bawahnya (baris + 1)
        # jika paling bawah, maka ambil paling atas (baris ke 0)
        if kolomSatu == kolomDua:
            if barisSatu == 4:
                encrypt = encrypt + matrixKey[0][kolomSatu]
            else:
                encrypt = encrypt + matrixKey[barisSatu+1][kolomSatu]
            if barisDua == 4:
                encrypt = encrypt + matrixKey[0][kolomDua]
            else:
                encrypt = encrypt + matrixKey[barisDua+1][kolomDua]
        
        # Jika sama baris
        # maka, diganti dengan sebelah kanannya (kolom + 1)
        # jika paling kanan, maka ambil paling kiri (kolom ke 0)
        elif barisSatu == barisDua:
            if kolomSatu == 4:
                encrypt = encrypt + matrixKey[barisSatu][0]
            else:
                encrypt = encrypt + matrixKey[barisSatu][kolomSatu+1]
            if kolomDua == 4:
                encrypt = encrypt + matrixKey[barisDua][0]
            else:
                encrypt = encrypt + matrixKey[barisDua][kolomDua+1]
        
        # jika baris dan kolom tidak sama
        # maka kolom ditukar
        else:
            encrypt = encrypt + matrixKey[barisSatu][kolomDua] + matrixKey[barisDua][kolomSatu]
        
    return encrypt

def decrypt(text, key):
    splitText = splitterText(text)
    key = createKey(key)
    matrixKey = createMatrixKey(key)

    decrypt=""
    for st in splitText:
        barisSatu = key.index(st[0])//5
        kolomSatu = key.index(st[0])%5

        barisDua = key.index(st[1])//5
        kolomDua = key.index(st[1])%5

        # jika sama kolom
        # maka, diganti dengan atasnya (baris - 1)
        # jika paling atas, maka ambil paling bawah (baris ke 4)
        if kolomSatu == kolomDua:
            if barisSatu == 0:
                decrypt = decrypt + matrixKey[4][kolomSatu]
            else:
                decrypt = decrypt + matrixKey[barisSatu-1][kolomSatu]
            if barisDua == 0:
                decrypt = decrypt + matrixKey[4][kolomDua]
            else:
                decrypt = decrypt + matrixKey[barisDua-1][kolomDua]
        
        # Jika sama baris
        # maka, diganti dengan sebelah kirinya (kolom - 1)
        # jika paling kiri, maka ambil paling kanan (kolom ke 4)
        elif barisSatu == barisDua:
            if kolomSatu == 0:
                decrypt = decrypt + matrixKey[barisSatu][4]
            else:
                decrypt = decrypt + matrixKey[barisSatu][kolomSatu-1]
            if kolomDua == 0:
                decrypt = decrypt + matrixKey[barisDua][4]
            else:
                decrypt = decrypt + matrixKey[barisDua][kolomDua-1]
        
        # jika baris dan kolom tidak sama
        # maka kolom ditukar
        else:
            decrypt = decrypt + matrixKey[barisSatu][kolomDua] + matrixKey[barisDua][kolomSatu]
        
    return decrypt

# ============================================== END CORE =============================================


def saveFile(nama, isi):
    # save file
    file = open(nama+'.txt', "w+")
    file.write(isi)
    file.close()
    print('Result saved in ', nama+'.txt')

def encryptFromFile():
    try:
        file_name = input("Your file name, include extension (ex: file.txt): ")
        file = open(file_name, 'r')
        text = file.read()
        file.close()
        if text:
            print('file loaded!')
        else:
            print('The file is empty!')
            print('')
            return None
    except Exception as e:
        print('error: ', e)
        print('')
        return None
    key = input('Key: ')
    encrypted = encrypt(text,key)
    print('\nText   :', text)
    print('Key  :',key)
    print('Encrypted    : ', encrypted)
    saveFile('playfair_encrypted', encrypted)

def encryptFromKeyboard():
    text = input('Text  : ')
    key = input('Key    : ')
    encrypted = encrypt(text,key)
    print('\n===============RESULT==============')
    print('\nText       :',text)
    print('Key          : ',key)
    print('Encrypted    : ',encrypted)
    saveFile('playfair_encrypted', encrypted)
    print('\n')

def decryptFromFile():
    try:
        file_name = input("Your file name, include extension (ex: file.txt): ")
        file = open(file_name, 'r')
        text = file.read()
        file.close()
        if text:
            print('file loaded!')
        else:
            print('The file is empty!')
            print('')
            return None
    except Exception as e:
        print('error: ', e)
        print('')
        return None
    key = input('Key: ')
    decrypted = decrypt(text,key)
    print('\nText   :', text)
    print('Key  :',key)
    print('Decrypted    : ', decrypted)
    saveFile('playfair_decrypted', decrypted)

def decryptFromKeyboard():
    text = input('Text  : ')
    key = input('Key    : ')
    decrypted = decrypt(text,key)
    print('\n===============RESULT==============')
    print('\nText       :',text)
    print('Key          : ',key)
    print('Decrypted    : ',decrypted)
    saveFile('playfair_decrypted', decrypted)
    print('\n')

while(1):
    print('=========== github.com/mtfiqh/learn-crypto =============')
    print('Playfair Cipher !!')
    print('WARNING!! ONLY ACCEPT UPPERCASE CHAR')
    print('1.   [Encrypt] text from file')
    print('2.   [Encrypt] text from keyboard')
    print('3.   [Decrypt] text from file')
    print('4.   [Decrypt] text from keyboard')
    print('5.   Exit')
    choice = input('Choice   : ')
    if(choice == '1'):
        encryptFromFile()
    elif(choice == '2'):
        encryptFromKeyboard()
    elif(choice == '3'):
        decryptFromFile()
    elif(choice == '4'):
        decryptFromKeyboard()
    elif(choice == '5'):
        exit()
        break
    print('\n\n')
