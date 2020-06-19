from Pygame_setup import *

lan = {
"geometry" : "hexagon",
"regions" : 
   {
      "Norrbotten" : (5, 0),
      "Västerbott" : (3, 0),
      "Västernorr" : (4, 1),
      "Jämtland" : (2, 1),
      "Gävleborg" : (3, 2),
      "Dalarna" : (2, 3),
      "Uppsala" : (5, 2),
      "Värmland" : (1, 4),
      "Västmanlan" : (4, 3),
      "Stockholms" : (7, 4),
      "Örebro" : (3, 4),
      "Södermanla" : (5, 4),
      "Östergötla" : (4, 5),
      "Jönköping" : (2, 5),
      "Västra Göt" : (0, 5),
      "Kalmar" : (3, 6),
      "Halland" : (1, 6),
      "Kronoberg" : (2, 7),
      "Blekinge" : (4, 7),
      "Skåne" : (1, 8),
      "Gotland" : (7, 6)
   }
}
lan2 = {
"geometry" : "square",
"regions" :
   {
      "Norrbotten" : (2, 0),
      "Västerbott" : (1, 0),
      "Västernorr" : (2, 1),
      "Jämtland" : (1, 1),
      "Gävleborg" : (2, 2),
      "Dalarna" : (1, 2),
      "Uppsala" : (2, 3),
      "Värmland" : (1, 3),
      "Västmanlan" : (2, 4),
      "Stockholms" : (3, 4),
      "Örebro" : (1, 4),
      "Södermanla" : (2, 5),
      "Östergötla" : (1, 5),
      "Jönköping" : (1, 6),
      "Västra Göt" : (0, 5),
      "Kalmar" : (2, 6),
      "Halland" : (0, 6),
      "Kronoberg" : (1, 7),
      "Blekinge" : (2, 7),
      "Skåne" : (1, 8),
      "Gotland" : (4, 6)
   }
}

def drawSavedMap(dict, width=WIDTH, height=HEIGHT):
    border = 100
    geometry = dict["geometry"]
    regions = dict["regions"]

    maxX = max([i[0] for i in regions.values()])
    maxY = max([i[1] for i in regions.values()])

    if geometry == "hexagon": transform = min( (WIDTH - 2*border) / maxX, (HEIGHT - 2*border) / (maxY*0.866) )
    elif geometry == "square": transform = min( (WIDTH - 2*border) / maxX, (HEIGHT - 2*border) / maxY )

    if geometry == "hexagon":
        for region in regions.keys():
            x, y = regions[region]
            x = x*transform*0.5 + border
            y = y*transform*0.866 + border
            s = transform/2
            corner_points = [(x, y + s), (x + 0.866 * s, y + s / 2), (x + 0.866 * s, y - s / 2), (x, y - s),
                             (x - 0.866 * s, y - s / 2), (x - 0.866 * s, y + s / 2)]
            corner_points = [(int(x), int(y)) for x, y in corner_points]
            pg.draw.polygon(screen, (255, 0, 0), corner_points)
    elif geometry == "square":
        for region in regions.keys():
            x, y = regions[region]
            x = int(x * transform + border)
            y = int(y * transform + border)
            pg.draw.rect(screen, (255, 0, 0), (x, y, int(transform - 1), int(transform-1)))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.draw.rect(screen, (255, 255, 255), (0, 0, WIDTH, HEIGHT))
    drawSavedMap(lan2)

    pg.display.flip()