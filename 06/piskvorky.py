def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"

vyhodnot1 = vyhodnot('--------------------')
vyhodnot2 = vyhodnot('--o--xxx---o--o-----')
vyhodnot3 = vyhodnot('xoxoxoxoxoxoxoxoxoxo')

print(vyhodnot1, vyhodnot2, vyhodnot3)