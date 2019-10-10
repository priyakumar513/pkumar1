"""Encryption function using the caesar cipher to encode a word."""
def c_encrypt(word, n):
    word = word.upper() #convert inputted word to uppercase 
    my_string=''
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for character in word:
         i=alpha.find(character)
         if (i == -1):
             my_string+=character #exempt punctuation and white space
         else: 
             my_string+=(alpha[(i+n)%26])
    return my_string
#print (c_encrypt('EFDSZQUJPO FYBNQMF',-25))
"""Decryption function decoding a word that was encoded using the caesar cipher."""
def c_decrypt(my_string,n):
    my_string = my_string.upper()
    decrypted_string=''
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for character in my_string:
         i=alpha.find(character)
         if (i == -1):
             decrypted_string+=character
         else: 
             decrypted_string+=(alpha[(i-n)%26])
    return decrypted_string
#print (c_decrypt('EFDSZQUJPO FYBNQMF',-25))
"""Encryption function encoding a word using the vigenere cipher."""
def vig_encrypt(plaintext, key):
    plaintext=plaintext.upper()
    key=key.upper()
    counter=0 
    my_answer=''
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for character in plaintext: 
        index=alpha.find(character)
        if (index == -1):
            my_answer+=character
        else:
            offset=alpha.find(key[counter% len(key)])
            #print(offset)
            counter+=1
            #print(counter)
            final_index = index+offset
            my_answer+=alpha[final_index%26]
    return my_answer 
#print(vig_encrypt(".CAESAR", "BACON"))
"""Decryption function decoding a word that was encoded using the vigenere cipher."""
def vig_decrypt(my_answer,key):
    my_answer = my_answer.upper()
    key=key.upper()
    counter=0 
    decrypted_answer =''
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for character in my_answer: 
        index=alpha.find(character)
        if (index == -1):
            decrypted_answer+=character
        else:
            offset=alpha.find(key[counter% len(key)])
            #print(offset)
            counter+=1
            #print(counter)
            final_index = index-offset
            decrypted_answer+=alpha[final_index%26]
    return decrypted_answer 
#print(vig_decrypt(".daggns","BACON"))
            
            


