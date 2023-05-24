# This is the code for making a symbol table which holds all the symbols and variables in asm file along with their values.
# This is also part of the white.py code as an asm file with no white spaces is required for this code.
# predefined symbols are added to a dictionary.
symbol_table = {'R0':'0','R1':'1','R2':'2','R3':'3','R4':'4','R5':'5',
'R6':'6','R7':'7','R8':'8','R9':'9','R10':'10','R11':'11',
'R12':'12','R13':'13','R14':'14','R15':'15','SP':'0',
'LCL':'1','ARG':'2','THIS':'3','THAT':'4','SCREEN':'16384',
'KBD':'24576'}

# I have named the file white.asm in the previous code so continuing with the same name here :)
with open("white.asm") as white:
    with open("symboltable.asm","w") as out:
        file = white.readlines()
        bit_count = 15
        for line in file :
            # Checking whether it is an A instruction
            if line[0]==('@'):
            	# Ignoring all predefined symbols and newly added symbols
                if line[1:-1] in symbol_table.keys():
                    pass
                # Ignoring all numbers
                elif line[1:-1].isdigit() :
                    pass
                # Gives value for labels according to line number
                elif line[1].isupper():
                    line_num=0 # Line number
                    for temp in file:
                        if temp[0] =='(':
                            if line[1:-1] == temp[1:-2]:
                                symbol_table[line[1:-1]] = str(line_num)
                        else:
                            line_num+=1
                else:
                    bit_count+=1
                    symbol_table[line[1:-1]]=bit_count
        out.write("Symbols \t Values\n")
        for i,j in symbol_table.items():
            out.write("{:<15} {:<15}\n".format(i,j))