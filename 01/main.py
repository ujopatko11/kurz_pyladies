

from random import randrange


def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"


vysledek1 = vyhodnot('--------------------')
vysledek2 = vyhodnot('--o--xxx---o--o-----')
vysledek3 = vyhodnot('xoxoxoxoxoxoxoxoxoxo')

print(vysledek1)
print(vysledek2)
print(vysledek3)


def tah(pole, pozice, symbol):

    zacatek = pole[:pozice]
    konec = pole[pozice + 1:]
    nove_pole = zacatek + symbol + konec
    if pozice >= 0 and pozice < len(pole) and pole[pozice] == '-' and symbol in ["x", "o"]:
        return nove_pole
    else:
        raise ValueError


tah1 = tah("--------------------", 1, "x")
tah2 = tah("--------------------", 19, "o")
tah3 = tah("x-o-xoo-x-o-x-o-x-o-", 1, "x")
print(tah1)
print(tah2)
print(tah3)


def tah_hrace(pole, symbol):
    while True:
        pozice = input('Na které políčko chceš hrát? ')
        try:
            int_pozice = int(pozice)
        except ValueError:
            print("Zadávej čísla !")
            continue
        try:
            return tah(pole, int_pozice, symbol)
        except ValueError:
            print("Nejde zahrát na tomto poli")
print("Nový stav hry je:", tah_hrace('o-------------------', 'x'))


def tah_pocitace(pole, symbol):
    while True:
        pozice = randrange(len(pole))
        if pole[pozice] == "-":
            return tah(pole, pozice, symbol)
print(tah_pocitace('o-------------------', 'x'))


def piskvorky1d():
    pole = "-" * 20
    while True:
        print(pole)
        pole = tah_hrace(pole, "x")
        print(pole)
        if vyhodnot(pole) != '-':
            break
        pole = tah_pocitace(pole, "o")
        if vyhodnot(pole) != '-':
            break

    print(pole)
    if vyhodnot(pole) == '!':
        print('Remíza!')
    elif vyhodnot(pole) == 'x':
        print('Vyhrála jsi!')
    elif vyhodnot(pole) == 'o':
        print('Vyhrál počítač!')


piskvorky1d()