subor = open('mena_zamestnancov.txt', 'r')
subor2 = open('vystup.txt', 'w')

pocet = 0
naj_m = ''
naj_p = ''
zoznam = []
for riadok in subor:
    pocet += 1
    riadok = riadok.strip()
    zoznam.append(riadok)
for i in range(int(pocet/2)):
    if len(zoznam[i])>len(naj_m):
        naj_m = zoznam[i]
    if len(zoznam[i+int(pocet/2)])>len(naj_p):
        naj_p = zoznam[i+int(pocet/2)]
    subor2.write(zoznam[i]+' '+zoznam[i+int(pocet/2)]+'\n')
    
subor.close()
subor2.close()
print('Počet zamestnancov je: '+str(round(pocet/2)))
print('Najdlhšie meno je: '+naj_m)
print('Najdlhšie priezvisko je: '+naj_p)
