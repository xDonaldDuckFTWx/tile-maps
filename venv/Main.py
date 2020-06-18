from Countries import USA, sweden, sweden_border, sweden_border_complex, sweden_border_medium, circle_border, sweden_municipalities
from Classes import *

clock = pg.time.Clock()
running = True
updating = False

viewing = "sweden_counties"

if viewing == "sweden_counties":
    map = TileMap(dict=sweden, border=sweden_border_medium, dictYNorth=True, geometry="hexagon")
    map.addOutlierRegion(15, name="Gotland")
elif viewing == "swedden_municipalities":
    map = TileMap(dict=sweden_municipalities, border=sweden_border_medium, dictYNorth=True, geometry="square")

    map.addOutlierRegion(159, name="Öland")
    map.addOutlierRegion(289, name="Gotland")


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
        map.drawTileMap(text=False)

    pg.display.flip()
    clock.tick(60)