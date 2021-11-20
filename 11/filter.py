seznam = []
with open('index.dic.txt', encoding='utf-8', mode="r") as soubor:
    for radek in soubor:
        radek = radek.rstrip().split("/")
        slovo = radek[0]
        if slovo[0].lower() == slovo[0]:
            seznam.append(slovo)
    seznam.pop(0)
    print(seznam)
with open("zapis_slov.txt", encoding='utf-8', mode="w") as soubor2:
    for slovo in seznam:
        print(slovo, end="\n", file=soubor2)