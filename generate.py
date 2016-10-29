a = [0,1,2,3,4,5,6,7,8,9]
b = [0,1,2,3,4,5,6,7,8,9]
total = "["
for c in a :
    for d in b :
        total = total + "\"%d%d\","%(c,d)

total = total[:-1] +"]"
print(total)
