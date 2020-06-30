from Pygame_setup import *
"""
drawing = "europe_full"
# Possibilities: "world", "europe", "africa", "asia", "american_continent", "latin_america", "china_provinces",
# "usa_states", "india_provinces", "sweden_counties", "sweden_municipalities", "european_union_member_states", "europe_full"
desired_geometry = "hexagon"

"""

def select(positions, rect_bounds):
    selected = []
    for region in positions.keys():
        x, y = positions[region]
        if x > rect_bounds[0] and y > rect_bounds[1] and x < rect_bounds[2] and y < rect_bounds[3]:
            selected.append(region)
    return selected

class SaveButton:
    def __init__(self):
        self.rect = (WIDTH - 100, 20, 80, 65)
        self.text = myfont.render("SAVE", 1, (0, 0, 0))
        self.reg_color = (164, 231, 141)
        self.hover_color = (120, 165, 110)
        self.hovering = False

    def draw(self):
        button = pg.Surface((self.rect[2], self.rect[3]))
        if not self.hovering:
            button.set_alpha(120)
            button.fill(self.reg_color)
        else:
            button.fill(self.hover_color)
        button.blit(self.text, ((self.rect[2]-self.text.get_rect().width)//2 ,
                                (self.rect[3]-self.text.get_rect().height)//2))
        screen.blit(button, (self.rect[0], self.rect[1]))

    def updateHovering(self, mouse_x, mouse_y):
        self.hovering = mouse_x > self.rect[0] and mouse_x < self.rect[0] + self.rect[2] and \
        mouse_y > self.rect[1] and mouse_y < self.rect[1] + self.rect[3]

    def save(self, directory, dict):
        with open(directory, "w+") as f:
            #f.seek(0)
            #f.truncate(0)
            new_d = dict
            for region in new_d["regions"]:
                new_d["regions"][region] = "({}, {})".format(dict["regions"][region][0], dict["regions"][region][1])
            print(json.dumps(new_d))
            f.write(json.dumps(new_d))
            f.close()
        running = False



save_button = SaveButton()

def editSavedMap(file,
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
    selected = []
    transformchange = 0

    while running:
        pg.draw.rect(screen, (255, 255, 255), (0, 0, WIDTH, HEIGHT))
        mouse_x, mouse_y = pg.mouse.get_pos()
        save_button.updateHovering(mouse_x, mouse_y)

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
                if selected:
                    if event.key == pg.K_RIGHT:
                        for selec in selected:
                            x, y = dict["regions"][selec]
                            dict["regions"][selec] = (x + 2, y)
                    if event.key == pg.K_LEFT:
                        for selec in selected:
                            x, y = dict["regions"][selec]
                            dict["regions"][selec] = (x - 2, y)
                    if event.key == pg.K_UP:
                        for selec in selected:
                                x, y = dict["regions"][selec]
                                dict["regions"][selec] = (x + 1, y - 1)
                    if event.key == pg.K_DOWN:
                        for selec in selected:
                            x, y = dict["regions"][selec]
                            dict["regions"][selec] = (x - 1, y + 1)

            if event.type == pg.MOUSEBUTTONDOWN:
                selecting = True
                x_first, y_first = mouse_x, mouse_y
                if save_button.hovering:
                    save_button.save(file, dict)
                    running = False
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

        if not running:
            break

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

        save_button.draw()

        if selecting:
            x_second, y_second = mouse_x, mouse_y
            x_s, x_b = min(x_first, x_second), max(x_first, x_second)
            y_s, y_b = min(y_first, y_second), max(y_first, y_second)
            selected = select(positions, (x_s, y_s, x_b, y_b))

            selected_rect = pg.Surface((x_b - x_s, y_b - y_s))
            selected_rect.set_alpha(100)
            selected_rect.fill((200, 200, 248))
            screen.blit(selected_rect, (x_s, y_s))
        for i in selected:
            pg.draw.circle(screen, (0,0,0), [int(k) for k in positions[i]], 10)

        if display_name is not None:
            display_text = myfont.render(display_name, 1, (0, 0, 0))
            screen.blit(display_text, (20, 5))

        pg.display.flip()



if __name__ == "__main__":
    editSavedMap("maps/final_maps/cache.json", transformchange=0, text=True)
