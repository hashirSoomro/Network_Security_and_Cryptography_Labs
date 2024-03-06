import random

#plaintext="HELLO"
def Encryption_OTP(plaintext):
    alphaList=[['A', '000000'], ['B', '000001'], ['C', '000010'], ['D', '000011'], ['E', '000100'], ['F', '000101'], ['G', '000110'], ['H', '000111'],
           ['I', '001000'], ['J', '001001'], ['K', '001010'], ['L', '001011'], ['M', '001100'], ['N', '001101'], ['O', '001110'], ['P', '001111'],
           ['Q', '010000'], ['R', '010001'], ['S', '010010'], ['T', '010011'], ['U', '010100'], ['V', '010101'], ['W', '010110'], ['X', '010111'],
           ['Y', '011000'], ['Z', '011001'], ['a', '011010'], ['b', '011011'], ['c', '011100'], ['d', '011101'], ['e', '011110'], ['f', '011111'],
           ['g', '100000'], ['h', '100001'], ['i', '100010'], ['j', '100011'], ['k', '100100'], ['l', '100101'], ['m', '100110'], ['n', '100111'],
           ['o', '101000'], ['p', '101001'], ['q', '101010'], ['r', '101011'], ['s', '101100'], ['t', '101101'], ['u', '101110'], ['v', '101111'],
           ['w', '110000'], ['x', '110001'], ['y', '110010'], ['z', '110011'], ['A', '110100'], ['B', '110101'], ['C', '110110'], ['D', '110111'],
           ['E', '111000'], ['F', '111001'], ['G', '111010'], ['H', '111011'], ['I', '111100'], ['J', '111101'], ['K', '111110'], ['L', '111111']]
    key=""
    for key_ind in range(len(plaintext)):
        random_int = random.randint(0, 51)
        key=key+alphaList[random_int][0]
    cipher_text=""
    for i in range(len(plaintext)):
        for j in range(len(alphaList)):
            if plaintext[i]==alphaList[j][0]:
                plain_var=alphaList[j][1]
            if key[i]==alphaList[j][0]:
                key_var=alphaList[j][1]
                
        cipher_list=''    
        for k in range(len(plain_var)):
            if plain_var[k]=='0' and key_var[k]=='0':
                cipher_list=cipher_list+'0'
            elif plain_var[k]=='0' and key_var[k]=='1':
                cipher_list=cipher_list+'1'
            elif plain_var[k]=='1' and key_var[k]=='0':
                cipher_list=cipher_list+'1'
            elif plain_var[k]=='1' and key_var[k]=='1':
                cipher_list=cipher_list+'0'
            
        plain_var=''
        key_var=''
        for l in range(len(alphaList)):
            if alphaList[l][1]==cipher_list:
                cipher_text=cipher_text+alphaList[l][0]
                
                
    return cipher_text,key

def Decryption_OTP(ciphertext,key):
    alphaList=[['A', '000000'], ['B', '000001'], ['C', '000010'], ['D', '000011'], ['E', '000100'], ['F', '000101'], ['G', '000110'], ['H', '000111'],
           ['I', '001000'], ['J', '001001'], ['K', '001010'], ['L', '001011'], ['M', '001100'], ['N', '001101'], ['O', '001110'], ['P', '001111'],
           ['Q', '010000'], ['R', '010001'], ['S', '010010'], ['T', '010011'], ['U', '010100'], ['V', '010101'], ['W', '010110'], ['X', '010111'],
           ['Y', '011000'], ['Z', '011001'], ['a', '011010'], ['b', '011011'], ['c', '011100'], ['d', '011101'], ['e', '011110'], ['f', '011111'],
           ['g', '100000'], ['h', '100001'], ['i', '100010'], ['j', '100011'], ['k', '100100'], ['l', '100101'], ['m', '100110'], ['n', '100111'],
           ['o', '101000'], ['p', '101001'], ['q', '101010'], ['r', '101011'], ['s', '101100'], ['t', '101101'], ['u', '101110'], ['v', '101111'],
           ['w', '110000'], ['x', '110001'], ['y', '110010'], ['z', '110011'], ['A', '110100'], ['B', '110101'], ['C', '110110'], ['D', '110111'],
           ['E', '111000'], ['F', '111001'], ['G', '111010'], ['H', '111011'], ['I', '111100'], ['J', '111101'], ['K', '111110'], ['L', '111111']]
    plain_text=""
    for i in range(len(ciphertext)):
        for j in range(len(alphaList)):
            if ciphertext[i]==alphaList[j][0]:
                cipher_var=alphaList[j][1]
            if key[i]==alphaList[j][0]:
                key_var=alphaList[j][1]
                
        plain_list=''    
        for k in range(len(cipher_var)):
            if cipher_var[k]=='0' and key_var[k]=='0':
                plain_list=plain_list+'0'
            elif cipher_var[k]=='0' and key_var[k]=='1':
                plain_list=plain_list+'1'
            elif cipher_var[k]=='1' and key_var[k]=='0':
                plain_list=plain_list+'1'
            elif cipher_var[k]=='1' and key_var[k]=='1':
                plain_list=plain_list+'0'
            
        cipher_var=''
        key_var=''
        for l in range(len(alphaList)):
            if alphaList[l][1]==plain_list:
                plain_text=plain_text+alphaList[l][0]
    return plain_text          
        
    
