zoznam = []
cisla = [0]*10
jedna = 'ADGJMPSVY'
dva = 'BEHKNQTWZ'
tri = 'CFILORUX'
v = ''

veta = input('Zadaj vetu na zašifrovanie: ')
veta = veta.strip()
for i in range(len(veta)):
    cislo = int((ord(veta[i])-65)/3)+1
    if ord(veta[i])==32:
        zoznam.append('0')
        cisla[0] += 1
    elif veta[i] in jedna:
        zoznam.append(str(cislo)*1)
        cisla[cislo] += 1
    elif veta[i] in dva:
        zoznam.append(str(cislo)*2)
        cisla[cislo] += 2
    elif veta[i] in tri:
        zoznam.append(str(cislo)*3)
        cisla[cislo] += 3

for i in range(len(zoznam)):
    v = v+' '+zoznam[i]
print(v)
print('Najčastejšie zvolené políčka: '+str(cisla.index(max(cisla))))
