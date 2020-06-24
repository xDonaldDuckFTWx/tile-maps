from Pygame_setup import *
from Pygame_textinput import *

clock = pg.time.Clock()

class Region:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.neighbors = []



class CreateMap:
    def __init__(self, image=None, progress = None, user_friendly=True):
        self.textinput = TextInput()
        self.regions    = []
        self.selected   = []
        self.border = []
        self.mode = "region"
        self.outliers = []
        self.image = image
        self.user_friendly = user_friendly

        if progress is not None:
            if "regions" in progress.keys():
                neighbor_pairs = []
                for region in progress["regions"].keys():
                    self.regions.append(Region(region, progress["regions"][region]["coordinates"]))
                    for neighbor in progress["regions"][region]["neighbors"]:
                        neighbor_pairs.append([region, neighbor])

                for neighbor_pair in neighbor_pairs:
                    pair = [[region.name for region in self.regions].index(i) for i in neighbor_pair]
                    if pair[0] < pair[1]:
                        self.addNeighbor(pair[0], pair[1])


    def run(self):
        while True:
            if self.image is None:
                screen.fill((255, 255, 255))
            else:
                screen.blit(image, (0,0))
            if self.user_friendly:
                text = myfont.render("Draw a map! Add node: Left click (OBS: after adding region, type in name and press enter). ", 1, (0, 0, 0))
                text2 = myfont.render("Add vertice: Shift click. Draw border polygon: Ctrl click. Done? Spacebar. Switch app: Q.", 1, (0, 0, 0))
                screen.blit(text, (10,10))
                screen.blit(text2, (10,28))

            if pg.key.get_mods() & pg.KMOD_SHIFT:
                mode = "neighbor"
            elif pg.key.get_mods() & pg.KMOD_CTRL:
                mode = "border"
            else:
                mode = "region"


            self.drawRegionsNeighbors()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    self.printData()
                    self.updateCache()
                    return True
                if event.type == pg.KEYDOWN and event.key == pg.K_q:
                    return False
                if mode == "neighbor":
                    if event.type == pg.KEYUP and event.mod == pg.KMOD_SHIFT:
                        self.selected = []
                    if event.type == pg.MOUSEBUTTONDOWN:
                        self.selected.append(self.getClosestRegionToMouse())
                        if len(self.selected) == 2:
                            self.addNeighbor(self.selected[0], self.selected[1])
                            self.selected = []
                elif mode == "region":
                    if event.type == pg.MOUSEBUTTONDOWN:
                        self.addRegion()
                elif mode == "border":
                    if event.type == pg.MOUSEBUTTONDOWN:
                        x, y = pg.mouse.get_pos()
                        self.border.append([x, y])

            pygame.display.update()
            clock.tick(30)

    def drawRegionsNeighbors(self):
        for region in self.regions:
            pg.draw.circle(screen, (50, 50, 80), region.coordinates, 10)
        searched = [False for i in range(len(self.regions))]
        for region_index in range(len(self.regions)):
            if not searched[region_index]:
                queue = [region_index]
                searched[region_index] = True
                while queue:
                    cur = queue.pop(0)
                    for neighbor_index in self.regions[cur].neighbors:
                        pg.draw.line(screen, (0, 0, 0), self.regions[cur].coordinates,
                                     self.regions[neighbor_index].coordinates)
                        if not searched[neighbor_index]:
                            queue.append(neighbor_index)
                            searched[neighbor_index] = True
        if len(self.border) > 2:
            pg.draw.polygon(screen, (0,0,0), self.border, 2)



    def addRegion(self):
        x, y = pg.mouse.get_pos()
        writing = True
        self.textinput = TextInput()
        while writing:
            screen.fill((225, 225, 225))

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

            if self.textinput.update(events):
                region_name = self.textinput.get_text()
                writing = False

            screen.blit(self.textinput.get_surface(), (10, 10))
            pygame.display.update()
            clock.tick(30)
        self.regions.append(Region(region_name, [x, y]))


    def getClosestRegionToMouse(self):
        x, y = pg.mouse.get_pos()
        dist_squared = {}
        for region_index in range(len(self.regions)):
            rx, ry = self.regions[region_index].coordinates
            dist_squared[ (x - rx)**2 + (y - ry)**2 ] = region_index
        return dist_squared[min(dist_squared.keys())]

    def getClosestNonOutlierRegion(self, coordinates):
        x, y = pg.mouse.get_pos()
        dist_squared = {}
        for region_index in range(len(self.regions)):
            if len(self.regions[region_index].neighbors) != 0:
                rx, ry = self.regions[region_index].coordinates
                dist_squared[(x - rx) ** 2 + (y - ry) ** 2] = region_index
        return dist_squared[min(dist_squared.keys())]


    def addNeighbor(self, index_1, index_2):
        self.regions[index_1].neighbors.append(index_2)
        self.regions[index_2].neighbors.append(index_1)

    def printData(self):
        print("Map data:")
        print()
        print("{")
        print('   "regions" : ')
        print("   {")
        for region in self.regions :
            if len(region.neighbors) != 0:
                print('      "{}" : {}"coordinates" : {}, "neighbors" : {} {},'.format(
                    region.name, "{", region.coordinates, [self.regions[i].name for i in region.neighbors], "}"))
            else:
                self.outliers.append(region)
                self.regions.remove(region)
        print("   },")
        print('   "outliers" : ')
        print("   {")
        for region in self.regions:
            if len(region.neighbors) == 0:
                print('      "{}" : {} "coordinates" : {}, "closest_to" : "{}" ,'.format(
                    region.name, "{", region.coordinates, self.regions[self.getClosestNonOutlierRegion(region.coordinates)].name), end="")
                print(" }")
        print('   }')
        print("}")
        print()
        print("Border:")
        print(self.border)

        print("JSON Data:")
        print('{"GPS":false,"regions":{',end="")
        for region_index in range(len(self.regions)):
            region = self.regions[region_index]
            print('"{}":{}"coordinates":"{}","neighbors":"{}"{}'.format(region.name,"{", region.coordinates, [self.regions[i].name for i in region.neighbors], "}"),end="")
            if region_index < len(self.regions) - 1: print(",",end="")
        print("},",end="")
        print('"outliers":{',end="")
        for outlier_index in range(len(self.outliers)):
            region = self.outliers[outlier_index]
            print('"{}":{}"coordinates":"{}","closest_to":"{}"{}'.format(region.name, "{", region.coordinates,
                                                                         self.regions[self.getClosestNonOutlierRegion(region.coordinates)].name, "}"), end="")
            if outlier_index < len(self.outliers) - 1: print(",", end="")
        print('{},"border":"{}"{}'.format("}",self.border, "}"))

    def updateCache(self):
        jsonString = '{"GPS":false,"regions":{'
        for region_index in range(len(self.regions)):
            region = self.regions[region_index]
            jsonString += '"{}":{}"coordinates":"{}","neighbors":"{}"{}'.format(region.name, "{", region.coordinates,
                                                                    [self.regions[i].name for i in region.neighbors], "}")
            if region_index < len(self.regions) - 1: jsonString += ","
        jsonString += '},"outliers":{'
        for outlier_index in range(len(self.outliers)):
            region = self.outliers[outlier_index]
            jsonString += '"{}":{}"coordinates":"{}","closest_to":"{}"{}'.format(region.name, "{", region.coordinates,
                                                                         self.regions[self.getClosestNonOutlierRegion(
                                                                             region.coordinates)].name, "}")
            if outlier_index < len(self.outliers) - 1: jsonString += ","
        jsonString += '{},"border":"{}"{}'.format("}", self.border, "}")

        with open("maps/pre_maps/cache.json", "r+") as f:
            f.seek(0)
            f.truncate(0)
            f.write(jsonString)
            f.close()


if __name__ == "__main__":
    image = pg.image.load("images/germany.jpg")
    image = pg.transform.scale(image, (WIDTH, HEIGHT))
    create_map = CreateMap(image=image)

