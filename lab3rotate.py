def rotate(c,n): 
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i=alpha.find(c)
    i+=n
    return(alpha[i%26])
    
rotate("C",7)

