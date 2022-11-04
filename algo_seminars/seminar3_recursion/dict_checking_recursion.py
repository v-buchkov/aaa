import json
# Rust-driven json => faster
import orjson

json_str = """{
"title": "iPhone X",
"class": "phones",
"price": 100, "location": {
"address": "город Самара, улица Мориса Тореза, 50",
"metro_stations": ["Спортивная", "Гагаринская"] }
}"""

data = orjson.loads(json_str)


def traverse(level: int, obj: dict):
    if not isinstance(obj, dict):
        return
    for k, v in obj.items():
        if isinstance(v, dict):
            print('|' + level * '_' + k)
            traverse(level + 1, v)
        elif isinstance(v, list):
            print('|' + level * '_' + '[]' + k)
            traverse(level + 1, v[0])
        else:
            print('|' + level * '_' + k)
    return


traverse(0, data)
