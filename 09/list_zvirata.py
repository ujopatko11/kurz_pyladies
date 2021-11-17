import random

def vytvor_seznam_zvirat():
    return ['pes', 'kočka',"andulka", 'králík', 'had', 'pelikán']
zvirata = vytvor_seznam_zvirat()
#print(zvirata)


def filtruj_kratka_jmena(list, size):
    result = []
    for word in list:
        if len(word) < size:
            result.append(word)
    return result
#print(filtruj_kratka_jmena(zvirata, 5))

def filtruj_k(list):
    result = []
    for word in list:
        if word.startswith("k"):
            result.append(word)
    return result
#print(filtruj_k(zvirata))

def obsahuje(list, word):
    #return True if word in list else False
    return word in list

#print(obsahuje(zvirata, "pes"))
#print(obsahuje(zvirata, "nabytek"))


def bez_prvniho(list):
    return list[1:]
#print(bez_prvniho([]))
#print(bez_prvniho(zvirata))

def serad_od_druheho(list):
    return sorted(list, key=lambda word: word[1:])
print(serad_od_druheho(zvirata))


def vytvor_balicek():
    ciselne_hodnoty = list(range(2, 11))
    pismenne_hodnoty = list('JQKA')

    balicek = []
    for barva in '♠', '♥', '♦', '♣':
        for hodnota in (ciselne_hodnoty + pismenne_hodnoty):
            dvojicky = (str(hodnota), barva)
            balicek.append(dvojicky)


    random.shuffle(balicek)
    return balicek
#print(vytvor_balicek())

#for sloupec in range(5):
  #  for radek in range(5):
 #       print(sloupec * radek)
#    print()

#zaznamy = '3A,8B,2E,9D'.split(',')
#print(zaznamy)


def nakresli_mapu(seznam_souradnic):
    for cislo_radku in range(10):
        for cislo_sloupce in range(10):
            radek_a_sloupec = (cislo_radku, cislo_sloupce)
            if radek_a_sloupec in seznam_souradnic:
                print("x", end=" ")
            else:
                print(".", end=' ')
        print()

#nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)])

seznam_zvirat = ["pes", "kocka", "kralik", "had"]
def bez_prvniho(seznam_zvirat):
    prvni_zvire = seznam_zvirat[0]
    seznam_zvirat.remove(prvni_zvire)
    novy_seznam = []
    for zvire in seznam_zvirat:
        novy_seznam.append(zvire)
    return novy_seznam
print(bez_prvniho(seznam_zvirat))
print(seznam_zvirat)