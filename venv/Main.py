from Generate import *
from DrawSavedMap import *
from CreateMap import *
import os


def main():
    create_map = CreateMap()
    #create_map.run() returns True if input was completed. If keyboard shortcut to switch app is used, returns False instead.
    c = create_map.run()
    if c==True:
        generate("maps/pre_maps/cache.json")
        drawSavedMap("maps/final_maps/cache.json")
    elif c=="escape":
        return "escape"
    
def browse():
    rootdir = __file__.replace("Main.py", "") + "maps/final_maps"
    # 'C:/Users/olle.lapidus/PycharmProjects/tile-maps/venv/maps/final_maps'
    maps = []
    mapfiles = []
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            mapfiles.append(os.path.join(subdir, file))
            maps.append(subdir.replace(rootdir, "")[1:] + "_" + file.replace(".json", ""))

    """maps = ["world", "europe", "africa", "asia", "american_continent", "latin_america", "china_provinces",
            "usa_states", "india_provinces", "sweden_counties", "sweden_municipalities", "european_union_member_states",
            "europe_full", "american_continent_full", "world_full", "france_regions", "spain_provinces", "brazil_states",
            "denmark_municipalities", "austria_states", "ireland_counties", "greece_regions", "turkey", "italy_provinces",
            "italy_regions", "japan", "liberia_regions", "luxembourg_communes", "luxembourg_cantones", "malaysia_regions",
            "mexico_states", "oman_provinces", "oman_regions", "pakistan_regions", "poland_regions", "portugal_regions",
            "romania_regions", "serbia_regions", "south_africa_regions", "spain_communities", "netherlands_regions",
            "england_regions"]
    mapfiles = ["maps/final_maps/{}.json".format(i) for i in maps]"""
    browsing_index = 0

    while True:
        change =  drawSavedMap(mapfiles[browsing_index], browsing=True, display_name = maps[browsing_index], text=True)
        # drawSavedMap() returns different keyword depending on which event exited the program.
        if change == "right":
            browsing_index = (browsing_index + 1) % len(mapfiles)
        elif change == "left":
            browsing_index = (browsing_index - 1) % len(mapfiles)
        elif change == "back":
            main()
        elif change == "escape":
            return "escape"
        else:
            exit()

if __name__ == "__main__":
    main()