# This is the standalone code for removing white spaces from an asm file.
# change file name here for different asm files
# current file used is from project 6/rect/rect.asm
f=input("Enter filename with extension : ")
with open(f, 'r') as a:
    with open('white.asm', 'w+') as b:
        file=a.readlines()
        for l in file:
            l=l.replace(' ','')	
            # removes all spaces
            if  l[0]=='\n' or l[0]=='/':
            # removes new line and comments
                pass
            else:
                if '/' in l:
                # removes inline comments
                    x=l.index('/')
                    l=l[:x]+'\n'
                b.write(l)