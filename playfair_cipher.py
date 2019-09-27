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
    # return[
    #     newKey[:5],
    #     newKey[5:10],
    #     newKey[10:15],
    #     newKey[15:20],
    #     newKey[20:25]
    # ]

# huruf sama disisipkan 'X'
# huruf J diganti dengan I
# Jika huruf berjumlah ganjil sisipkan Z
def splitText(text):
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

print(splitText('JJAWA TENGAH'))
def encrypt(text, key):
    splitText = splitText(text)
    key = createKey(key)

    # jika sama kolom

    