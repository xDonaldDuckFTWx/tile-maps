from Classes import *


def generate(file):
    clock = pg.time.Clock()
    running = True
    updating = False

    viewing = file  # options: "europe", "africa", "asia", "american_continent", "latin_america",
    # "usa_states", "india_main", "india_side", "china_provinces", "sweden_counties", "sweden_municipalities"
    geometry = "hexagon"

    with open(file) as f:
        dict = json.load(f)

    map = TileMap(dict=dict, dictYNorth=True, geometry=geometry)

    tilemap = False
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                updating = not updating
            if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                map.grid_shift_x += 5
            if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                map.grid_shift_x -= 5
            if event.type == pg.KEYDOWN and event.key == pg.K_UP:
                map.grid_shift_y -= 5
            if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                map.grid_shift_y += 5
            if event.type == pg.KEYDOWN and event.key == pg.K_0:
                map.matchTilepoints()
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                map.convertToTileMap(cheate=False)
                tilemap = True
            if event.type == pg.KEYDOWN and event.key == pg.K_9:
                map.printDict()

        pg.draw.rect(screen, (255, 255, 255), (0, 0, WIDTH, HEIGHT))

        if updating:
            map.updateMap(iterations=150, k=4, noise=True)
            updating = False

        if not tilemap:
            map.getTileCoordinates()
            map.draw(region_radius=10)
            map.drawGrid()
            map.drawTilepoints()
        else:
            map.drawTileMap(text=True)
            jsonString = '{}"geometry":"{}","regions":{}'.format("{", map.geometry, "{")

            for region_index in range(map.number_of_regions - 1):
                region = map.regions[region_index]
                jsonString += '"{}":"{}",'.format(region.name, map.region_to_tile_coordinate[region_index])
            jsonString += '"{}":"{}"{}'.format(map.regions[-1].name,
                                               map.region_to_tile_coordinate[map.number_of_regions - 1], "}}")
            with open("maps/final_maps/cache.json", "r+") as f:
                f.seek(0)
                f.truncate(0)
                f.write(jsonString)
                f.close()

            return map

        pg.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    generate("asia")