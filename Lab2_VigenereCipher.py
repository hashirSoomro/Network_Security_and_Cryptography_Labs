text="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plainText=input("Enter text you want to encrypt: ")
cipherText=input("Enter text you want to decrypt: ") #"GCYCZFMLYLEIM"
keyword="AYUSH"
key=""
kcount=0

#Generating key using keyword
if (len(plainText)>len(keyword)) or (len(plainText)<len(keyword)):
    for i in range(len(plainText)):
        if kcount>=(len(keyword)-1):
            kcount=-1
        key=key+keyword[kcount]
        kcount=kcount+1
else:
    key=keyword

#For encryption of text
def encryption(plainText):
    encrypted_text=""
    for i in range(len(plainText)):#GEEKSFORGEEKS
        temp_text=""               #AYUSHAYUSHAYU
        row=plainText[i]
        col=key[i]
        
        for row_no in range(len(text)):
            if text[row_no]==plainText[i]:
                temp_row_no=row_no
                #print(temp_row_no)
            if text[row_no]==key[i]:
                temp_col_no=row_no
                #print(temp_col_no)
            
        temp_text=text[temp_row_no:]+text[0:temp_row_no]
        #print(temp_text)
        encrypted_text=encrypted_text+temp_text[temp_col_no]
    return ("Encrypted Text: "+encrypted_text)

#for decryption of text
def decryption(cipherText):
    decrypted_text=""
    for i in range(len(cipherText)):#GCYCZFMLYLEIM
        temp_text=""                #AYUSHAYUSHAYU
        row=key[i]
        col=cipherText[i]
        
        for row_no in range(len(text)):
            if text[row_no]==row:
                temp_text=text[row_no:]+text[0:row_no]
                break
        for col_no in range(len(temp_text)):
            if temp_text[col_no]==col:
                decrypted_text=decrypted_text+text[col_no]
                break
    return ("Decrypted Text: "+decrypted_text)

print(encryption(plainText))
print(decryption(cipherText))

