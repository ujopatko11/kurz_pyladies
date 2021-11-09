from random import randrange
from util import tah


def tah_pocitace(pole, symbol):
    symbol_hrac = "x"
    if "-" not in pole and len(pole) >= 1:
        raise ValueError("pole is full")
    if len(pole) == 0:
        raise ValueError("pole is empty")
    if symbol_hrac + "-" in pole:
        pozice_ai_tah = pole.rfind(symbol_hrac + '-') + 1
        return tah(pole, pozice_ai_tah, symbol)
    else:
        while True:
            pozice = int(randrange(0, len(pole)))
            if pole[pozice] == "-":
                return tah(pole, pozice, symbol)
