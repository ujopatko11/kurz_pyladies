"""Zaparkovali jste auto na parkovišti a chcete vypočítat celkovou cenu jízdenky. Pravidla účtování jsou následující:

Vstupné na parkoviště je 2;
První celá nebo částečná hodina stojí 3;
Každá následná celá nebo částečná hodina (po první) stojí 4.
Vstoupili jste na parkoviště v čase E a odjeli v čase L. V tomto úkolu jsou časy reprezentovány jako řetězce ve formátu "HH:MM" (kde "HH" je dvoumístné číslo mezi 0 a 23, které znamená pro hodiny a „MM“ je dvoumístné číslo mezi 0 a 59, což znamená minuty).

Napište funkci:

def roztok (E, L)

že zadané řetězce E a L určující body v čase ve formátu "HH:MM" vrátí celkovou cenu účtu za parkování od vašeho vstupu v čase E k vašemu výjezdu v čase L. Můžete předpokládat, že E popisuje čas před L ve stejný den.

Například při „10:00“ a „13:21“ by vaše funkce měla vrátit 17, protože vstupní poplatek se rovná 2, první hodina stojí 3 a zbývají další dvě celé hodiny a část další hodiny, takže celková cena je 2 + 3 + (3 * 4) = 17. Vzhledem k "09:42" a "11:42" by vaše funkce měla vrátit 9, protože vstupné se rovná 2, první hodina stojí 3 a druhá hodina 4 , takže celkové náklady jsou 2 + 3 + 4 = 9.

Předpokládat, že:

řetězce E a L striktně dodržují formát " HH:MM ";
řetězec E popisuje čas před L ve stejný den.
Při řešení se zaměřte na správnost . Výkon vašeho řešení nebude předmětem hodnocení."""

A = [-1, -3]
import random
def solution(A):
    # write your code in Python 3.6
    N = set(range(1, 100001))
    return min(N - set(A))


def solution1(N):
    binx = bin(N)
    formated = binx[2:]
    print(formated)
    string = str(formated)
    print(string)
    if string.count("1") < 2:
        return 0
    first = string.index("1")
    second = string.index("1", first)
    return len(second - first)

print(solution1(35))
