def tah(pole, pozice, symbol):
    zacatek = pole[:pozice]
    konec = pole[pozice + 1:]
    nove_pole = zacatek + symbol + konec
    if pozice >= 0 and pozice < len(pole) and pole[pozice] == '-' and symbol in ["x", "o"]:
        return nove_pole
    else:
        raise ValueError