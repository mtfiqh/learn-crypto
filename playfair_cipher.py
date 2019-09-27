# Muhammad Taufiq Hidayat
# 14116162
# playfair_cipher


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

print(encrypt('INSTRUMENTS', 'MONARCHY'))