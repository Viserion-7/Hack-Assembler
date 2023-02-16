# This is a standalone A instruction binary convertor
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

file_name=input("Enter filename with extension : ")
with open(file_name) as raw:
    with open("ainstr.asm","w+") as out:
        file = raw.readlines()
        file = remove_white(file)
        bit_count = 16
        for line in file :
	    # Checking whether it is an A instruction
            if line[0]==('@'):
            	# Checking whether it is a predefined symbol
                if line[1:-1] in symbol_table.keys():
                    value_table.append(symbol_table[line[1:-1]])
                # Checking whether it a digit
                elif line[1].isdigit():
                    value = "{}".format(line[1:-1])
                    value_table.append(value)
                # Checking whether it a label
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
        print(value_table)
        # Converting to Binary
        for i in value_table:
            instruction = format(int(i),'016b')
            out.write(instruction+'\n')