# This is the code for making a file which holds all the symbols and variables in the code.
# This is part of the white.py code as an asm file with no white spaces is required for this code.
def check(z):
    # Checking whether it is a variable
    if z[0] == '@':
        # Checking whether it is a variable or number  
        if z[1].isalpha():
            return True
    # Checking whether it is a label
    elif z[0] == '(':
        return True
        
# I have named the file white.asm in the previous code so continuing with the same name here :)

with open("white.asm",'r') as a:
    with open('symbolsandvariables.asm', 'w+') as b:
        file = a.readlines()
        for i in file:
            if check(i) :
            	b.write(i)