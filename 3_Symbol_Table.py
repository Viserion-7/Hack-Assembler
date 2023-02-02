# This is the code for making a symbol table which holds all the symbols and variables in asm file along with their values.
# This is also part of the white.py code as an asm file with no white spaces is required for this code.
# predefined symbols are added to a dictionary.
symbol_table={'R0':'0','R1':'1','R2':'2','R3':'3','R4':'4','R5':'5',
'R6':'6','R7':'7','R8':'8','R9':'9','R10':'10','R11':'11',
'R12':'12','R13':'13','R14':'14','R15':'15','SP':'0',
'LCL':'1','ARG':'2','THIS':'3','THAT':'4','SCREEN':'16384',
'KBD':'24576'}
variables={}
# This function gives value for labels according to line number
def line_index(x,data):
    count = 0
    for i in data : 
        if (i[0]) == '(':
            if x == i[1:-2]:
                variables[x]=count
                return True
        else :
            count += 1 

# I have named the file white.asm in the previous code so continuing with the same name here :)
with open("white.asm") as rawfile:
    with open("symboltable.txt","w") as b:
        file = rawfile.readlines()
        bit_count = 15
        for l in file :
            if l[0]==('@'):
            	# ignoring all predefined symbols
                if l[1:-1] in symbol_table.keys():
                    pass
                # label name and value is saved to a dictionary
                elif line_index(l[1:-1],file) == True :
                    continue
                #ignoring all predefined symbols and numbers
                elif l[1:-1].isdigit() :
                    pass
                # checking whether symbol exists in table already
                # if it doesnt exist adding it along with it's value
                elif l[1:-1] not in variables.keys():
                    bit_count += 1
                    variables[l[1:-1]]=bit_count
                else:
                    pass
        b.write("Symbols \t Values\n")
        for i,j in symbol_table.items():
            b.write("{:<15} {:<15}\n".format(i,j))
        for i,j in variables.items():
            if isinstance(j,int):
                j=str(j)
            b.write("{:<15} {:<15}\n".format(i,j))