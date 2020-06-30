from Classes import *
from GeoJSONconverter import *
import json
from DrawSavedMap import drawSavedMap


def createMapFromFile(directory, chunk_dist = 3, order_dist = 0, maps = 1):
    chunks_n, chunk_centers, chunk_regions_n = convertGeoJSON(directory)
    chunk_radi = [(i/pi)**0.5 for i in chunk_regions_n]
    
    for chunk_index in range(chunks_n):
        with open("maps/pre_maps/cache{}.json".format(chunk_index)) as f:
            with open("maps/cache/cache{}.json".format(chunk_index), "w+", encoding="utf-8") as c:
                j_s = getMinimalCostMap(json.load(f), maps, returnJson=True, geometry="hexagon")
                c.seek(0)
                c.truncate(0)
                c.write(j_s)
                c.close()
            f.close()

    with open("maps/cache/cache0.json", "r+") as f:
        final_dict = json.load(f)


    center = chunk_centers[0]
    rad = chunk_radi[0]
    transform_values = []
    for chunk_index in range(1, chunks_n):
        cen = chunk_centers[chunk_index]
        ang = [cen[0] - center[0], center[1] - cen[1]]
        ang2 = [i/sum([abs(k) for k in ang]) for i in ang]
        dist = rad + chunk_radi[chunk_index] + chunk_dist + chunk_index * order_dist
        transform_values.append( [int(ang2[i] * dist + rad) for i in [0,1]] )

    odd_to_odd = all([int(i)%2==0 for i in final_dict["regions"][list(final_dict["regions"].keys())[0]][1:-1].split(", ")]) or \
                 all([int(i)%2!=0 for i in final_dict["regions"][list(final_dict["regions"].keys())[0]][1:-1].split(", ")])

    occupied_coordinates = [tuple([int(i) for i in final_dict["regions"][region][1:-1].split(", ")]) for region in final_dict["regions"]]
    for c_index in range(len(occupied_coordinates)):
        x, y = occupied_coordinates[c_index]
        occupied_coordinates += [(x + 2, y), (x - 2, y), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)]
    occupied_coordinates = set(occupied_coordinates)

    for chunk_index in range(1, chunks_n):
        with open("maps/cache/cache{}.json".format(chunk_index))as f:
            chunk = json.load(f)
            print(chunk)
            regions = list(chunk["regions"].keys())

            def assign(power):
                chunk_coords = []
                for region in chunk["regions"]:
                    coords = [int(i) for i in chunk["regions"][region][1:-1].split(", ")]
                    new_coords = [int(coords[i] + transform_values[chunk_index - 1][i] * power) for i in [0,1]]
                    if odd_to_odd:
                        if new_coords[0]%2 != new_coords[1]%2:
                            new_coords[0] -= 1
                    else:
                        if new_coords[0]%2 == new_coords[1]%2:
                            new_coords[0] -= 1

                    chunk_coords.append(tuple(new_coords))
                cSet = set(chunk_coords)
                if len(cSet) + len(occupied_coordinates) == len(cSet.union(occupied_coordinates)):
                    return chunk_coords
                else:
                    return False

            pow = 1; e = False
            while e == False:
                e = assign(pow)
                pow += 0.1

            index = 0
            for region in regions:
                print(e, index)
                x, y = e[index]
                index += 1
                new_coords_string = '({}, {})'.format(x, y)
                final_dict["regions"][region] = new_coords_string
                for i in [(x + 2, y), (x - 2, y), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1), (x, y)]:
                    occupied_coordinates.add(i)
            f.close()

    minX = min([int(final_dict["regions"][region][1:-1].split(", ")[0]) for region in final_dict["regions"].keys()])
    minY = min([int(final_dict["regions"][region][1:-1].split(", ")[1]) for region in final_dict["regions"].keys()])
    for region in final_dict["regions"]:
        coords = [int(i) for i in final_dict["regions"][region][1:-1].split(", ")]
        coords[0] += abs(minX)
        coords[1] += abs(minY)
        new_coords = '({}, {})'.format(coords[0], coords[1])
        final_dict["regions"][region] = new_coords



    with open("maps/final_maps/cache.json", "r+") as f:
        jsonS = json.dumps(final_dict)
        f.seek(0)
        f.truncate(0)
        f.write(jsonS)
        f.close()



        
def chooseFileToCreate(chunk_dist = 3, order_dist = 0, maps = 1):
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    from os.path import relpath

    Tk().withdraw()
    filename = relpath(askopenfilename())  # show an "Open" dialog box and return the path to the selected file
    createMapFromFile(filename, chunk_dist, order_dist, maps)
    if drawSavedMap("maps/final_maps/cache.json") == "escape":
        return "escape"
        

if __name__ == "__main__":
    chooseFileToCreate()

