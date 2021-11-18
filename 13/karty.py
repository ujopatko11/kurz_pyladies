import random
def vytvor_balicek():
    ciselne_hodnoty = list(range(2, 11))
    pismenne_hodnoty = list('JQKA')

    balicek = []
    for barva in '♠', '♥', '♦', '♣':
        for hodnota in (ciselne_hodnoty + pismenne_hodnoty):
            dvojicky = (str(hodnota), barva)
            balicek.append(dvojicky)


    random.shuffle(balicek)
    return balicek
print(vytvor_balicek())