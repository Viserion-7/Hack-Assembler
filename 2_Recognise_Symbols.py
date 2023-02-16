# This is the code for making a file which holds all the labels and variables in the code.
# This is part of the white.py code as an asm file with no white spaces is required for this code.

# I have named the file white.asm in the previous code so continuing with the same name here :)

with open("white.asm",'r') as white:
    with open('symbolsandvariables.asm', 'w+') as out:
        # For adding all the new labels and variables found in the asm file
        sym=[]
        file = white.readlines()
        for line in file:
            # Checking whether it is an A instruction
            if line[0] == '@':
                # Checking whether it is a symbol or number  
                if line[1].isalpha():
                    if line[1:-1] not in sym:
                        sym.append(line[1:-1])
                        out.write(line[1:])