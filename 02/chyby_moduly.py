while True:
    num1 = input("Zadej první číslo: ")
    num2 = input("Zadej druhé číslo: ")
    try:
        int_num1 = int(num1)
        int_num2 = int(num2)
        break
    except ValueError:
        print("Zadávej pouze čísla")


oper1 = input("Zadej operátor +, -, * nebo /.")
operator = ["+", "-", "*", "/"]
vysledek = ""


def deleni(delenec, delitel):
    try:
        return delenec / delitel
    except ZeroDivisionError:
        print(f'{delitel} nelze dělit.')


if oper1 == operator[0]:
    vysledek = int_num1 + int_num2
elif oper1 == operator[1]:
    vysledek = int_num1 - int_num2
elif oper1 == operator[2]:
    vysledek = int_num1 * int_num2
else:
    vysledek = deleni(int_num1, int_num2)
    if vysledek == None:
        vysledek = "nulou nelze delit"
print("První číslo: ", int_num1)
print("Druhé číslo: ", int_num2)
print("Operace: ", oper1)
print(int_num1, oper1, int_num2, " = ", vysledek)
