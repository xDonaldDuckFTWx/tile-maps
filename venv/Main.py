from Generate import *
from DrawSavedMap import *
from CreateMap import *


def main():
    create_map = CreateMap()
    #create_map.run() returns True if input was completed. If keyboard shortcut to switch app is used, returns False instead.
    if create_map.run():
        generate("maps/pre_maps/cache.json")
        drawSavedMap("maps/final_maps/cache.json")
    
    else:
        maps = ["world", "europe", "africa", "asia", "american_continent", "latin_america", "china_provinces",
                "usa_states", "india_provinces", "sweden_counties", "sweden_municipalities", "european_union_member_states",
                "europe_full", "american_continent_full", "world_full", "france_regions", "spain_provinces", "brazil_states"]
        mapfiles = ["maps/final_maps/{}.json".format(i) for i in maps]
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
            else:
                exit()

if __name__ == "__main__":
    main()