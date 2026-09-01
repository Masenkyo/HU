import json

with open('stations.json', 'r') as file:
    info = json.load(file)

stations = info['payload']
meestOostelijkeStation = stations[0]

for station in stations:
    code = station['code']
    stationType = station['stationType']
    naamLang = station['namen']['lang']

    print(f"{naamLang:25} - {code:5} : {stationType}")

    if station['lng'] > meestOostelijkeStation['lng']:
        meestOostelijkeStation = station

print(f"\nHet meest oostelijk gelegen station is: {meestOostelijkeStation['namen']['lang']}")