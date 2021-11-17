with open('basnicka.txt', encoding='utf-8') as soubor:
    for radek in soubor:
        print(radek.rstrip().upper())
