
def encryption_P(string_user):
    dec= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ?!.,;:"
    enc=["ASDFGHJKLPOIUYTREWQZXCVBNMasdfghjklpoiuytrewqzxcvbnm ?!.,;:",
         "QAZWSXEDCRFVTGBYHNUPJMIKOLqazwsxedcrfvtgbyhnupjmikol ?!.,;:",
         "ZXCVBNMKIOPLUJHYTGFREDSWQAzxcvbnmkioplujhytgfredswqa ?!.,;:"]
    len_count=0
    enc_str=""
    for i in range(len(string_user)):
        for j in range(len(enc[len_count])):
            if string_user[i]==dec[j]:
                enc_str=enc_str+enc[len_count][j]
                break
        len_count=len_count+1
        if len_count==3:
            len_count=0
    return enc_str

def decryption_P(string_user):
    dec= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ?!.,;:"
    enc=["ASDFGHJKLPOIUYTREWQZXCVBNMasdfghjklpoiuytrewqzxcvbnm ?!.,;:",
         "QAZWSXEDCRFVTGBYHNUPJMIKOLqazwsxedcrfvtgbyhnupjmikol ?!.,;:",
         "ZXCVBNMKIOPLUJHYTGFREDSWQAzxcvbnmkioplujhytgfredswqa ?!.,;:"]
    len_count=0
    dec_str=""
    for i in range(len(string_user)):
        for j in range(len(dec)):
            if string_user[i]==enc[len_count][j]:
                dec_str=dec_str+dec[j]
                break
        len_count=len_count+1
        if len_count==3:
            len_count=0
    return dec_str
