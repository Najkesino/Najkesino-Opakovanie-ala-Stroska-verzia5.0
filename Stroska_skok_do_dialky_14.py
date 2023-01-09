zoznam_k = []
zoznam = []
pocet = []
naj = ''
cislo = 0

subor = open('skok_do_dialky.txt', 'r')
for riadok in subor:
    riadok = riadok.strip()
    riadok = riadok.split()
    zoznam_k.append(riadok[1])
    for i in range(len(riadok)-2):
        if int(riadok[2+i])==int(cislo):
            naj = naj+' a '+riadok[0]
        if int(riadok[2+i])>int(cislo):
            cislo = riadok[2+i]
            naj = riadok[0]
subor.close()

for i in zoznam_k:
    if i in zoznam:
        cislo = zoznam.index(i)
        pocet[cislo] += 1
    if i not in zoznam:
        zoznam.append(i)
        pocet.append(1)
        
print('Krajiny ktoré sa zúčastnili a počet súťažiacich danej krajiny: ')
for i in range(len(zoznam)):
    print(zoznam[i]+' '+str(pocet[i]))
print('Celkový víťaz je: '+naj)
