# This is the code for making a file which holds all the symbols and variables in the code.
# This is part of the white.py code as an asm file with no white spaces is required for this code.

# I have named the file white.asm in the previous code so continuing with the same name here :)

with open("white.asm",'r') as a:
    with open('symbolsandvariables.asm', 'w+') as b:
        file = a.readlines()
        for i in file:
            # Checking whether it is an A instruction
            if i[0] == '@':
                # Checking whether it is a variable or number  
                if i[1].isalpha():
                    b.write(i)
            # Checking whether it is a label
            elif i[0] == '(':
                b.write(i)
