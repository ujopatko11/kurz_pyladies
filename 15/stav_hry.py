import json

data = {
    'stav_hry': [],
    'vitez': []
}
def zapis_stav(koren, hodnota):
    data[koren].append(hodnota)
    run = json.dumps(data, ensure_ascii=False, indent=2)
    with open('stavHry.json', encoding='utf-8', mode='w') as souborJson:
        print(run, file=souborJson)

def zjisti_stav_hry():

    with open('stavHry.json', encoding='utf-8', mode='r') as souborJsonRead:
        kod = souborJsonRead.read()
        data = json.loads(kod)
        if data['vitez'] == []:
            pole = data['stav_hry'][-1]
            return pole
        else:
            pole = "-" * 20
            return pole



