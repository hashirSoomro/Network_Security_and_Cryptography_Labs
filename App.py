import streamlit as st
from Lab1_CaeserCipher import encryption_C,decryption_C
from Lab2_VigenereCipher import encryption,decryption
from Lab3_PolyAlphabeticCiphers import encryption_P,decryption_P

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


def main():
    st.sidebar.title("Select Cipher")
    selected_cipher = st.sidebar.radio("", ("Caeser Cipher", "Vigenere Cipher","PolyAlphabetic Cipher"))

    if selected_cipher == "Caeser Cipher":
        caeser_cipher()
    elif selected_cipher == "Vigenere Cipher":
        vigenere_cipher()
    elif selected_cipher == "PolyAlphabetic Cipher":
        polyAlphabetic_cipher()

if __name__ == "__main__":
    main()
