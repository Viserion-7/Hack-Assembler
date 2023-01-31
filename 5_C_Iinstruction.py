# This is a standalone C instruction binary convertor
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
f=input("Enter filename with extension : ")
with open(f) as a:
    with open("cinstr.asm",'w+') as b:
        file = a.readlines()
        for l in file :
            if l[0] =='@' or l[0] == '(':
                continue
            else:
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
