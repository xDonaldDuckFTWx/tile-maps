import json
from shapely.geometry import Polygon, Point, MultiPolygon
from math import pi, sin, cos

def convertGeoJSON(file, treatMultiAsSingle=False, border_points=100):
    with open(file, encoding="utf-8") as f:
        geojson = json.load(f)
        regions = {} #["name"] = {"neighbors":"", "border":""}

        singlePolygons = {}
        for feature in geojson["features"]:
            name_names = ["name", "nom", "namn", "nam"]
            name_index = 0
            while name_names[name_index] not in feature["properties"].keys():
                name_index += 1
            name = feature["properties"][name_names[name_index]]
            regions[name] = {"neighbors" : [], "geometry" : None}

            if feature["geometry"]["type"] == "Polygon":
                regions[name]["geometry"] = Polygon(feature["geometry"]["coordinates"][0])
                singlePolygons[name] = Polygon(feature["geometry"]["coordinates"][0])

            elif feature["geometry"]["type"] == "MultiPolygon":
                singlePolygons[name] = Polygon(feature["geometry"]['coordinates'][0][0])
                polygonsInMultipolygon = [Polygon(p[0]) for p in feature["geometry"]['coordinates']]
                geometry = MultiPolygon(polygonsInMultipolygon)
                regions[name]["geometry"] = geometry

            else:
                print("OBS: region {} with geometry {}.".format(name, feature["geometry"]["type"]))


        for k1, v1 in regions.items():
            v1 = v1["geometry"]
            for k2, v2 in regions.items():
                v2 = v2["geometry"]
                if v1.touches(v2) or v1.overlaps(v2):
                    regions[k1]["neighbors"].append(k2)

        f.close()

    chunks = []
    chunk_centers = []
    searched = 0
    region_keys = list(regions.keys())
    while region_keys:
        queue = [region_keys[0]]
        visited = queue.copy()
        while queue:
            current = queue.pop(0)
            searched += 1
            region_keys.remove(current)
            for neighbor in regions[current]["neighbors"]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.append(neighbor)
        chunks.append(visited)

    dicts = []

    for region in regions.values():
        point = region["geometry"].centroid
        x, y = point.x, point.y
        region["coordinates"] = (x, y)

    chunks.sort(reverse=True, key=len)

    for chunk_index in range(len(chunks)):
        chunk = chunks[chunk_index]
        connected_geometry = []
        final_dict = {"GPS" : True, "regions" : {}, "outliers" : {}}
        for region in chunk:
            coor, nei = str(regions[region]["coordinates"]), str(regions[region]["neighbors"])
            final_dict["regions"][region] = {}
            final_dict["regions"][region]["coordinates"], \
            final_dict["regions"][region]["neighbors"] = \
            coor, nei


            connected_geometry.append(singlePolygons[region])


        entire_land_mass = MultiPolygon(connected_geometry)
        center = entire_land_mass.centroid
        chunk_centers.append((center.x, center.y))
        bounds = entire_land_mass.bounds
        search_distance_max = ( (bounds[1] - bounds[0])**2 + (bounds[3] - bounds[2])**2 )**0.5

        def getNewPoints(point1, point2):
            point3 = [(point1[0] + point2[0])/2, (point1[1] + point2[1])/2]
            p = Point(point3)
            if any([polygon.contains(p) for polygon in connected_geometry]):
                return point3, point2
            else:
                return point1, point3

        border = []
        for point in range(border_points):
            angle = ((2*pi) / border_points) * point
            x, y = center.x, center.y
            point1 = [x, y]
            point2 = [point1[0] + cos(angle) * search_distance_max, point1[1] + sin(angle) * search_distance_max]
            iterations = 100
            for iter in range(iterations):
                point1, point2 = getNewPoints(point1, point2)
            border.append(point2)


        final_dict["border"] = str(border)

        with open("maps/pre_maps/cache{}.json".format(chunk_index), "w+") as f:
            json_string = json.dumps(final_dict)
            f.seek(0); f.truncate(0)
            f.write(json_string)
            f.close()
    return len(chunks), chunk_centers, [len(chunk) for chunk in chunks]

if __name__ == "__main__":
    convertGeoJSON("maps/geojson_maps/france_regions.geojson")
