
# DECODE ERROR, TERMINAL CRASH

from PIL import Image

def enc(img, text):
    newImg = img.copy()

    binaryText = []
    # convert text data to binary
    for i in text:
        binaryText.append(format(ord(i), '08b'))
    print(binaryText)
    # initiate pixels x and y of images
    (x, y, s) = (0, 0, 0)
    (pixelX, pixelY) = (newImg.size[0], newImg.size[1])
    newPixels = list(newImg.getpixel((x,y)))
    # looping for each binary in data
    for i in binaryText:
        for j in i:
            if(j=='1'):
                if(newImg.getpixel((x, y))[s]%2==0):
                    newPixels[s] = newImg.getpixel((x, y))[s]+1
                else:
                    newPixels[s] = newImg.getpixel((x,y))[s]
            elif(j=='0'):
                if(newImg.getpixel((x,y))[s]%2!=0):
                    newPixels[s] = newImg.getpixel((x, y))[s]-1
                else:
                    newPixels[s] = newImg.getpixel((x,y))[s]
            newImg.putpixel((x,y), tuple(newPixels))                        
            s+=1
            if(s>2):
                s=0
                x+=1
                newPixels = list(newImg.getpixel((x,y)))

            if(x>pixelX-1):
                x=0
                y+=1
                       
    newImgName = input("Enter the name of new image(without extension): ")
    newImg.save(newImgName+'.png')
    print('image saved as ',newImgName+'.png')


def dec(img):
    data = '' 
    imgData = list(img.getdata())
    print(imgData[:8])
    # ambil pixels per 8
    # pixels=[0, 0, 0, 0, 0, 0, 0, 0]
    s=0
    binstr=''
    data=''

    for i in imgData:
        for j in i:
            if(j%2==0):
                binstr+='0'
            else:
                binstr+='1'
            s+=1
            if(s>=8):
                # print(binstr)
                s=0
                data+=chr(int(binstr, 2))
                binstr=''

    return data
# Main Function         
def main(): 
    print("Steganography\nMuhammad Taufiq Hidayat\t14116162\nIsnedi Chandra Kusuma\t14116136\nYohanes Eloi P Manik\t14116059")
    a = int(input("1. Encode\n2. Decode\nChoice:\t"))
    imgName = input('Name file (with extension ex: myImage.jpg): ')
    img = Image.open(imgName, 'r')
    if (a == 1):
        data = input('String to encode: ')
        newImg = img.copy()
        enc(newImg, data)

    elif (a == 2): 
        print("Decoded word- ")
        print(dec(img)) 
    else: 
        raise Exception("Enter correct input") 
          
# Driver Code 
if __name__ == '__main__' : 
    # Calling main function 
    main() 