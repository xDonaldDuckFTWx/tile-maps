from Classes import *
from GeoJSONconverter import *
import json


def createMapFromFile(directory, chunk_dist = 8, order_dist = 0):
    chunks_n, chunk_centers, chunk_regions_n = convertGeoJSON(directory)
    chunk_radi = [(i/pi)**0.5 for i in chunk_regions_n]
    
    for chunk_index in range(chunks_n):
        with open("maps/pre_maps/cache{}.json".format(chunk_index)) as f:
            with open("maps/cache/cache{}.json".format(chunk_index), "w+") as c:
                j_s = getMinimalCostMap(json.load(f), 1, returnJson=True, geometry="hexagon")
                c.seek(0)
                c.truncate(0)
                c.write(j_s)
                c.close()
            f.close()

    with open("maps/cache/cache0.json", "r+") as f:
        final_dict = json.load(f)

    print(final_dict)

    center = chunk_centers[0]
    rad = chunk_radi[0]
    transform_values = []
    for chunk_index in range(1, chunks_n):
        cen = chunk_centers[chunk_index]
        ang = [cen[0] - center[0], center[1] - cen[1]]
        ang2 = [i/sum([abs(k) for k in ang]) for i in ang]
        dist = rad + chunk_radi[chunk_index] + chunk_dist + chunk_index * order_dist
        print(ang, ang2)
        transform_values.append( [int(ang2[i] * dist + rad) for i in [0,1]] )

    odd_to_odd = all([int(i)%2==0 for i in final_dict["regions"][list(final_dict["regions"].keys())[0]][1:-1].split(", ")]) or \
                 all([int(i)%2!=0 for i in final_dict["regions"][list(final_dict["regions"].keys())[0]][1:-1].split(", ")])
    
    for chunk_index in range(1, chunks_n):
        with open("maps/cache/cache{}.json".format(chunk_index))as f:
            chunk = json.load(f)
            for region in chunk["regions"]:
                coords = [int(i) for i in chunk["regions"][region][1:-1].split(", ")]
                new_coords = [coords[i] + transform_values[chunk_index - 1][i] for i in [0,1]]
                if odd_to_odd:
                    if new_coords[0]%2 != new_coords[1]%2:
                        new_coords[0] -= 1
                else:
                    if new_coords[0]%2 == new_coords[1]%2:
                        new_coords[0] -= 1

                new_coords_string = '({}, {})'.format(new_coords[0], new_coords[1])
                final_dict["regions"][region] = new_coords_string
            f.close()

    print(final_dict)
    minX = min([int(final_dict["regions"][region][1:-1].split(", ")[0]) for region in final_dict["regions"].keys()])
    minY = min([int(final_dict["regions"][region][1:-1].split(", ")[1]) for region in final_dict["regions"].keys()])
    print(minX, minY)
    for region in final_dict["regions"]:
        coords = [int(i) for i in final_dict["regions"][region][1:-1].split(", ")]
        coords[0] += abs(minX)
        coords[1] += abs(minY)
        new_coords = '({}, {})'.format(coords[0], coords[1])
        final_dict["regions"][region] = new_coords

    print(final_dict)


    with open("maps/final_maps/cache.json", "r+") as f:
        jsonS = json.dumps(final_dict)
        f.seek(0)
        f.truncate(0)
        f.write(jsonS)
        f.close()



        
        
        
        

if __name__ == "__main__":
    createMapFromFile("maps/geojson_maps/brazil_states.geojson")