from random import randrange
from util import tah
def tah_pocitace(pole, symbol):
    while True:
        pozice = randrange(len(pole))
        if pole[pozice] == "-":
            return tah(pole, pozice, symbol)
        else:
            raise ValueError