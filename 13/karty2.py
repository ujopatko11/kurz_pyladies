import random

def vytvor_balicek():
    """Vrátí nový zamíchaný balíček karet."""
    karty = []
    for barva in 'Sr', 'Pi', 'Ka', 'Kr':
        for hodnota in range(1, 14):
            karta = hodnota, barva
            karty.append(karta)
    random.shuffle(karty)
    return karty


karty = vytvor_balicek()
#print(karty)


def popis_kartu(karta):
    """Popíše danou kartu; vrací řetězec jako "7♣", "A♠" nebo "Q♥"."""
    hodnota, barva = karta
    if hodnota == 11:
        popis_hodnoty = 'J'
    elif hodnota == 12:
        popis_hodnoty = 'Q'
    elif hodnota == 13:
        popis_hodnoty = 'K'
    elif hodnota == 1:
        popis_hodnoty = 'A'
    elif hodnota == 10:
        # Aby byly všechny hodnoty jednopísmenné,
        # a líp se to pak vypisovalo,
        # desítku označíme římským číslem.
        popis_hodnoty = 'X'
    else:
        popis_hodnoty = str(hodnota)

    if barva == 'Sr':
        popis_barvy = '♥'
    elif barva == 'Pi':
        popis_barvy = '♠'
    elif barva == 'Ka':
        popis_barvy = '♦'
    else:
        popis_barvy = '♣'

    return popis_hodnoty + popis_barvy

#print(popis_kartu(karty[0]))


def balicekValka(karty):
    for x in karty:
        print(popis_kartu(x))
#balicekValka(karty)

def porovnej_karty(karta_a, karta_b):
    if karta_a[0] > karta_b[0]:
        return 'A'
    elif karta_a[0] == karta_b[0]:
        return None
    else:
        return 'B'

#print(porovnej_karty((3, "Ka"), (2, "Sr")))

def rozdej_balicky():
    balicek = vytvor_balicek()
    polovina = len(balicek) // 2

    balicek_a = balicek[:polovina]
    balicek_b = balicek[polovina:]

    return balicek_a, balicek_b, []
balicky_x = rozdej_balicky()



def rozdej_balicky_sloupec():
    print("Hráč A\tHráč B")
    for karta1, karta2 in zip(balicky[0], balicky[1]):
        print(f"{popis_kartu(karta1)}\t\t{popis_kartu(karta2)}")

#rozdej_balicky_sloupec()

def vyloz_karty(balicky):
        balicek_a, balicek_b, na_stole = balicky
        try:
            karta_a = balicek_a.pop()
        except IndexError:
            raise SystemExit('Hráč B vyhrál')

        try:
            karta_b = balicek_b.pop()
        except IndexError:
            raise SystemExit('Hráč A vyhrál')


        print("Hráč A hraje kartu:", karta_a)
        print("Hráč B hraje kartu:", karta_b)
        na_stole.append(karta_a)
        na_stole.append(karta_b)

#vyloz_karty(balicky_x)


def valka(balicky):
    balicek_a, balicek_b, na_stole = balicky
    while True:
        vyloz_karty((balicek_a, balicek_b, na_stole))
        while na_stole[-2][0] == na_stole[-1][0]:
            print("Válka !!!")
            for _ in range(3):
                vyloz_karty((balicek_a, balicek_b, na_stole))
        if na_stole[-2][0] > na_stole[-1][0]:
            vitez_kola = "A"
        else:
            vitez_kola = "B"
        print(f"Hráč {vitez_kola} bere {len(na_stole)} karet!")
        print(30 * "-")
        if vitez_kola == "A":
            for karta in na_stole:
                balicek_a = [karta] + balicek_a
        else:
            for karta in na_stole:
                balicek_b = [karta] + balicek_b
        na_stole = []

valka(balicky_x)