import json

data = {
    'stav_hry': []

}
def zapis_stav(koren, hodnota):
    data[koren] = hodnota
    run = json.dumps(data, ensure_ascii=False, indent=2)
    with open('stavHry.json', encoding='utf-8', mode='w') as souborJson:
        print(run, file=souborJson)

def zjisti_stav_hry():
    try:
        with open('stavHry.json', encoding='utf-8', mode='r') as souborJsonRead:
            kod = souborJsonRead.read()
            data = json.loads(kod)
            if "-" in data['stav_hry']:
                return data['stav_hry']
    except FileNotFoundError:
        return "-" * 20



