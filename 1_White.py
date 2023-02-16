# This is the standalone code for removing white spaces from an asm file.
# change file name here for different asm files
# current file used is from project 6/rect/rect.asm
filename=input("Enter filename with extension : ")
with open(filename, 'r') as raw:
    with open('white.asm', 'w+') as white:
        file=raw.readlines()
        for line in file:
            line=line.replace(' ','')	
            # removes all spaces
            if  line[0]=='\n' or line[0]=='/':
            # removes new line and comments
                pass
            else:
                if '/' in line:
                # removes inline comments
                    comment_index = line.index('/')
                    line = line[:comment_index]+'\n'
                white.write(line)