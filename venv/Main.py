from Generate import *
from DrawSavedMap import *
from CreateMap import *


def main():
    create_map = CreateMap()
    if create_map.run():
        generate("maps/pre_maps/cache.json")
        drawSavedMap("maps/final_maps/cache.json")
    
    else:
        maps = ["world", "europe", "africa", "asia", "american_continent", "latin_america", "china_provinces",
     "usa_states", "india_provinces", "sweden_counties", "sweden_municipalities", "european_union_member_states", "europe_full"]
        mapfiles = ["maps/final_maps/{}.json".format(i) for i in maps]
        index = 0
        while True:
            change =  drawSavedMap(mapfiles[index], browsing=True, display_name = maps[index])
            if change == "right":
                index = (index + 1) % len(mapfiles)
            elif change == "left":
                index = (index - 1) % len(mapfiles)
            elif change == "back":
                main()
            else:
                exit()

if __name__ == "__main__":
    main()