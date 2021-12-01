def mocniny(n):
    slovnik = {}
    for x in range(1, n+1):
        slovnik[x] = x**2
    return slovnik
#print(mocniny(4))
slovnik1 = mocniny(4)
def vypis_slovnik(slovnik):
    for klic, hodnota in slovnik.items():
        print(f'Klíč {klic}, hodnota {hodnota}')

#vypis_slovnik(slovnik1)
slovnik_eng_cz = {}
slovnik_cz_eng = {'Jablko': 'Apple', 'Knoflík': 'Button', 'Myš': 'Mouse'}

def obrat_slovnik(slovnik):
    anglicko_cesky = {}
    for prvni, druhy in slovnik.items():
        anglicko_cesky[druhy] = prvni
    return anglicko_cesky

#print(obrat_slovnik(slovnik_cz_eng))

"""
import collections
def pocet_znaku(str):
    repeated = {}
    freq = collections.Counter(str)

    for key, value in freq.items():
        repeated[key] = value
    return repeated


print(pocet_znaku("halllo"))
"""
import collections as col
def pocet_znaku(strx):
    d = col.defaultdict(int)
    for key in strx:
        d[key] += 1
    return d.items()

print(pocet_znaku('nejdeee'))

slovnikx = {'a': 'ɐ', 'b': 'q', 'c': 'ɔ', 'd': 'p', 'e': 'ǝ', 'f': 'ɟ', 'g': 'ƃ',
 'h': 'ɥ', 'i': 'ᴉ', 'j': 'ɾ', 'k': 'ʞ', 'l': 'l', 'm': 'ɯ', 'n': 'u',
 'o': 'o', 'p': 'd', 'q': 'b', 'r': 'ɹ', 's': 's', 't': 'ʇ', 'u': 'n',
 'v': 'ʌ', 'w': 'ʍ', 'x': 'x', 'y': 'ʎ', 'z': 'z', 'A': '∀', 'B': 'B',
 'C': 'Ɔ', 'D': 'D', 'E': 'Ǝ', 'F': 'Ⅎ', 'G': 'פ', 'H': 'H', 'I': 'I',
 'J': 'ſ', 'K': 'ʞ', 'L': '˥', 'M': 'W', 'N': 'N', 'O': 'O', 'P': 'Ԁ',
 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': '┴', 'U': '∩', 'V': 'Λ', 'W': 'M',
 'X': 'X', 'Y': '⅄', 'Z': 'Z', '0': '0', '1': 'Ɩ', '2': 'ᄅ', '3': 'Ɛ',
 '4': 'ㄣ', '5': 'ϛ', '6': '9', '7': 'ㄥ', '8': '8', '9': '6', ',': "'",
 '.': '˙', '?': '¿', '!': '¡', '"': '„', "'": ',', '`': ',', '(': ')',
 ')': '(', '[': ']', ']': '[', '{': '}', '}': '{', '<': '>', '>': '<',
 '&': '⅋', '_': '‾'}
basnickax = 'basnicka.txt'
def prohod_text(basnicka, slovnik):
    nova_basen = ""
    with open(basnicka, encoding='utf-8', mode="r") as soubor:
        for radek in soubor:
            for znak in radek:
                if znak in slovnik:
                    nova_basen = nova_basen + slovnik[znak]
                else:
                    nova_basen = nova_basen + znak
    return nova_basen
#print(prohod_text(basnickax, slovnikx))
