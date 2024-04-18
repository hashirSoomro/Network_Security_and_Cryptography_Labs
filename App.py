import streamlit as st
from Lab1_CaeserCipher import encryption_C,decryption_C
from Lab2_VigenereCipher import encryption,decryption
from Lab3_PolyAlphabeticCiphers import encryption_P,decryption_P
from Lab4_OneTimePadCipher import Encryption_OTP,Decryption_OTP
from Lab5_RailFenceCipher import Encryption_RailFence,Decryption_RailFence

def caeser_cipher():
    st.title("Caeser Cipher")
    option = st.radio("Select an option:", ("Encrypt", "Decrypt"))
    if option == "Encrypt":
        string_user = st.text_input("Enter the message to encrypt:")
        if st.button("Encrypt"):
            enc_str=encryption_C(string_user)
            st.write("Here is your encrypted message:", enc_str)
            
    elif option == "Decrypt":
        string_user = st.text_input("Enter the message to decrypt:")
        if st.button("Decrypt"):
            dec_str=decryption_C(string_user)
            st.write("Here is your decrypted message:", dec_str)

def vigenere_cipher():
    st.title("Vigenere Cipher")
    option = st.radio("Select an option:", ("Encrypt", "Decrypt"))
    if option == "Encrypt":
        plainText = st.text_input("Enter text you want to encrypt:")
        keyword = st.text_input("Enter the keyword:")
        if st.button("Encrypt"):
            enc_text = encryption(plainText, keyword)
            st.write("Encrypted Text:", enc_text)
    elif option == "Decrypt":
        cipherText = st.text_input("Enter text you want to decrypt:")
        keyword = st.text_input("Enter the keyword:")
        if st.button("Decrypt"):
            dec_text = decryption(cipherText, keyword)
            st.write("Decrypted Text:", dec_text)

def polyAlphabetic_cipher():
    st.title("PolyAlphabetic Cipher")
    option = st.radio("Select an option:", ("Encrypt", "Decrypt"))
    if option == "Encrypt":
        string_user = st.text_input("Enter text you want to encrypt:")
        if st.button("Encrypt"):
            enc_text = encryption_P(string_user)
            st.write("Encrypted Text:", enc_text)
    elif option == "Decrypt":
        string_user = st.text_input("Enter text you want to decrypt:")
        if st.button("Decrypt"):
            dec_text = decryption_P(string_user)
            st.write("Decrypted Text:", dec_text)

def OneTimePad_cipher():
    st.title("One Time Pad Cipher")
    option = st.radio("Select an option:", ("Encrypt", "Decrypt"))
    if option == "Encrypt":
        string_user = st.text_input("Enter text you want to encrypt:")
        if st.button("Encrypt"):
            enc_text,key = Encryption_OTP(string_user)
            st.write("Encrypted Text:", enc_text)
            st.write("Randomly Generated Key:", key)
    elif option == "Decrypt":
        string_user = st.text_input("Enter text you want to decrypt:")
        key = st.text_input("Enter the key:")
        if st.button("Decrypt"):
            dec_text = Decryption_OTP(string_user,key)
            st.write("Decrypted Text:", dec_text)

def RailFence_cipher():
    st.title("Rail Fence Cipher")
    option = st.radio("Select an option:", ("Encrypt", "Decrypt"))
    if option == "Encrypt":
        string_user = st.text_input("Enter text you want to encrypt:")
        depth=st.number_input('Enter Depth:', min_value=1, value=5, step=1)
        if st.button("Encrypt"):
            cipherText = Encryption_RailFence(string_user,depth)
            st.text(cipherText)
            st.write("Depth:", depth)
    elif option == "Decrypt":
        string_user = st.text_area("Enter text you want to decrypt:")
        depth=st.number_input('Enter Depth:', min_value=1, value=5, step=1)
        if st.button("Decrypt"):
            dec_text = Decryption_RailFence(string_user,depth)
            st.write("Decrypted Text:", dec_text)
            st.write("Depth:", depth)

def main():
    st.sidebar.title("Select Cipher")
    selected_cipher = st.sidebar.radio("", ("Caeser Cipher", "Vigenere Cipher","PolyAlphabetic Cipher","One Time Pad Cipher","Rail Fence Cipher"))

    if selected_cipher == "Caeser Cipher":
        caeser_cipher()
    elif selected_cipher == "Vigenere Cipher":
        vigenere_cipher()
    elif selected_cipher == "PolyAlphabetic Cipher":
        polyAlphabetic_cipher()
    elif selected_cipher == "One Time Pad Cipher":
        OneTimePad_cipher()
    elif selected_cipher == "Rail Fence Cipher":
        RailFence_cipher()

if __name__ == "__main__":
    main()
