import math

plainText="GoodMorning"
cipherText="GoMrigodonn"
depth=2

def Encryption_RailFence(plainText,depth):
    count_key=0
    cipherMatrix={}
    cipherText=''
    for i in range(1,depth+1):
        cipherMatrix[i]=[]

    for i in range(0,len(plainText),depth):
        for key, value in cipherMatrix.items():
            count_key=count_key+1
            print(count_key)
            if count_key<=len(plainText):
                value.append(plainText[count_key-1])
    for key, value in cipherMatrix.items():
        for i in range(len(value)):
            cipherText=cipherText+value[i]
    return cipherText

##def Decryption_RailFence(cipherText,depth):
##    col_len=math.ceil(len(cipherText/depth))
##    count_key=0
##    plainMatrix={}
##    plainText=''
##    for i in range(1,depth+1):
##        plainMatrix[i]=[]
##
##    for i in range(0,len(cipherText),depth):
##        for key, value in plainMatrix.items():
##            
##            count_key=count_key+1
##
##            if count_key<=len(cipherText):
##                value.append(cipherText[count_key-1])
##
##                
##    for key, value in plainMatrix.items():
##        for i in range(len(value)):
##            plainText=plainText+value[i]
##    return plainText
    
print(Decryption_RailFence(cipherText,depth))
