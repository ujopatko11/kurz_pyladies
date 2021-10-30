from util import tah


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
    print("Nový stav hry je:", tah_hrace('o-------------------', 'x'))