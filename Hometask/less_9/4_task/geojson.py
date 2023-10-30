import json


def get_file_json(url: str = '../city.list.json') -> list:
    with open(url, 'r', encoding='UTF-8') as file:
        return json.loads(file.read())


cities = get_file_json()


def get_cities_country(code_country: str) -> list:
    return list(filter(lambda c: c['country'] == code_country, cities))


def get_geo(code_country: str):
    cities_country = get_cities_country(code_country)
    geo = {"type": "FeatureCollection", "features": [], }
    for city in cities_country:
        inner = {
            "type": "Feature",
            "id": city['id'],
            "geometry": {
                "type": "Point",
                "coordinates": [city['coord']['lon'], city['coord']['lat']],
            },
            "properties": {
                "iconCaption": city['name'],
                "marker-color": "#b51eff",
            },
        }
        geo['features'].append(inner)

    return geo


def create_geojson(code_country: str, filename='geojson.json'):
    try:
        with open(filename, 'w', encoding='UTF-8') as file:
            file.write(json.dumps(get_geo(code_country=code_country), indent=4))
            print(f'Файл успешно создан {filename}')
    except Exception as e:
        print(f'Не создался файл,\nОшибка:\n{e}')


create_geojson('BY')
