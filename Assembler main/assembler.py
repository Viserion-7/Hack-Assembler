# This is the final compilation of converting both A and C Instruction to binary.
# The binary code for differennt parts of a C Instruction
comp_value={'1':{'M': '110000', '!M':'110001', '-M':'110011', 'M+1':'110111', 'M-1':'110010', 
        'D+M':'000010', 'D-M':'010011', 'M-D':'000111', 'D&M':'000000', 'D|M':'010101'},
      '0':{'0': '101010', '1':'111111', '-1':'111010', 'D':'001100', 'A':'110000',
        '!D':'001101', '!A':'110001', '-D':'001111', '-A':'110011', 'D+1':'011111',
        'A+1':'110111', 'D-1':'001110', 'A-1':'110010', 'D+A':'000010', 'D-A':'010011',
        'A-D':'000111', 'D&A':'000000', 'D|A':'010101'}}
dest_value = {'0':'000', 'M':'001', 'D':'010', 'MD':'011', 'A':'100', 'AM':'101',
        'AD':'110', 'AMD':'111'}
jump_value = {'0':'000', 'JGT':'001', 'JEQ':'010', 'JGE':'011', 'JLT':'100',
        'JNE':'101', 'JLE':'110', 'JMP':'111'}
# Predefined symbols are added to a dictionary.
symbol_table={'R0':'0','R1':'1','R2':'2','R3':'3','R4':'4','R5':'5',
'R6':'6','R7':'7','R8':'8','R9':'9','R10':'10','R11':'11',
'R12':'12','R13':'13','R14':'14','R15':'15','SP':'0',
'LCL':'1','ARG':'2','THIS':'3','THAT':'4','SCREEN':'16384',
'KBD':'24576'}
value_table = []

def remove_white(file):
    white=[]
    for line in file:
        line=line.replace(' ','')	
        if  line[0]=='\n' or line[0]=='/':
            pass
        else:
            if '/' in line:
                comment_index = line.index('/')
                line = line[:comment_index]+'\n'
            white.append(line)
    return white

def instruction(dest,comp,jump):
    if comp in comp_value['0']:
        value ='1110'+comp_value['0'][comp]
    else:
        value = '1111'+comp_value['1'][comp]
    binary=value
    if dest:
        value=dest_value[dest]
        binary+=value
    else:
        binary+='000'
    if jump:
        value=jump_value[jump]
        binary+=value
    else:
        binary+='000'
    
    return binary

file_name = input("Enter filename with extension : ")
with open(file_name) as raw:
    with open("out.hack",'w') as out:
        file = raw.readlines()
        file=remove_white(file)
        bit_count = 15
        A_instr_counter=0
        for line in file :
            if line[0] =='@' or line[0] == '(':
		        # A instruction                
                if line[0]==('@'):
                    # Checking whether it is a predefined symbol
                    if line[1:-1] in symbol_table.keys():
                        value_table.append(symbol_table[line[1:-1]])
                    # Checking whether it is a digit
                    elif line[1].isdigit():
                        value = "{}".format(line[1:-1])
                        value_table.append(value)
                    # Checking whether it is a label
                    # Gives value for labels according to line number
                    elif line[1].isupper():
                        line_num=0 # Line number
                        for temp in file:
                            if temp[0] =='(':
                                if line[1:-1] == temp[1:-2]:
                                    symbol_table[line[1:-1]] = str(line_num)
                                    value_table.append(symbol_table[line[1:-1]])
                            else:
                                line_num+=1
                    else:
                        bit_count += 1
                        value_table.append(bit_count)
                        symbol_table[line[1:-1]]=bit_count

	                # Converting to Binary
                    binary_write = format(int(value_table[A_instr_counter]),'016b')
                    A_instr_counter+=1
                    out.write(binary_write+'\n')
                    
            else:
                # C Instruction
                # we need to spilt the whole code into 3 parts dest comp and jump
            	# Replacing = with a space 
                equal_space= (line.strip()).replace('='," ")
                # Replacing ; with a space
                colon_space= equal_space.replace(';'," ")
                # Splitting the instruction to 3 parts
                instr = colon_space.split(" ")
                # Checking which all part exists in the instruction
                if len(instr) == 3:
                    binary_write=instruction(instr[0],instr[1],instr[2])
                elif len(instr) == 2:
                    if '=' in line:
                        binary_write=instruction(instr[0],instr[1],0)        
                    else:
                        binary_write=instruction(0,instr[0],instr[1])
                elif len(instr) == 1:
                    binary_write=instruction(0,instr[0],0)
                out.write(binary_write+'\n')

