import json


def get_file_json(url: str = 'city.list.json') -> list:
    with open(url, 'r', encoding='UTF-8') as file:
        return json.loads(file.read())


cities = get_file_json()


# 1. Определить количество городов в файле.
def get_count_cities() -> int:
    count = 0
    for i in cities:
        if i['country']:
            count += 1
    return count


# 2. Создать словарь, где ключ — это код страны, а значение — количество городов.
def get_count_cities_by_countries() -> dict:
    """Функция создает и возвращает словарь, где ключ — это код страны, а значение — количество городов."""
    count_cities = dict()

    for city in cities:
        if city['country']:
            if city['country'] in count_cities:
                count_cities[city['country']] += 1
            else:
                count_cities[city['country']] = 1

    return count_cities


# 3. Подсчитать количество городов в северном полушарии и в южном
def count_cities_hemispheres() -> dict:
    """
    Функция подсчитывает количество городов в разных полушариях и экваторе
    :return: возвращает словарь с тремя ключами юг, север и экватор
    """
    # Северное полушарие + lat +
    # Южное полушарие - lat -
    count_cities = {'north': 0, 'south': 0, 'equator': 0}
    for city in cities:
        if city['country'] != '':
            if city['coord']['lat'] > 0:
                count_cities['north'] += 1
            elif city['coord']['lat'] < 0:
                count_cities['south'] += 1
            else:
                count_cities['equator'] += 1
    return count_cities


print(get_count_cities())
print(get_count_cities_by_countries())
print(count_cities_hemispheres())
