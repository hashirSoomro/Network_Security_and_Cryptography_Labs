# Welcome to Caeser Cipher
print("Welcome to Caeser Cipher")

#decrypted/normal key and encrypted key is defined
dec="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
enc="DEFGHIJKLMNOPQRSTUVWXYZABCdefghijklmnopqrstuvwxyzabc"

#taking input from user
print("Do you want to enrcrypt or decrypt the key?")
ask_user=input("For encryption enter E and For decryption enter D:")

if ask_user=='E' or ask_user=='e':
    string_user=input("Enter the message to encrypt:")#HELLO
    enc_str=""
    for i in range(len(string_user)):
        for j in range(len(enc)):
            if string_user[i]==dec[j]:
                enc_str=enc_str+enc[j]
    print("Here is your encrypted message: "+enc_str)
                
elif ask_user=='D' or ask_user=='d':
    string_user=input("Enter the message to decrypt:")#HELLO
    dec_str=""
    for i in range(len(string_user)):
        for j in range(len(dec)):
            if string_user[i]==enc[j]:
                dec_str=dec_str+dec[j]
    print("Here is your encrypted message: "+dec_str)
else:
    print("Invalid input!Please answer in E or D")
