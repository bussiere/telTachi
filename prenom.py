import csv
fichier ="liste_des_prenoms_2004_a_2012.csv"
file = csv.reader(open(fichier, newline=''), delimiter=';', quotechar="'")
total = "["
for f in file :
    #print(f)
    total = total +  "\"%s\","%(f[0])
total = total[:-1]+"]"
print(total)