def vytvor_seznam_zvirat():
    return ['pes', 'kočka', 'králík', 'had']
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
    if word in list:
        return True
    else:
        return False
print(obsahuje(zvirata, "pes"))
print(obsahuje(zvirata, "nabytek"))

