import json
import fiona

json_s = {"type": "FeatureCollection", "features": []}

# layers : 2 country, 1 admin big regions, 0 admin smaller reginos
for layer in [1]:
    c = fiona.open('maps/geopackage_maps/gadm36_ZWE.gpkg', layer=layer)
    for feature in c:
        feat = feature
        feat["properties"] = dict(feat["properties"])
        feat["properties"]["name"] = feat["properties"]["NAME_{}".format(2 - layer)]

        json_s["features"].append(feat)
    with open("maps/geojson_maps/cache.geojson", "w+") as cache:
        cache.write(json.dumps(json_s))

"""print(len(list(c)))
print(c[1])
for i in range(1, len(list(c))):
    print(c[i])"""