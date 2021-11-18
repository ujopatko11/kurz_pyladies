import random

with open("zapis_slov.txt", encoding="utf-8", mode="r") as file:
    slova_by_lines = file.read().split()
    slovo = random.choice(slova_by_lines)
    file.close()
print(slovo)
spravne = ["_"] * len(slovo)
spatne = []
kontrola_spravne = False


while not kontrola_spravne:
    pismeno = input("Hádej znak.")

    if pismeno in slovo.lower() and len(pismeno) == 1:
        if pismeno in slovo:
            for i in range(len(slovo)):
                if slovo[i] == pismeno:
                    spravne[i] = pismeno
            print(pismeno)
        else:
            if pismeno in spatne:
                print("Znak již existuje.")
            else:
                print("Vedle.")
                spatne.append(pismeno)
                print(zapis_slov.rada_sibenic[-len(spatne)])

        kontrola_spravne = True
        for spravnepismeno in spravne:
            if spravnepismeno == "_":
                kontrola_spravne = False
                break
        if len(spatne) == 6:
            print("Prohra!")
            kontrola_spravne = False
            break
        print(" ".join(spravne))
        print(" ".join(spatne))
    else:
        print("Zadej pouze jeden znak.")
if kontrola_spravne:
    print("Výhra!")