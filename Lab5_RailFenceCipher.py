import math

##plainText="GoodMorning"
##cipherText="GMioonorgdn"
##depth=4

def Encryption_RailFence(plainText,depth):
    row_len=math.ceil(len(plainText)/depth)
    while len(plainText)<(row_len*depth):
        plainText=plainText+"x"
    count_key=0
    cipherMatrix={}
    cipherText=''
    for i in range(1,depth+1):
        cipherMatrix[i]=[]

    for i in range(0,len(plainText),depth):
        for key, value in cipherMatrix.items():
            count_key=count_key+1
            if count_key<=len(plainText):
                value.append(plainText[count_key-1])
    for key, value in cipherMatrix.items():
        for i in range(len(value)):
            cipherText=cipherText+value[i]
    return cipherText

def Decryption_RailFence(cipherText,depth):
    col_len=math.ceil(len(cipherText)/depth)
    count_key=0
    index_count=0
    plainText=''

    for i in range(0,col_len+1):
        index_count=i
        for j in range(depth):
            count_key=count_key+1
            if index_count<(len(cipherText)) and count_key<=len(cipherText):
                plainText=plainText+cipherText[index_count]
            index_count=index_count+col_len
    return plainText

