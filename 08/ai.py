from random import randrange
from util import tah


def tah_pocitace(pole, symbol):
    if "-" not in pole:
        raise ValueError("pole is full")
    if len(pole) == 0:
        raise ValueError("pole is empty")
    while True:
        pozice = randrange(len(pole))
        if pole[pozice] == "-":
            return tah(pole, pozice, symbol)