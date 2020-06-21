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
europe = {
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

european_union = {
   "geometry" : "hexagon",
   "regions" :
      {
         "Belgium" : (6, 5),
         "Bulgaria" : (15, 6),
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
         "Luxembourg" : (8, 5),
         "Lithuania" : (14, 3),
         "Latvia" : (15, 2),
         "Netherland" : (7, 4),
         "Poland" : (11, 4),
         "Portugal" : (1, 8),
         "Romania" : (16, 5),
         "Slovakia" : (14, 5),
         "Sweden" : (11, 2),
         "Slovenia" : (7, 6),
         "Ireland" : (1, 4),
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

american_continent = {
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
          "Falkland" : (13, 12),
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

asia = {
   "geometry" : "hexagon",
   "regions" :
      {
         "Afghanista" : (13, 3),
         "United Ara" : (8, 4),
         "Armenia" : (9, 1),
         "Azerbaijan" : (11, 1),
         "Bangladesh" : (16, 4),
         "Bhutan" : (14, 4),
         "China" : (17, 3),
         "Georgia" : (7, 1),
         "India" : (13, 5),
          "Sri Lanka" : (14, 6),
         "Iran" : (10, 2),
         "Iraq" : (8, 2),
         "Israel" : (3, 3),
         "Jordan" : (4, 4),
         "Kazakhstan" : (13, 1),
         "Kyrgyzstan" : (16, 2),
         "Cambodia" : (19, 5),
         "S. Korea" : (18, 2),
         "Kuwait" : (7, 3),
         "Lao PDR" : (18, 4),
         "Lebanon" : (4, 2),
         "Myanmar" : (17, 5),
         "Mongolia" : (17, 1),
         "Nepal" : (15, 3),
         "Oman" : (7, 5),
         "Pakistan" : (12, 4),
         "N. Korea" : (19, 1),
         "Palestine" : (5, 3),
         "Qatar" : (9, 3),
         "Saudi Arab" : (6, 4),
         "Syria" : (6, 2),
         "Thailand" : (18, 6),
         "Tajikistan" : (15, 1),
         "Turkmenist" : (12, 2),
         "Turkey" : (5, 1),
         "Uzbekistan" : (14, 2),
         "Vietnam" : (21, 5),
         "Yemen" : (5, 5),
         "Tiawan" : (21, 3),
         "Japan" : (23, 1),
          "Phillipines" : (25, 5),
          "Malaysia" : (19, 7),
          "Singapore" : (20, 8),
          "Brunei" : (21, 7),
          "Indonesia" : (25, 7),
          "P N Guinea" : (27, 7)
      }
}

africa = {
   "geometry" : "hexagon",
   "regions" :
      {
         "Burundi" : (17, 6),
         "Morocco" : (12, 1),
         "Mauritania" : (5, 2),
         "W. Sahara" : (6, 1),
         "Angola" : (13, 6),
         "Central Af" : (14, 5),
         "Botswana" : (15, 8),
         "Burkina Fa" : (6, 3),
         "Benin" : (10, 3),
         "Algeria" : (9, 2),
         "Ivory Coast" : (6, 5),
         "Cameroon" : (13, 4),
         "Dem. Rep. " : (15, 6),
         "Eritrea" : (15, 2),
         "Djibouti" : (18, 3),
         "Ethiopia" : (17, 4),
         "Egypt" : (17, 2),
         "Congo" : (12, 5),
         "Ghana" : (7, 4),
         "Gabon" : (11, 4),
         "Guinea" : (4, 3),
         "Gambia" : (2, 3),
         "Guinea-Bis" : (3, 4),
         "Eq. Guinea" : (9, 4),
         "Kenya" : (20, 5),
         "Liberia" : (4, 5),
         "Lesotho" : (16, 9),
         "Libya" : (13, 2),
         "Mali" : (7, 2),
         "Malawi" : (18, 7),
         "Mozambique" : (19, 8),
         "Namibia" : (14, 7),
         "Nigeria" : (12, 3),
         "Niger" : (11, 2),
         "Rwanda" : (16, 5),
         "Sudan" : (16, 3),
         "S. Sudan" : (15, 4),
         "Senegal" : (3, 2),
         "Sierra Leo" : (5, 4),
         "Somalia" : (19, 4),
         "Somaliland" : (20, 3),
         "Swaziland" : (18, 9),
         "Chad" : (14, 3),
         "Togo" : (8, 3),
         "Tunisia" : (14, 1),
         "Tanzania" : (19, 6),
         "Uganda" : (18, 5),
         "South Afri" : (17, 10),
         "Zimbabwe" : (17, 8),
         "Zambia" : (16, 7),
         "Madagascar" : (22, 7),
      }
}

usa = {
   "geometry" : "hexagon",
   "regions" :
      {
         "Maine" : (22, 1),
         "Massachuse" : (20, 1),
         "Michigan" : (13, 0),
         "Montana" : (6, 1),
         "Nevada" : (3, 2),
         "New Jersey" : (18, 1),
         "New York" : (22, 3),
         "North Caro" : (19, 4),
         "Ohio" : (14, 1),
         "Pennsylvan" : (16, 1),
         "Rhode Isla" : (21, 2),
         "Tennessee" : (12, 3),
         "Texas" : (10, 5),
         "Utah" : (5, 2),
         "Washington" : (2, 1),
         "Wisconsin" : (11, 0),
         "Maryland" : (17, 4),
         "Alabama" : (15, 4),
         "Arizona" : (4, 3),
         "Arkansas" : (9, 4),
         "California" : (2, 3),
         "Colorado" : (6, 3),
         "Connecticu" : (19, 2),
         "Delaware" : (20, 3),
         "District o" : (17, 2),
         "Florida" : (17, 6),
         "Georgia" : (16, 5),
         "Idaho" : (4, 1),
         "Illinois" : (11, 2),
         "Indiana" : (12, 1),
         "Iowa" : (10, 1),
         "Kansas" : (8, 3),
         "Kentucky" : (13, 2),
         "Louisiana" : (11, 4),
         "Minnesota" : (9, 0),
         "Mississipp" : (13, 4),
         "Missouri" : (10, 3),
         "Nebraska" : (9, 2),
         "New Hampsh" : (21, 0),
         "New Mexico" : (5, 4),
         "North Dako" : (7, 0),
         "Oklahoma" : (7, 4),
         "Oregon" : (1, 2),
         "South Caro" : (18, 5),
         "South Dako" : (8, 1),
         "Vermont" : (19, 0),
         "Virginia" : (18, 3),
         "West Virgi" : (16, 3),
         "Wyoming" : (7, 2),
         "Alaska" : (-1, 0),
         "Hawaii" : (-1, 6),
      }
}

world = {
   "geometry" : "hexagon",
   "regions" :
      {
         "Belize" : (3, 8),
         "Costa Rica" : (4, 11),
         "Guatemala" : (2, 9),
         "Honduras" : (4, 9),
         "Haiti" : (9, 8),
         "Dom R." : (11, 8),
         "Jamaica" : (7, 8),
         "Bahamas" : (5, 6),
         "Mexico" : (2, 7),
         "Cuba" : (6, 7),
         "USA" : (1, 6),
         "Canada" : (2, 5),
         "Nicaragua" : (5, 10),
         "Panama" : (6, 11),
         "El Salvado" : (3, 10),
         "Argentina" : (10, 15),
         "Bolivia" : (8, 13),
         "Brazil" : (10, 13),
         "Chile" : (9, 16),
         "Falkland" : (13, 16),
         "Colombia" : (7, 12),
         "Ecuador" : (6, 13),
         "Guyana" : (11, 12),
         "Peru" : (7, 14),
         "Paraguay" : (9, 14),
         "Suriname" : (12, 13),
         "Uruguay" : (11, 14),
         "Venezuela" : (9, 12),
"Switzerlan" : (23, 6),
         "Albania" : (31, 8),
         "Bosnia and" : (29, 6),
         "Belgium" : (24, 5),
         "Bulgaria" : (33, 6),
         "Belarus" : (31, 4),
         "Austria" : (27, 6),
         "Czech Rep." : (28, 5),
         "Germany" : (27, 4),
         "Denmark" : (28, 3),
         "Spain" : (20, 7),
         "Estonia" : (34, 1),
         "Finland" : (30, 1),
         "France" : (21, 6),
         "Greece" : (33, 8),
         "Croatia" : (26, 7),
         "Hungary" : (30, 5),
         "Italy" : (22, 7),
         "Kosovo" : (32, 7),
         "Luxembourg" : (26, 5),
         "Lithuania" : (32, 3),
         "Latvia" : (33, 2),
         "Moldova" : (33, 4),
         "Macedonia" : (30, 7),
         "Montenegro" : (28, 7),
         "Netherland" : (25, 4),
         "Norway" : (28, 1),
         "Poland" : (29, 4),
         "Portugal" : (19, 8),
         "Romania" : (34, 5),
         "Russia" : (36, 3),
         "Slovakia" : (32, 5),
         "Serbia" : (31, 6),
         "Sweden" : (29, 2),
         "Slovenia" : (25, 6),
         "Ukraine" : (34, 3),
         "Iceland" : (24, 1),
         "UK" : (21, 4),
         "Ireland" : (19, 4),
         "Turkey" : (35, 8),
"Burundi" : (33, 15),
         "Morocco" : (28, 10),
         "Mauritania" : (21, 11),
         "W. Sahara" : (22, 10),
         "Angola" : (29, 15),
         "Central Af" : (30, 14),
         "Botswana" : (31, 17),
         "Burkina Fa" : (22, 12),
         "Benin" : (26, 12),
         "Algeria" : (25, 11),
         "Ivory Coast" : (22, 14),
         "Cameroon" : (29, 13),
         "Dem. Rep. " : (31, 15),
         "Eritrea" : (31, 11),
         "Djibouti" : (34, 12),
         "Ethiopia" : (33, 13),
         "Egypt" : (33, 11),
         "Congo" : (28, 14),
         "Ghana" : (23, 13),
         "Gabon" : (27, 13),
         "Guinea" : (20, 12),
         "Gambia" : (18, 12),
         "Guinea-Bis" : (19, 13),
         "Eq. Guinea" : (25, 13),
         "Kenya" : (36, 14),
         "Liberia" : (20, 14),
         "Lesotho" : (32, 18),
         "Libya" : (29, 11),
         "Mali" : (23, 11),
         "Malawi" : (34, 16),
         "Mozambique" : (35, 17),
         "Namibia" : (30, 16),
         "Nigeria" : (28, 12),
         "Niger" : (27, 11),
         "Rwanda" : (32, 14),
         "Sudan" : (32, 12),
         "S. Sudan" : (31, 13),
         "Senegal" : (19, 11),
         "Sierra Leo" : (21, 13),
         "Somalia" : (35, 13),
         "Somaliland" : (36, 12),
         "Swaziland" : (34, 18),
         "Chad" : (30, 12),
         "Togo" : (24, 12),
         "Tunisia" : (30, 10),
         "Tanzania" : (35, 15),
         "Uganda" : (34, 14),
         "South Afri" : (33, 19),
         "Zimbabwe" : (33, 17),
         "Zambia" : (32, 16),
         "Madagascar" : (38, 16),
"Afghanista" : (49, 5),
         "United Ara" : (44, 6),
         "Armenia" : (45, 3),
         "Azerbaijan" : (47, 3),
         "Bangladesh" : (52, 6),
         "Bhutan" : (50, 6),
         "China" : (53, 5),
         "Georgia" : (43, 3),
         "India" : (49, 7),
         "Sri Lanka" : (50, 8),
         "Iran" : (46, 4),
         "Iraq" : (44, 4),
         "Israel" : (39, 5),
         "Jordan" : (40, 6),
         "Kazakhstan" : (49, 3),
         "Kyrgyzstan" : (52, 4),
         "Cambodia" : (55, 7),
         "S. Korea" : (54, 4),
         "Kuwait" : (43, 5),
         "Lao PDR" : (54, 6),
         "Lebanon" : (40, 4),
         "Myanmar" : (53, 7),
         "Mongolia" : (53, 3),
         "Nepal" : (51, 5),
         "Oman" : (43, 7),
         "Pakistan" : (48, 6),
         "N. Korea" : (55, 3),
         "Palestine" : (41, 5),
         "Qatar" : (45, 5),
         "Saudi Arab" : (42, 6),
         "Syria" : (42, 4),
         "Thailand" : (54, 8),
         "Tajikistan" : (51, 3),
         "Turkmenist" : (48, 4),
         "Turkey" : (41, 3),
         "Uzbekistan" : (50, 4),
         "Vietnam" : (57, 7),
         "Yemen" : (41, 7),
         "Tiawan" : (57, 5),
         "Japan" : (59, 3),
         "Phillipines" : (61, 7),
         "Malaysia" : (55, 9),
         "Singapore" : (56, 10),
         "Brunei" : (57, 9),
         "Indonesia" : (61, 9),
         "P N Guinea" : (63, 9),
          "Australia" : (52, 14),
          "New Zeeland" : (55, 15)
      }
}



def select(positions):
    mousex, mousey = pg.mouse.get_pos()
    distances = {}
    for region in positions.keys():
        x, y = positions[region]
        disSquared = (x - mousex) **2 + (y - mousey) **2
        distances[disSquared] = region
    minDis = min(distances.keys())
    return (distances[minDis], positions[distances[minDis]])


def drawSavedMap(dict, width=WIDTH, height=HEIGHT, text=True, transformchange=0, Xborder=10, Yborder=10):
    myfont = pg.font.SysFont("Times New Roman", 12)

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
                if event.key == pg.K_SPACE:
                    printMove(dict)
                if event.key == pg.K_1:
                    transformchange += 5
                elif event.key == pg.K_2:
                    transformchange -= 5
                elif event.key == pg.K_a:
                    Xborder += 15
                elif event.key == pg.K_d:
                    Xborder -= 15
                elif event.key == pg.K_w:
                    Yborder += 15
                elif event.key == pg.K_s:
                    Yborder -= 15
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

        border = 10
        geometry = dict["geometry"]
        regions = dict["regions"]

        maxX = max([i[0] for i in regions.values()])
        maxY = max([i[1] for i in regions.values()])

        if geometry == "hexagon": transform = min( (WIDTH - 2*border) / maxX, (HEIGHT - 2*border) / (maxY*0.866) ) + transformchange
        elif geometry == "square": transform = min( (WIDTH - 2*border) / maxX, (HEIGHT - 2*border) / maxY ) + transformchange

        positions = {}

        if geometry == "hexagon":
            for region in regions.keys():
                x, y = regions[region]
                x = x*transform*0.5 + border + Xborder
                y = y*transform*0.866 + border*0.866 + Yborder
                s = transform/2
                corner_points = [(x, y + s), (x + 0.866 * s, y + s / 2), (x + 0.866 * s, y - s / 2), (x, y - s),
                                 (x - 0.866 * s, y - s / 2), (x - 0.866 * s, y + s / 2)]
                corner_points = [(int(x), int(y)) for x, y in corner_points]
                positions[region] = (x, y)

                """if is_in_european_union[region]:
                    color = (50, 50, 150)
                else:
                    color = (255, 255, 255)"""

                color = (255, 50, 50)

                pg.draw.polygon(screen, color, corner_points)

                region_name_text = myfont.render(region[:8], 1, (255, 255, 255))

                if text:
                    width, height = region_name_text.get_rect().width, region_name_text.get_rect().height
                    text_position = (int(x - width / 2), int(y - height / 2))
                    screen.blit(region_name_text, text_position)

        elif geometry == "square":
            for region in regions.keys():
                x, y = regions[region]
                x = int(x * transform + border)
                y = int(y * transform + border)
                positions[region] = (x, y)

                """if is_in_european_union[region]:
                    color = (50, 50, 100)
                else:
                    color = (100, 50, 50)"""

                pg.draw.rect(screen, color, (x, y, int(transform - 1), int(transform-1)))

                region_name_text = myfont.render(region, 1, (0, 0, 0))

                if text:
                    width, height = region_name_text.get_rect().width, region_name_text.get_rect().height
                    text_position = (x + transform // 2 - width // 2, y + transform // 2 - height // 2)
                    screen.blit(region_name_text, text_position)

        if selecting:
            selected, pos = select(positions)
            pg.draw.circle(screen, (0,0,0), [int(i) for i in pos], 10)

        pg.display.flip()

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



#printMove(american_continent, 4, 0)
#printMove(africa, 9, 16)
#printMove(eu, 0, 18)
drawSavedMap(world, transformchange=0, text=False)
#printMove(asia, 2, 36)