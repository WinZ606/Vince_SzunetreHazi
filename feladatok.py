import random

def feladat1():
    szam1 = int(input(f"Kérek egy számot 200-920 között!\n"))
    if (szam1 <= 920) or (szam1 >= 200):
        elso = str(szam1)[0]
        print(f"az első számjegy: {elso}\n")
    else:
        print(f"A megadott szám nem 200-920 között van!\n")

def feladat2(szam2:int):
    if szam2 == 1:
        print("Még 90-on vagyunk! ")
    elif szam2 == 2 or szam2 == 3:
        print("Még bírjuk! (60%)")
    elif szam2 <= 7 and szam2 >= 4:
        print("Progit tanulunk, töltődünk! (70%)")
    elif szam2 == 8 or szam2 == 9:
        print("Lassan nem bírjuk tovább! (50%)")
    elif szam2 > 10:
        print("Ez már tényleg túlzás!")
    elif szam2 == 0:
        print("Be se jövök! ")
    else:
        print(f"Hiba nincs {szam2}. órájuk! ")

def feladat3(nap:int,ora:str.lower):
    if nap == 1 or nap == 2 and ora != "hittan":
        print("Alszik")
    elif nap == 2 and ora == "hittan" or nap == 4:
        print("Figyel")
    elif ora == "programozás" and nap == 3:
        print("Dolgozik")
    elif nap == 5:
        print("Félig figyel")
    else:
        print("Nincs info")

def feladat4():
    szam3 = float(input(f"Kérek egy valós számot!\n"))
    if szam3 >= 0:
        gyok = float(szam3 ** 0.5)
        print(f"{szam3} négyzetgyöke: {gyok}")
    else:
        print("Negatív számból nem lehet gyököt vonni!")

def feladat5():
    print(f"Szektorok:\n1 -> A\n2 -> B és E\n3 -> C\n4 -> D\n5 -> F\n6 -> G\n7 -> H")
    szam4 = int(input("Melyik szektor kiállítására vagy kíváncsi?\n"))
    if szam4 == 1:
        print(f"A szektor:\nNemzetközi Csarnok, World Conservation Forum 2021")
    elif szam4 == 2:
        print(f"B és E szektor:\nKereskedelmi Csarnok")
    elif szam4 == 3:
        print(f"C szektor:\nKonferencia-központ Innovációs Showroom")
    elif szam4 == 4:
        print(f"D szektor:\nHal, Víz és Ember")
    elif szam4 == 5:
        print(f"F szektor:\nHagyományos Vadászati Módok Csarnoka")
    elif szam4 == 6:
        print(f"G szektor:\nHazai és nemzetközi Trófeakiállítás, 12. Nyílt Európai Taxiderma-bajnokság, Vadászat 21.században kiállítás")
    elif szam4 == 7:
        print(f"H szektor:\nKözponti Magyar Kiállítás")
    else:
        print("Forduljon a pénztárhoz!")

def feladat6_lista():
    szamok = []
    i = 0
    while i < 13:
        szam1 = int(random.random()*18)-5
        szamok.append(szam1)
        i += 1
    return szamok

def feladat6_1(lista):
    i = 0
    pozitiv = 0
    negativ = 0
    while i < 13:
        if lista[i] < 0:
            negativ += 1
        else:
            pozitiv += 1
        i += 1
    print(f"Pozitív eredmények száma: {pozitiv}")
    print(f"Negatív eredmények száma: {negativ}")

def feladat6_2_3(lista):
    i = 0
    paros = 0
    paratlan = 0
    while i < 13:
        if lista[i] % 2 == 0:
            paros += lista[i]
        else:
            paratlan += lista[i]
        i += 1
    print(f"Páros számok összege: {paros}")
    if paros > paratlan:
        print(f"A páros számok összege nagyobb! ({paros})")
    elif paros < paratlan:
        print(f"A páratlan számok összege nagyobb! ({paratlan})")
    else:
        print("A két összeg egyenlő!")

def feladat6_4_5(lista):
    i = 0
    osszeg = 0
    while i < 13:
        osszeg += lista[i]
        i += 1
    atlag = osszeg/13
    print(f"A számok átlaga: {atlag}")
    print(f"A lista legnagyobb eleme: {max(lista)}")

def feladat7():
    nevek = ""
    nevek2 = []
    nevekszam = 0
    print("Kérek neveket!")
    while nevek != "@":
        nevek = str(input(""))
        if nevek != "@":
            nevek2.append(nevek)
            nevekszam += 1

    print(f"Ennyi név lett megadva: {nevekszam}")

    o = 0
    elsobetu = []
    while o < (nevekszam):
        elsobetu.append(nevek2[o][0].upper())
        o += 1

    if (elsobetu.count("A")) > 0:
        print("Van A betűvel kezdődő név!")
    else:
        print("Nincs A betűbel kezdődő név!")
    
    nevhossz = []
    for i in range(0,(nevekszam),1):
        nevhossz.append(len(nevek2[i]))

    legnev = nevhossz.index(max(nevhossz))
    melyiknev = nevek2[legnev]
    if nevekszam > 0:
        print(f"A {legnev}. név a leghosszabb, vagyis {melyiknev}")
    else:
        print("Nincs megadott név!")

"""def feladat8():
    fszam = 0
    o = 0
    sorozat = 0
    p = 10
    print("Fej vagy írás: (f/i)")
    for i in range(0,p,1):
        fi = str(input(""))
        if fi == "f" or fi == "i":
            if fi == "f":
                fszam += 1
        else:
            fi = str(input("Fej (f) vagy írás (i) lehet csak!\n"))
            p += 1
    while o < p:
        if o < (p-1):
            if fi[o] == fi[(o+1)]:
                sorozat += 1
        o += 1"""
def feladat8():
    fszam = 0  
    sorozat1 = 0  
    sorozat2 = 0
    p = 10
    eredmenyek = []

    for i in range(0,p,1):
        fi = input("Fej vagy írás: (f/i)\n").lower()
        if fi == "f" or fi == "i":
            eredmenyek.append(fi)
        else:
            print("Fej (f) vagy írás (i) lehet csak!")

    for o in range(0,len(eredmenyek),1):
        if eredmenyek[o] == "f":
            fszam += 1
            sorozat2 += 1
            if sorozat2 > sorozat1:
                sorozat1 = sorozat2
        else:
            sorozat2 = 0  

    print(f"Összes fej dobás: {fszam}")
    print(f"Leghosszabb fej sorozat: {sorozat1}")

def feladat9():
    print("Szorzótábla:")
    print("*"*49)
    
    for i in range(1, 11):
        for o in range(1, 11):
            print(f"{i * o:4}", end=" ")
        print()

def feladat10_1(szam):
    eredmenyek = []
    helyi = 1

    while helyi <= szam:
        darab = szam // helyi
        eredmenyek.append(darab % 10)
        helyi *= 10

    return eredmenyek

def feladat10_2(eredmeny,szam):
    helyi = 1
    i = 0
    while helyi <= szam:
        if i < len(eredmeny):
            db = eredmeny[i]
        print(f"{helyi}-esek: {db}")
        helyi *= 10
        i += 1