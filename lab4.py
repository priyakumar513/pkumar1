def cencrypt(word, n):
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
print (cencrypt("A.B.A",3))

           
        

