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