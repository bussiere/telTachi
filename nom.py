f = open('name.txt', 'r')
total = "["
for line in f :
    line = line.replace("\n","")
    line = line.replace("\r","")
    total = total + "\"%s\","%line

total = total[:-1] + "]"
print(total)