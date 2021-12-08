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

#print(pocet_znaku('nejdeee'))

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
basnicka = 'basnicka.txt'
def prohod_text(txt_file, slovnik):
    novy_text = ""
    with open(txt_file, encoding='utf-8', mode="r") as soubor:
        for radek in soubor:
            for znak in radek:
                if znak in slovnik:
                    novy_text = novy_text + slovnik[znak]
                else:
                    novy_text = novy_text + znak
    return novy_text
#print(prohod_text(basnicka, slovnikx))


import random
def ziskej_odpovedi():
    odpovedi = {"kdo":[],"co":[],"kde":[]}
    for i in range(len(odpovedi)):
        otazka = input(f"zadej {list(odpovedi.keys())[i]}:")
        odpovedi[list(odpovedi.keys())[i]].append(otazka)
    return odpovedi

vsechny_odpovedi = ziskej_odpovedi()


def vyber_odpovedi(odpoved):
    kdo = random.choice(odpoved["kdo"])
    co = random.choice(odpoved["co"])
    kde = random.choice(odpoved["kde"])
    return kdo, co, kde

vybrane_odpovedi = vyber_odpovedi(vsechny_odpovedi)


def vypis_vysledek(xyz):
    kdo, co, kde = xyz
    print(f'{kdo} {co} {kde}.')

vypis_vysledek(vybrane_odpovedi)
