from Pygame_setup import *

myfont = pg.font.SysFont("Times New Roman", 15)

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
eu = {
"geometry" : "hexagon",
"regions" :
   {
      "Switzerlan" : (5, 6),
      "Albania" : (13, 8),
      "Bosnia and" : (11, 6),
      "Belgium" : (6, 5),
      "Bulgaria" : (15, 6),
      "Belarus" : (13, 4),
      "Austria" : (9, 6),
      "Czech Rep." : (10, 5),
      "Germany" : (9, 4),
      "Denmark" : (10, 3),
      "Spain" : (2, 7),
      "Estonia" : (16, 1),
      "Finland" : (12, 1),
      "France" : (3, 6),
      "Greece" : (15, 8),
      "Croatia" : (8, 7),
      "Hungary" : (12, 5),
      "Italy" : (4, 7),
      "Kosovo" : (14, 7),
      "Luxembourg" : (8, 5),
      "Lithuania" : (14, 3),
      "Latvia" : (15, 2),
      "Moldova" : (15, 4),
      "Macedonia" : (12, 7),
      "Montenegro" : (10, 7),
      "Netherland" : (7, 4),
      "Norway" : (10, 1),
      "Poland" : (11, 4),
      "Portugal" : (1, 8),
      "Romania" : (16, 5),
      "Russia" : (18, 3),
      "Slovakia" : (14, 5),
      "Serbia" : (13, 6),
      "Sweden" : (11, 2),#(13, 0),
      "Slovenia" : (7, 6),
      "Ukraine" : (16, 3),
        "Iceland" : (6, 1),
       "UK" : (3, 4),
       "Ireland" : (1, 4),
       "Turkey" : (17, 8)
   }
}

is_in_european_union = {
"Switzerlan" : False,
      "Albania" : False,
      "Bosnia and" : False,
      "Belgium" : True,
      "Bulgaria" : True,
      "Belarus" : False,
      "Austria" : True,
      "Czech Rep." : True,
      "Germany" : True,
      "Denmark" : True,
      "Spain" : True,
      "Estonia" : True,
      "Finland" : True,
      "France" : True,
      "Greece" : True,
      "Croatia" : True,
      "Hungary" : True,
      "Italy" : True,
      "Kosovo" : False,
      "Luxembourg" : True,
      "Lithuania" : True,
      "Latvia" : True,
      "Moldova" : False,
      "Macedonia" : False,
      "Montenegro" : False,
      "Netherland" : True,
      "Norway" : False,
      "Poland" : True,
      "Portugal" : True,
      "Romania" : True,
      "Russia" : False,
      "Slovakia" : True,
      "Serbia" : False,
      "Sweden" : True,
      "Slovenia" : True,
      "Ukraine" : False,
        "Iceland" : False,
       "UK" : False,
       "Ireland" : True,
    "Turkey" : False
}


latin_america = {
"geometry" : "hexagon",
"regions" :
   {
      "Belize" : (4, 0),
      "Costa Rica" : (7, 3),
      "Guatemala" : (5, 1),
      "Honduras" : (7, 1),
      "Mexico" : (2, 0),
      "Nicaragua" : (8, 2),
      "Panama" : (9, 3),
      "El Salvado" : (6, 2),
      "Argentina" : (13, 7),
      "Bolivia" : (11, 5),
      "Brazil" : (13, 5),
      "Chile" : (12, 8),
      "Colombia" : (10, 4),
      "Ecuador" : (9, 5),
      "Guyana" : (14, 4),
      "Peru" : (10, 6),
      "Paraguay" : (12, 6),
      "Suriname" : (15, 5),
      "Uruguay" : (14, 6),
      "Venezuela" : (12, 4)
   }
}

latin_america = {
   "geometry" : "hexagon",
   "regions" :
      {
         "Belize" : (3, 4),
         "Costa Rica" : (4, 7),
         "Guatemala" : (2, 5),
         "Honduras" : (4, 5),
         "Haiti" : (9, 4),
         "Dom R." : (11, 4),
         "Jamaica" : (7, 4),
         "Bahamas" : (5, 2),
         "Mexico" : (2, 3),
         "Cuba" : (6, 3),
         "USA" : (1, 2),
         "Canada" : (2, 1),
         "Nicaragua" : (5, 6),
         "Panama" : (6, 7),
         "El Salvado" : (3, 6),
         "Argentina" : (10, 11),
         "Bolivia" : (8, 9),
         "Brazil" : (10, 9),
         "Chile" : (9, 12),
         "Colombia" : (7, 8),
         "Ecuador" : (6, 9),
         "Guyana" : (11, 8),
         "Peru" : (7, 10),
         "Paraguay" : (9, 10),
         "Suriname" : (12, 9),
         "Uruguay" : (11, 10),
         "Venezuela" : (9, 8)
      }
}


def drawSavedMap(dict, width=WIDTH, height=HEIGHT, text=True, transformchange=0):
    border = 2
    geometry = dict["geometry"]
    regions = dict["regions"]

    maxX = max([i[0] for i in regions.values()])
    maxY = max([i[1] for i in regions.values()])

    if geometry == "hexagon": transform = min( (WIDTH - 2*border) / maxX, (HEIGHT - 2*border) / (maxY*0.866) ) + transformchange
    elif geometry == "square": transform = min( (WIDTH - 2*border) / maxX, (HEIGHT - 2*border) / maxY ) + transformchange

    if geometry == "hexagon":
        for region in regions.keys():
            x, y = regions[region]
            x = x*transform*0.5 + border
            y = y*transform*0.866 + border
            s = transform/2
            corner_points = [(x, y + s), (x + 0.866 * s, y + s / 2), (x + 0.866 * s, y - s / 2), (x, y - s),
                             (x - 0.866 * s, y - s / 2), (x - 0.866 * s, y + s / 2)]
            corner_points = [(int(x), int(y)) for x, y in corner_points]

            if is_in_european_union[region]:
                color = (50, 50, 150)
            else:
                color = (150, 50, 50)

            #color = (255, 50, 50)

            pg.draw.polygon(screen, color, corner_points)

            region_name_text = myfont.render(region, 1, (255, 255, 255))

            if text:
                width, height = region_name_text.get_rect().width, region_name_text.get_rect().height
                text_position = (int(x - width / 2), int(y - height / 2))
                screen.blit(region_name_text, text_position)

    elif geometry == "square":
        for region in regions.keys():
            x, y = regions[region]
            x = int(x * transform + border)
            y = int(y * transform + border)

            if is_in_european_union[region]:
                color = (50, 50, 100)
            else:
                color = (100, 50, 50)

            pg.draw.rect(screen, color, (x, y, int(transform - 1), int(transform-1)))

            region_name_text = myfont.render(region, 1, (0, 0, 0))

            if text:
                width, height = region_name_text.get_rect().width, region_name_text.get_rect().height
                text_position = (x + transform // 2 - width // 2, y + transform // 2 - height // 2)
                screen.blit(region_name_text, text_position)

def printMove(dict, y=0, x=0):
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


running = True
transformchange = 0

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                transformchange += 5

    pg.draw.rect(screen, (255, 255, 255), (0, 0, WIDTH, HEIGHT))
    drawSavedMap(eu, transformchange=transformchange)

    pg.display.flip()