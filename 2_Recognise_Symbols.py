# This is the code for making a file which holds all the symbols and variables in the code.
# This is part of the white.py code as an asm file with no white spaces is required for this code.
def check(z):
    if z[0] == '@':
        if z[1].isalpha():
            return True
    elif z[0] == '(':
        return True
        
# I have named the file white.asm in the previous code so continuing with the same name here :)

with open("white.asm",'r') as a:
    with open('symbolsandvariables.asm', 'w+') as b:
        file = a.readlines()
        m=len(file)
        n=1
        for i in file:
            n+=1
            if check(i) :
            	b.write(i)
