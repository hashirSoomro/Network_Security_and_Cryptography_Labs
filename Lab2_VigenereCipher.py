#For encryption of text
def encryption(plainText,keyword):
    text= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text1="abcdefghijklmnopqrstuvwxyz"
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
    
    encrypted_text=""
    for i in range(len(plainText)):#GEEKSFORGEEKS
        temp_text=""               
        temp_text1=""
        temp_row_no=-1
        temp_row_no1=-1
        temp_col_no=-1
        temp_col_no1=-1
                                           
        for row_no in range(len(text)):    
            if text[row_no]==plainText[i]: 
                temp_row_no=row_no
                
            elif text1[row_no]==plainText[i]:
                temp_row_no1=row_no
                
            if text[row_no]==key[i]:
                temp_col_no=row_no
                
            elif text1[row_no]==key[i]:
                temp_col_no1=row_no
                
        if temp_row_no != -1 and temp_col_no !=-1:
            temp_text=text[temp_row_no:]+text[0:temp_row_no]
            encrypted_text=encrypted_text+temp_text[temp_col_no]
            
        elif temp_row_no != -1 and temp_col_no1 !=-1:
            temp_text=text[temp_row_no:]+text[0:temp_row_no]
            encrypted_text=encrypted_text+temp_text[temp_col_no1]
            
        elif temp_row_no1 != -1 and temp_col_no !=-1:
            temp_text1=text1[temp_row_no1:]+text1[0:temp_row_no1]
            encrypted_text=encrypted_text+temp_text1[temp_col_no]

        elif temp_row_no1 != -1 and temp_col_no1 !=-1:
            temp_text1=text1[temp_row_no1:]+text1[0:temp_row_no1]
            encrypted_text=encrypted_text+temp_text1[temp_col_no1]
    return ("Encrypted Text: "+encrypted_text)

#for decryption of text
def decryption(cipherText,keyword):
    text= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text1="abcdefghijklmnopqrstuvwxyz"
    key=""
    kcount=0
    #Generating key using keyword
    if (len(cipherText)>len(keyword)) or (len(cipherText)<len(keyword)):
        for i in range(len(cipherText)):
            if kcount>=(len(keyword)-1):
                kcount=-1
            key=key+keyword[kcount]
            kcount=kcount+1
    else:
        key=keyword
    decrypted_text=""
    for i in range(len(cipherText)):#GCYCZFMLYLEIM
        temp_text=""                #gcyczfmlyleim
        temp_text1=""
        
        for row_no in range(len(text)):
            if text[row_no]==key[i] and cipherText[i] in text:#A==A and G 
                temp_text=text[row_no:]+text[0:row_no]
                break

            elif text[row_no]==key[i] and cipherText[i] in text1: 
                temp_text1=text1[row_no:]+text1[0:row_no]
                break
                
            elif text1[row_no]==key[i] and cipherText[i] in text:#a==a
                temp_text=text[row_no:]+text[0:row_no]
                break
            
            elif text1[row_no]==key[i] and cipherText[i] in text1:#a==a
                temp_text1=text1[row_no:]+text1[0:row_no]
                break
            
        if temp_text!="":
            for col_no in range(len(temp_text)):
                if temp_text[col_no]==cipherText[i]: #G==g
                    decrypted_text=decrypted_text+text[col_no]
                    break
        if temp_text1!="":
            for col_no in range(len(temp_text1)):
                if temp_text1[col_no]==cipherText[i]:
                    decrypted_text=decrypted_text+text1[col_no]
                    print(decrypted_text)
                    break
    return ("Decrypted Text: "+decrypted_text)

