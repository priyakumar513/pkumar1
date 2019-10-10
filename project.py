def c_encrypt(word, n):
    word = word.upper()
    my_string=''
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for character in word:
         i=alpha.find(character)
         if (i == -1):
             my_string+=character
         else: 
             my_string+=(alpha[(i+n)%26])
    return my_string
print (c_encrypt("c.eas.ar",3))
def c_decrypt(word,n):
    word = word.upper()
    my_string=''
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for character in word:
         i=alpha.find(character)
         if (i == -1):
             my_string+=character
         else: 
             my_string+=(alpha[(i+n)%26])
    return my_string
print (c_decrypt("c.eas.ar",3))

           
        

