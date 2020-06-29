from Pygame_setup import *
"""
drawing = "europe_full"
# Possibilities: "world", "europe", "africa", "asia", "american_continent", "latin_america", "china_provinces",
# "usa_states", "india_provinces", "sweden_counties", "sweden_municipalities", "european_union_member_states", "europe_full"
desired_geometry = "hexagon"

"""

def select(positions):
    mousex, mousey = pg.mouse.get_pos()
    distances = {}
    for region in positions.keys():
        x, y = positions[region]
        disSquared = (x - mousex) **2 + (y - mousey) **2
        distances[disSquared] = region
    minDis = min(distances.keys())
    return (distances[minDis], positions[distances[minDis]])


def drawSavedMap(file,
                 width=WIDTH,
                 height=HEIGHT,
                 text=True,
                 transformchange=0,
                 Xborder=10,
                 Yborder=10,
                 desired_geometry="hexagon",
                 browsing = False,
                 display_name = None):
    with open(file) as f:
        tilemap = json.load(f)

    for region in tilemap["regions"].keys():
        x, y = tilemap["regions"][region][1:-1].split()
        x = x[:-1]
        tilemap["regions"][region] = (int(x), int(y))
    dict = tilemap

    running = True
    selecting = False
    selected = None
    transformchange = 0

    while running:
        pg.draw.rect(screen, (255, 255, 255), (0, 0, WIDTH, HEIGHT))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return "escape"
                if event.key == pg.K_SPACE:
                    printMove(dict)
                if event.key == pg.K_1:
                    transformchange += 5
                elif event.key == pg.K_2:
                    transformchange = transformchange - 5#max(transformchange - 5, 1 - transform)
                elif event.key == pg.K_a:
                    Xborder += 15
                elif event.key == pg.K_d:
                    Xborder -= 15
                elif event.key == pg.K_w:
                    Yborder += 15
                elif event.key == pg.K_s:
                    Yborder -= 15
                elif event.key == pg.K_t:
                    text = not text
                elif event.key == pg.K_RIGHT and browsing:
                    return "right"
                elif event.key == pg.K_LEFT and browsing:
                    return "left"
                elif event.key == pg.K_q and browsing:
                    return "back"
                if selected is not None:
                    if event.key == pg.K_RIGHT:
                        x, y = dict["regions"][selected]
                        dict["regions"][selected] = (x + 2, y)
                    if event.key == pg.K_LEFT:
                        x, y = dict["regions"][selected]
                        dict["regions"][selected] = (x - 2, y)
                    if event.key == pg.K_UP:
                        x, y = dict["regions"][selected]
                        dict["regions"][selected] = (x + 1, y - 1)
                    if event.key == pg.K_DOWN:
                        x, y = dict["regions"][selected]
                        dict["regions"][selected] = (x - 1, y + 1)

            if event.type == pg.MOUSEBUTTONDOWN:
                selecting = True
            if event.type == pg.MOUSEBUTTONUP:
                selecting = False
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            Xborder += 3
        if keys[pg.K_d]:
            Xborder -= 3
        if keys[pg.K_w]:
            Yborder += 3
        if keys[pg.K_s]:
            Yborder -= 3
        if keys[pg.K_1]:
            transformchange += 1
        if keys[pg.K_2]:
            transformchange = max(transformchange - 1, 0)


        border = 10
        geometry = dict["geometry"]
        regions = dict["regions"]

        maxX = max([i[0] for i in regions.values()])
        maxY = max([i[1] for i in regions.values()])

        if geometry == "hexagon": transform = min( (WIDTH - 2*border) / maxX, (HEIGHT - 2*border) / (maxY*0.866) ) + transformchange
        elif geometry == "square": transform = min( (WIDTH - 2*border) / maxX, (HEIGHT - 2*border) / maxY ) + transformchange

        positions = {}

        if geometry == "hexagon":
            if desired_geometry=="romb":
                for region in regions.keys():
                    x, y = regions[region]
                    x = x * transform * 0.5 + border + Xborder
                    y = y * transform * 0.866 + border * 0.866 + Yborder
                    s = transform / 2
                    corner_points = [(x, y + 1.5*s), (x + s*0.9, y), (x, y - 1.5*s), (x - s*0.9, y)]
                    corner_points = [(int(x), int(y)) for x, y in corner_points]
                    positions[region] = (x, y)

                    color = (255, 50, 50)

                    pg.draw.polygon(screen, color, corner_points)
            else:
                for region in regions.keys():
                    x, y = regions[region]
                    x = x*transform*0.5 + border + Xborder
                    y = y*transform*0.866 + border*0.866 + Yborder
                    s = transform/2
                    corner_points = [(x, y + s), (x + 0.866 * s, y + s / 2), (x + 0.866 * s, y - s / 2), (x, y - s),
                                     (x - 0.866 * s, y - s / 2), (x - 0.866 * s, y + s / 2)]
                    corner_points = [(int(x), int(y)) for x, y in corner_points]
                    positions[region] = (x, y)

                    color = (255, 50, 50)

                    pg.draw.polygon(screen, color, corner_points)

                    letters = 20
                    region_name_text = myfont.render(region[:letters], 1, (255, 255, 255))

                    if text:
                        width, height = region_name_text.get_rect().width, region_name_text.get_rect().height
                        while width > 0.866 * s * 2 - 3:
                            letters -= 1
                            region_name_text = myfont.render(region[:letters] + ".", 1, (255, 255, 255))
                            width, height = region_name_text.get_rect().width, region_name_text.get_rect().height
                        text_position = (int(x - width / 2), int(y - height / 2))
                        screen.blit(region_name_text, text_position)

        elif geometry == "square":
            for region in regions.keys():
                x, y = regions[region]
                x = int(x * transform + border)
                y = int(y * transform + border)
                positions[region] = (x, y)

                color = (255, 50, 50)
                pg.draw.rect(screen, color, (x, y, int(transform - 1), int(transform-1)))

                region_name_text = myfont.render(region, 1, (0, 0, 0))

                if text:
                    width, height = region_name_text.get_rect().width, region_name_text.get_rect().height
                    text_position = (x + transform // 2 - width // 2, y + transform // 2 - height // 2)
                    screen.blit(region_name_text, text_position)

        if selecting:
            selected, pos = select(positions)
            pg.draw.circle(screen, (0,0,0), [int(i) for i in pos], 10)

        if display_name is not None:
            display_text = myfont.render(display_name, 1, (0, 0, 0))
            screen.blit(display_text, (20, 5))

        pg.display.flip()

def printMove(file_directory_or_dict, y=0, x=0):
    try:
        with open(file_directory_or_dict) as f:
            tilemap = json.load(f)
        for region in tilemap["regions"].keys():
            X, Y = tilemap["regions"][region][1:-1].split()
            X = X[:-1]
            tilemap["regions"][region] = (int(X), int(Y))
    except TypeError:
        tilemap = file_directory_or_dict


    dict = tilemap

    print("DICT Data:")
    print("{")
    print('   "geometry" : "{}",'.format(dict["geometry"]))
    print('   "regions" : ')
    print("      {")
    for region in dict["regions"].keys():
        X, Y = dict["regions"][region]
        X += x
        Y += y
        print('         "{}" : ({}, {}),'.format(region, X, Y))
    print("      }")
    print("}")
    print("\n")
    print("JSON Data:")
    print('{}"geometry":"{}","regions":{}'.format("{", dict["geometry"], "{"), end="")
    i = 0
    for region in dict["regions"].keys():
        X, Y = dict["regions"][region]
        X += x
        Y += y
        print('"{}":"({}, {})"'.format(region, X, Y),end="")
        i += 1
        if i < len(dict["regions"].keys()):
            print(",",end="")
    print("}}")





#printMove(american_continent, 4, 0)
#printMove(africa, 9, 16)
#printMove(eu, 0, 18)
#printMove(tilemap, 5, 36) #asia

if __name__ == "__main__":
    """printMove("maps/final_maps/american_continent_full.json", 4, 0)
    printMove("maps/final_maps/africa.json", 9, 21)
    printMove("maps/final_maps/europe_full.json", 0, 24)
    printMove("maps/final_maps/asia.json", 5, 40)"""
    #printMove("maps/final_maps/oceania.json", 13, 51)
    drawSavedMap("maps/final_maps/cache.json", transformchange=0, text=True)
