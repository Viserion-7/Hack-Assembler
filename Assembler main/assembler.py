# This is the final compilation of converting both A and C Instruction to binary.
# The binary code for differennt parts of a C Instruction
comp={'1':{'M': '110000', '!M':'110001', '-M':'110011', 'M+1':'110111', 'M-1':'110010', 
        'D+M':'000010', 'D-M':'010011', 'M-D':'000111', 'D&M':'000000', 'D|M':'010101'},

      '0':{'0': '101010', '1':'111111', '-1':'111010', 'D':'001100', 'A':'110000',
        '!D':'001101', '!A':'110001', '-D':'001111', '-A':'110011', 'D+1':'011111',
        'A+1':'110111', 'D-1':'001110', 'A-1':'110010', 'D+A':'000010', 'D-A':'010011',
        'A-D':'000111', 'D&A':'000000', 'D|A':'010101'}}
dest = {'0':'000', 'M':'001', 'D':'010', 'MD':'011', 'A':'100', 'AM':'101',
        'AD':'110', 'AMD':'111'}
jump = {'0':'000', 'JGT':'001', 'JEQ':'010', 'JGE':'011', 'JLT':'100',
        'JNE':'101', 'JLE':'110', 'JMP':'111'}
# Predefined symbols are added to a dictionary.
symbol_table={'R0':'0','R1':'1','R2':'2','R3':'3','R4':'4','R5':'5',
'R6':'6','R7':'7','R8':'8','R9':'9','R10':'10','R11':'11',
'R12':'12','R13':'13','R14':'14','R15':'15','SP':'0',
'LCL':'1','ARG':'2','THIS':'3','THAT':'4','SCREEN':'16384',
'KBD':'24576'}
value_table = []
variables={}
# This function gives value for labels according to line number
def line_index(x,data):
    count = 0
    for i in data :
        if (i[0]) == '(':
            if x == i[1:-2]:
                value_table.append(count)
                variables[x]=count
                return True
        else :
            count += 1 

def instruction(x,y,z):
	# Adding computing part
    if y in comp['0']:
        value ='1110'+comp['0'][y]
    else:
        value = '1111'+comp['1'][y]
    new=value
	# Adding Destination part        
    if x:
        value=dest[x]
        new+=value
    else:
        new+='000'
	# Adding Jump part            
    if z:
        value=jump[z]
        new+=value
    else:
        new+='000'
    return new

def remwhite(file):
    i=0
    n=len(file)
    white=[]
    while i<n:
        l=file[i]
        l=l.replace(' ','')
        # removes all spaces        
        if  l[0]=='\n' or l[0]=='/':
        # removes new line and comments        
            pass
        else:
            if '/' in l:
                # removes inline comments            
                x=l.index('/')
                l1=''
                for j in range(x):
                    l1=l1+l[j]
                l=l1+'\n'
            if i==n-1:
                l.strip()
            white.append(l)
        i+=1
    return white
f=input("Enter filename with extension : ")
with open(f) as a:
    with open("out.hack",'w+') as b:
        file = a.readlines()
        file=remwhite(file)
        bit_count = 15
        f=0
        for l in file :
            if l[0] =='@' or l[0] == '(':
		        # Checking whether it is an A instruction                
                if l[0]==('@'):
                	# Checking whether it is a predefined symbol
                	if l[1:-1] in symbol_table.keys():
                		value_table.append(symbol_table[l[1:-1]])
	                	variables[l[1:-1]]=symbol_table[l[1:-1]]
	                # Checking whether it is a label
	                elif line_index(l[1:-1],file) == True :
	                	pass
	                # Checking whether it a digit
	                elif l[1].isdigit():
	                	k = "{}".format(l[1:-1])
	                	value_table.append(k)
	                # Checking whether symbol exists in table already
	                # if it doesnt exist adding it along with it's value
	                elif l[1:-1] not in variables.keys():
	                	bit_count += 1
	                	value_table.append(bit_count)
	                	variables[l[1:-1]]=bit_count
	                else:
	                	value_table.append(variables[l[1:-1]])
	                # Converting to Binary
	                nullcode = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	                x = int(value_table[f])
	                # Converting to binary and replacing elements in list
	                f+=1
	                a = str(bin(x).replace("0b",""))
	                for i in range(-1,-(len(a)+1),-1):
	                	nullcode[i]=a[i]
	                i=0
	                instr = ""
	                for v in (nullcode):
	                	instr += str(v)
	                b.write(instr+'\n')
            else:
                	# C Instruction
                	# we need to spilt the whole code into 3 parts dest comp and jump
                	# Replacing = with a space 
                	c = (l.strip()).replace('='," ")
                	# Replacing ; with a space
                	d = c.replace(';'," ")
                	# Splitting the instruction to 3 parts
                	e = d.split(" ")
                	# Checking which all part exists in the instruction
                	if len(e) == 3:
                		final=instruction(e[0],e[1],e[2])
                	elif len(e) == 2:
                		if '=' in l:
                			final=instruction(e[0],e[1],0)        
                		else:
                			final=instruction(0,e[0],e[1])
                	elif len(e) == 1:
                		final=instruction(0,e[0],0)
                	b.write(final+'\n')
