import random

def vytvor_seznam_zvirat():
    return ['pes', 'kočka',"andulka", 'králík', 'had']
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
    return True if word in list else False


print(obsahuje(zvirata, "pes"))
print(obsahuje(zvirata, "nabytek"))


def bez_prvniho(list):
    return list[1:]
#print(bez_prvniho([]))
#print(bez_prvniho(zvirata))

def serad_od_druheho(list):
    return sorted(list, key=lambda word: word[1])
#print(serad_od_druheho(zvirata))


def vytvor_balicek():
    ciselne_hodnoty = list(range(2, 11))
    pismenne_hodnoty = list('JQKA')

    balicek = []
    for barva in '♠', '♥', '♦', '♣':
        for hodnota in (ciselne_hodnoty + pismenne_hodnoty):
            balicek.append(f"({hodnota} , {barva})")
    #print(balicek)

    random.shuffle(balicek)
    return balicek
print(vytvor_balicek())