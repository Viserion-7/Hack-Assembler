# This is a standalone A instruction binary convertor
# Predefined symbols are added to a dictionary.
symbol_table={'R0':'0','R1':'1','R2':'2','R3':'3','R4':'4','R5':'5',
'R6':'6','R7':'7','R8':'8','R9':'9','R10':'10','R11':'11',
'R12':'12','R13':'13','R14':'14','R15':'15','SP':'0',
'LCL':'1','ARG':'2','THIS':'3','THAT':'4','SCREEN':'16384',
'KBD':'24576'}
value_table = []
v={}
# This function gives value for labels according to line number
def line_index(x,data):
    count = 0
    for i in data : 
        if (i[0]) == '(':
            if x == i[1:-2]:
                value_table.append(count)
                v[x]=count
                return True
        else :
            count += 1 

f=input("Enter filename with extension : ")
with open(f) as rawfile:
    with open("ainstr.asm","w+") as b:
        file = rawfile.readlines()
        bit_count = 15
        for l in file :
	        # Checking whether it is an A instruction
            if l[0]==('@'):
            	# Checking whether it is a predefined symbol
                if l[1:-1] in symbol_table.keys():
                	value_table.append(symbol_table[l[1:-1]])
                	v[l[1:-1]]=symbol_table[l[1:-1]]
                # Checking whether it is a label
                elif line_index(l[1:-1],file) == True :
                    continue
                # Checking whether it a digit
                elif l[1].isdigit():
                	k = "{}".format(l[1:-1])
                	value_table.append(k)
                	v[k]=k
				# Checking whether symbol exists in table already
                # if it doesnt exist adding it along with it's value
                elif l[1:-1] not in v.keys():
                    bit_count += 1
                    value_table.append(bit_count)
                    v[l[1:-1]]=bit_count
                else:
                    value_table.append(v[l[1:-1]])
        # Converting to Binary
        for i in value_table:
            nullcode = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            x = int(i)
            # Converting to binary and replacing elements in list
            a = str(bin(x).replace("0b",""))
            for i in range(-1,-(len(a)+1),-1):
                nullcode[i]=a[i]
            instruction = ""
            for i in nullcode:
                instruction += str(i)
            b.write(instruction+'\n')
