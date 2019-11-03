f = open("../dataset.tff", "r")

neededLines = []
pos=[]
neg=[]
nut=[]
n=0

for line in f:
    line = line.split(' ')
   

    if (line[4] == "stemmed1=y" or line[3]=="pos1=noun"):
        n+=1
        neededLines.append(line[2]+"="+line[5])
    
    else:
        next

for lines in neededLines:
    lines = lines.split('=')
    lines = lines[1] + " " + lines[3].replace("\n", '')

    lines = lines.split(" ")

    if(lines[1]=="positive"):
        pos.append(lines[1])
    elif (lines[1] == "neutral"):
        nut.append(lines[1])
    elif (lines[1] == "negative"):
        neg.append(lines[1])
    else:


        
