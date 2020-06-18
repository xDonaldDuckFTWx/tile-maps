from Countries import printIDs, USA, USA_border, USA_border_simple, sweden, \
    sweden_border, sweden_border_medium, circle_border, sweden_municipalities, \
    south_america, south_america_border, africa, africa_border, europe, europe_border
from Classes import *

clock = pg.time.Clock()
running = True
updating = False

viewing = "sweden_counties"
geometry = "hexagon"

if viewing == "sweden_counties":
    map = getMinimalCostMap(sweden, sweden_border, 50, True, "hexagon")
    #map = TileMap(dict=sweden, border=sweden_border_medium, dictYNorth=True, geometry=geometry)
    #map.addOutlierRegion(15, name="Gotland")

elif viewing == "sweden_municipalities":
    map = getMinimalCostMap(sweden_municipalities, sweden_border, 25, True, geometry)
    #map = TileMap(dict=sweden_municipalities, border=sweden_border_medium, dictYNorth=True, geometry="hexagon")

elif viewing == "usa_states":
    map = TileMap(dict=USA, border=USA_border_simple, dictYNorth=True, geometry=geometry)

elif viewing == "south_america":
    map = TileMap(dict=south_america, border=south_america_border, dictYNorth=True, geometry=geometry)

elif viewing == "africa":
    map = TileMap(dict=africa, border=africa_border, dictYNorth=True, geometry=geometry)

elif viewing == "europe":
    map = TileMap(dict=europe, border=europe_border, dictYNorth=True, geometry=geometry)

tilemap = True

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

    pg.draw.rect(screen, (255, 255, 255), (0,0,WIDTH, HEIGHT))

    if updating:
        map.updateMap(iterations=150, k=4, noise=True)
        updating=False

    if not tilemap:
        map.getTileCoordinates()
        map.draw(region_radius=10)
        map.drawGrid()
        map.drawTilepoints()
    else:
        map.drawTileMap(text=True)

    pg.display.flip()
    clock.tick(60)