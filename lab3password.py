def password1(s1,s2): 
    return(s1 + "_" + s2)
    
print(password1("yellow","daisy"))

def password2(s1,s2,n):
    return str(n) + s1 + s2 + str(n)
    
print(password2("yellow", "daisy", 6))

