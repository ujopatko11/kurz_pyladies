from util import tah
from ai import tah_pocitace
from stav_hry import *

def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"


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



def piskvorky1d():
    pole = "-" * 20
    while True:
        print(pole)
        zapis_stav('stav_hry', pole)
        pole = tah_hrace(pole, "x")
        print(pole)
        zapis_stav('stav_hry', pole)
        if vyhodnot(pole) != '-':
            break
        pole = tah_pocitace(pole, "o")
        if vyhodnot(pole) != '-':
            break

    print(pole)
    zapis_stav('stav_hry', pole)
    if vyhodnot(pole) == '!':
        print('Remíza!')
        zapis_stav('vitez', 'Remíza')
    elif vyhodnot(pole) == 'x':
        print('Vyhrála jsi!')
        zapis_stav('vitez', 'Hráč')
    elif vyhodnot(pole) == 'o':
        print('Vyhrál počítač!')
        zapis_stav('vitez', 'Počítač')
