"""
with open("maps/final_maps/oceania.json", "r+") as f:
    lines = [i.replace("\n", "") for i in f.readlines()]
    print(lines)
    jsonString = ""
    for i in lines:
        jsonString += '"{}":"(1, 1)",'.format(i)
    print(jsonString)"""

import json
from random import randint

with open("maps/data/world_random_binarydata.json", "r+") as f:
    with open("maps/final_maps/world_full.json") as og:
        dic = json.load(og)
        data_json = "{"
        for region in dic["regions"]:
            data_json += '"{}":"{}",'.format(region, randint(0, 1))
print(data_json)