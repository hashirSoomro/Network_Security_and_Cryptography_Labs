def encryption_C(string_user):
    enc="DEFGHIJKLMNOPQRSTUVWXYZABCdefghijklmnopqrstuvwxyzabc ?!.,;:"
    dec="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ?!.,;:"
    #string_user=input("Enter the message to encrypt:")#HELLO
    enc_str=""
    for i in range(len(string_user)):
        for j in range(len(enc)):
            if string_user[i]==dec[j]:
                enc_str=enc_str+enc[j]
    return enc_str

def decryption_C(string_user):
    enc="DEFGHIJKLMNOPQRSTUVWXYZABCdefghijklmnopqrstuvwxyzabc ?!.,;:"
    dec="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ?!.,;:"
    #string_user=input("Enter the message to decrypt:")#HELLO
    dec_str=""
    for i in range(len(string_user)):
        for j in range(len(dec)):
            if string_user[i]==enc[j]:
                dec_str=dec_str+dec[j]
    return dec_str

