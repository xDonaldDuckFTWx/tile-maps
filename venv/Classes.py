"""
Structure:

Region -> Map -> TileMap -> OptimalMap

Map takes care of all things graph related.

METHODS AND PROPERTIES
Region:
    neighbors, neighbors_higher_id, number_of_neighbors,
    centroid, original_centroid
    name, id



Usage:
map = TileMap(dict = {"name_1": {"coordinates" : [x, y], "neighbors" : [name_2, ...], ...., border=[(x1, y1), (x2, y2), ...]}

if any landmasses not connected to main:
    map.addOutlier(closest_to_id, name)

map.updateMap()
map.getTileCoordinates()
map.convertToTileMap()

"""
from Pygame_setup import *
from shapely.geometry import Polygon, Point
from Hungarian import Hungarian


class Region:
    def __init__(self, centroid, id, name="Ö"):
        self.original_centroid = centroid
        self.centroid = centroid
        self.id = id
        self.neighbors = []
        self.neighbors_higher_id = []
        self.number_of_neighbors = 0
        self.name = name

    def addNeighbor(self, neighbor_id):
        if neighbor_id not in self.neighbors:
            self.neighbors.append(neighbor_id)
            self.number_of_neighbors += 1

    # Keeping track of neighbors with higher id helps avoid duplicates when drawing graph
    def addHighNeighbor(self, neighbor_id):
        if neighbor_id not in self.neighbors_higher_id:
            self.neighbors_higher_id.append(neighbor_id)

class Outlier:
    def __init__(self, closest_to_id, name, coordinate):
        self.closest_to_id = closest_to_id
        self.name = name
        self.centroid = coordinate

class Map:
    def __init__(self, dict=None, border=[], dictYNorth=True, dictCoordinatesGPS=True):
        self.number_of_regions = 0
        self.number_of_outliers = 0
        self.regions = []
        self.out_lier_regions = []
        self.region_index_to_tile_index = None
        if dictYNorth:
            self.border = border
        else:
            self.border = list([[x, 0-y] for x, y in border])

        if dict is not None:
            for key in dict["regions"].keys():
                x, y = dict["regions"][key]["coordinates"]
                if not dictYNorth: y = 0-y
                self.addRegion((x, y))
                self.regions[-1].name = key[:10]
            for key in dict["regions"].keys():
                for neighbor in dict["regions"][key]["neighbors"]:
                    self.addConnection(list(dict["regions"].keys()).index(key), list(dict["regions"].keys()).index(neighbor))
            for key in dict["outliers"].keys():
                self.addOutlierRegion(list(dict["regions"].keys()).index(dict["outliers"][key]["closest_to"]), dict["outliers"][key]["coordinates"], name=key)

            if dictCoordinatesGPS:
                self.transformGPStoFlat()

            self.standardize()

            """" Standardize coordinates so that all are in ([0, WIDTH], [0, HEIGHT])
            allX = [region.centroid[0] for region in self.regions] + [border_point[0] for border_point in self.border]
            allY = [region.centroid[1] for region in self.regions] + [border_point[1] for border_point in self.border]
            maxX, maxY, minX, minY = max(allX), max(allY), min(allX), min(allY)

            border_size = 75
            drawing_width = WIDTH - 2 * border_size
            drawing_height = HEIGHT - 2 * border_size

            transform_value = min(drawing_width / (maxX - minX), drawing_height / (maxY - minY))

            shiftX = 0 - minX
            shiftY = 0 - minY
            midX = (WIDTH - (maxX + shiftX) * transform_value) / 2
            midY = (HEIGHT - (maxY + shiftY) * transform_value) / 2

            for region in self.regions:
                x, y = region.centroid
                region.centroid = ((x + shiftX) * transform_value + border_size + midX,
                                   (y + shiftY) * transform_value + border_size + midY)

            for point_index in range(len(self.border)):
                x, y = self.border[point_index]
                self.border[point_index] =  ((x + shiftX) * transform_value + border_size + midX,
                                            (y + shiftY) * transform_value + border_size + midY)"""

    def transformGPStoFlat(self):
        # It is assumed all region coordinates are GPS coordinates
        coordinates = [region.centroid for region in self.regions]
        new_coordinates = []

        mapWidth, mapHeight = WIDTH, HEIGHT
        for coordinate in coordinates:
            longitude, latitude = coordinate
            x = (longitude + 180) * (mapWidth / 360)
            latRad = latitude * pi / 180
            mercN = log(tan((pi / 4) + (latRad / 2)))
            y = (mapHeight / 2) - (mapWidth * mercN / (2 * pi))
            new_coordinates.append((x, y))

        for region_index in range(self.number_of_regions):
            self.regions[region_index].centroid = new_coordinates[region_index]

        coordinates = self.border.copy()
        new_coordinates = []

        mapWidth, mapHeight = WIDTH, HEIGHT
        for coordinate in coordinates:
            longitude, latitude = coordinate
            x = (longitude + 180) * (mapWidth / 360)
            latRad = latitude * pi / 180
            mercN = log(tan((pi / 4) + (latRad / 2)))
            y = (mapHeight / 2) - (mapWidth * mercN / (2 * pi))
            new_coordinates.append([x, y])

        self.border = new_coordinates

    def standardize(self):
        allX = [region.centroid[0] for region in self.regions] + [border_point[0] for border_point in self.border]
        allY = [region.centroid[1] for region in self.regions] + [border_point[1] for border_point in self.border]
        maxX, maxY, minX, minY = max(allX), max(allY), min(allX), min(allY)

        border_size = 75
        drawing_width = WIDTH - 2 * border_size
        drawing_height = HEIGHT - 2 * border_size

        transform_value = min(drawing_width / (maxX - minX), drawing_height / (maxY - minY))

        shiftX = 0 - minX
        shiftY = 0 - minY
        midX = (WIDTH - (maxX + shiftX) * transform_value) / 2
        midY = (HEIGHT - (maxY + shiftY) * transform_value) / 2

        for region in self.regions:
            x, y = region.centroid
            region.centroid =   ((x + shiftX) * transform_value + midX,
                                (y + shiftY) * transform_value + midY)

        for point_index in range(len(self.border)):
            x, y = self.border[point_index].copy()
            self.border[point_index] =  ((x + shiftX) * transform_value + midX,
                                        (y + shiftY) * transform_value + midY)
    
    def draw(self, region_radius=10):
        self.drawing_coordinates_neighbors = []
        for region in self.regions:
            for neighbor in region.neighbors_higher_id:
                self.drawing_coordinates_neighbors.append(
                    ([int(i) for i in self.regions[region.id].centroid], [int(i) for i in self.regions[neighbor].centroid])
                )

        for pos_1, pos_2 in self.drawing_coordinates_neighbors:
            pg.draw.line(screen, (0,0,0), pos_1, pos_2)

        for region in self.regions:
            pg.draw.circle(screen, (50, 50, 90), [int(i) for i in region.centroid], region_radius)

        if self.border:
            pg.draw.lines(screen, (50,50,50), True, [[int(i) for i in coordinate] for coordinate in self.border])

    def addRegion(self, centroid):
        self.regions.append(Region(centroid, self.number_of_regions))
        self.number_of_regions += 1
    
    def addOutlierRegion(self, closest_to_id, coordinate, name=""):
        self.out_lier_regions.append(Outlier(closest_to_id, name, coordinate))
        self.number_of_outliers += 1

    def addConnection(self, id_1, id_2):
        self.regions[id_1].addNeighbor(id_2)
        self.regions[id_2].addNeighbor(id_1)

        self.regions[min(id_1, id_2)].addHighNeighbor(max(id_1, id_2))


class TileMap(Map):
    def __init__(self, dict=None, border=[], dictYNorth=True, geometry="square"):
        Map.__init__(self, dict=dict, border=border, dictYNorth=dictYNorth)
        self.geometry = geometry
        self.tile_coordinate_filled = {}
        self.tile_coordinates = []
        self.grid_shift_x, self.grid_shift_y = 0, 0
        if not border:
            raise Exception("Tile map initiated without border")
        self.getArea()
        self.region_area = 1
        #if self.geometry == "hexagon": self.region_area = 0.65
        self.stepSize = (self.area / (self.number_of_regions * self.region_area)) ** 0.5
        self.tile_map_dict = {}

    #Vector addition
    def addVectors(self, *vectors):
        result = [0,0]
        vectors = vectors[0]
        for vector in vectors:
            result[0] += vector[0]
            result[1] += vector[1]
        return result

    #sets self.area to the area contained within the country border
    def getArea(self):
        #Shoelace Theorem on border
        """area = 0
        border_points = len(self.border)
        for i in range(border_points):
            area += (self.border[i][0] * self.border[(i + 1) % border_points][1] -
                     self.border[(i + 1) % border_points][0]*self.border[i][1])
        area = abs(area)/2
        self.area = area"""
        self.border_polygon = Polygon(self.border)
        self.area = self.border_polygon.area
        self.stepSize = (self.area / self.number_of_regions) ** 0.5

    #Used for transforming centroids
    def getUji(self, ci, cj):
        subtracted = [ci[0] - cj[0], ci[1] - cj[1]]
        magnitude = max( ( subtracted[0]**2 + subtracted[1]**2 )**(0.5), 0.001)
        return [subtracted[0]/magnitude, subtracted[1]/magnitude]

    #Update the positions of the centroids
    def transform_centroids(self, noise=True):
        s = self.stepSize
        new_positions = []
        for region in self.regions:
            new = [0,0]
            for neighbor in region.neighbors:
                uji = self.getUji(region.centroid, self.regions[neighbor].centroid)
                suji = [self.stepSize * uji[0], self.stepSize * uji[1]]
                new = self.addVectors([new, suji, self.regions[neighbor].centroid])
            new = [new[0] / region.number_of_neighbors, new[1] / region.number_of_neighbors]

            new_positions.append(new)
        for i in range(self.number_of_regions):
            self.regions[i].centroid = new_positions[i]

    def getDistanceSquared(self, point_1, point_2):
        return ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)

    #Update the position of each point along the border. k = the amount of closest regions every border point takes into account.
    def transform_border(self, k):
        def M(i, k):
            border_point = self.border[i]
            distances = {}
            for q in range(self.number_of_regions):
                distances[self.getDistanceSquared(border_point, self.regions[q].centroid)] = q
            lowest_k_distances = sorted(list(distances.keys()))[:k]
            return list([distances[q] for q in lowest_k_distances])

        def getWeightsForM(m, i, k): #M is supposed to be sorted
            border_point = self.border[i]
            minimi = self.getDistanceSquared(self.regions[m[0]].centroid, border_point)
            weights = {}
            for index in m:
                weights[index] = exp(
                        0 - (self.getDistanceSquared(border_point, self.regions[index].centroid)) / (2 * minimi)
                    )

            weights_sum = sum(weights.values())
            for q in m:
                weights[q] = weights[q] / weights_sum
            return weights

        def v(weights, k, m, i):
            border_point = self.border[i]
            resultant = [0,0]
            for index in m:
                region_point = self.regions[index].centroid
                resultant[0] += (border_point[0] - region_point[0]) * weights[index]
                resultant[1] += (border_point[1] - region_point[1]) * weights[index]

            return resultant


        new_border = []
        for i in range(len(self.border)):
            m = M(i, k)
            weights = getWeightsForM(m, i, k)
            V = v(weights, k, m, i)

            res_1 = [0,0]
            for j in m:
                res_1[0] += weights[j] * self.regions[j].centroid[0]
                res_1[1] += weights[j] * self.regions[j].centroid[1]

            res_2 = (self.stepSize / self.getDistanceSquared(V, [0, 0]))**(0.5) * 2
            res_2 = [res_2 * V[0], res_2 * V[1]]

            res_final = [res_1[0] + res_2[0], res_1[1] + res_2[1]]
            new_border.append(res_final)
        self.border = new_border.copy()

    #Update centroids and border. iterations = how many iterations of centroid updates.
    #k = how many of closest regions every border point takes into account.
    #noise = True if regions begin by having their centroid shifted with Gaussian nosie.
    def updateMap(self, iterations=30, k=3, noise=True):
        if self.area == 0:
            raise Exception("Border area is 0")

        if noise:
            noise = np.random.normal(0, 0.1, self.number_of_regions * 2)
            for i in range(self.number_of_regions):
                self.regions[i].centroid = (
                self.regions[i].centroid[0] + noise[2 * i], self.regions[i].centroid[1] + noise[2 * i + 1])

        for iteration in range(iterations):
            self.transform_centroids()
        self.transform_border(k=k)
        self.standardize()
        self.getArea()
    
    #Draws grid-lines behind map
    def drawGrid(self):
        if self.geometry == "square":
            x = self.grid_shift_x % self.stepSize
            while x < WIDTH:
                X = int(x)
                pg.draw.line(screen, (100,100,100), (X, 0), (X, HEIGHT))
                x += self.stepSize
            y = self.grid_shift_y % self.stepSize
            while y < HEIGHT:
                Y = int(y)
                pg.draw.line(screen, (100,100,100), (0, Y), (WIDTH, Y))
                y += self.stepSize
        #elif self.geometry == "hexagon":

    #Get the coordinates of tiles within country border
    def getTileCoordinates(self):
        if self.geometry == "square":

            self.tile_coordinates = []
            self.tile_coordinate_filled = {}
            x = (self.grid_shift_x + self.stepSize/2) % self.stepSize
            while x < WIDTH:
                X = int(x)
                y = (self.grid_shift_y + self.stepSize/2) % self.stepSize
                while y < HEIGHT:
                    Y = int(y)
                    point = Point(x, y)

                    if point.within(self.border_polygon):
                        self.tile_coordinates.append((x, y))
                        self.tile_coordinate_filled[(x, y)] = True
                    else:
                        self.tile_coordinate_filled[(x, y)] = False

                    y += self.stepSize
                x += self.stepSize
        elif self.geometry == "hexagon":
            og_grid_shift_x = self.grid_shift_x
            self.tile_coordinates = []
            self.tile_coordinate_filled = {}
            y = (self.grid_shift_y + self.stepSize / 2) % self.stepSize
            while y < HEIGHT:
                Y = int(y)
                if self.grid_shift_x != 0: self.grid_shift_x = (self.grid_shift_x + self.stepSize / 2) % self.stepSize
                else: self.grid_shift_x = self.stepSize/2
                x = (self.grid_shift_x + self.stepSize / 2) % self.stepSize
                while x < WIDTH:
                    X = int(x)
                    point = Point(x, y)

                    if point.within(self.border_polygon):
                        self.tile_coordinates.append((x, y))
                        self.tile_coordinate_filled[(x, y)] = True
                    else:
                        self.tile_coordinate_filled[(x, y)] = False

                    x += self.stepSize
                y += self.stepSize# * 0.866
            self.grid_shift_x = og_grid_shift_x

    # Find a line-up with the current country border that fits the right amount of tile points
    def matchTilepoints(self):
        succes = False
        for grid_shift_x, grid_shift_y in [(x, y) for x in range(0, int(self.stepSize), 4) for y in range(0, int(self.stepSize), 4)]:
            self.grid_shift_x, self.grid_shift_y = grid_shift_x, grid_shift_y
            self.getTileCoordinates()
            if len(self.tile_coordinates) == self.number_of_regions:
                succes = True
                break
        return succes
        if not succes: print("Not succesful... Tiles: {}, Regions: {}".format(len(self.tile_coordinates), self.number_of_regions))

    # Draws all tile points within country border. Red if amount not matching region amount, else green.
    def drawTilepoints(self):
        if len(self.tile_coordinates) == self.number_of_regions:
            color = (50,155,50)
        else:
            color = (155, 50, 50)
        for point in self.tile_coordinates:
            x, y = [int(i) for i in point]
            pg.draw.circle(screen, color, (x, y), 2)

    # Gives every outlier a position in final map.
    def getOutLiers(self):
        for outlier in self.out_lier_regions:
         #   outlier_pos = outlier.centroid
          #  closest_region_pos = self.regions[outlier.closest_to_id].centroid
           # original_angle = asin((outlier_pos[1] - closest_region_pos[1]) / (((outlier_pos[1] - closest_region_pos[1])**2 + (outlier_pos[0] - closest_region_pos[0])**2)**0.5))

            #region_x, region_y = self.tile_coordinates[self.region_index_to_tile_index[outlier.closest_to_id]]
            # bfs utill found
            start = self.region_to_tile_coordinate[outlier.closest_to_id]
            def getNeighbors(x, y, only_adjacent=True, angle=True):
                s = self.stepSize
                if self.geometry == "square":
                    #returning = [(x + self.stepSize, y), (x - self.stepSize, y), (x, y + self.stepSize), (x, y - self.stepSize), (x + s, y + s), (x + s, y - s), (x - s, y + s), (x - s, y - s)]
                    returning = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                    if not only_adjacent: returning += [(x + 1, y - 1), (x + 1, y + 1), (x - 1, y - 1), (x - 1, y + 1)]
                    returning = [i for i in returning if (i[0] >= 0 and i[0] < self.tile_map_maxX and i[1] >= 0 and i[1] < self.tile_map_maxY)]
                    if angle:
                        #Return only those in the same direction...
                        returning = [i for i in returning if (outlier.centroid[0] - i[0] <= outlier.centroid[0] - x and outlier.centroid[1] - i[1] <= outlier.centroid[1] - y)]
                else:
                    returning = [(x + 2, y), (x - 2, y), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1), (x - 1, y - 1)]
                    returning = [i for i in returning if (i[0] >= 0 and i[0] < self.tile_map_maxX and i[1] >= 0 and i[1] < self.tile_map_maxY)]
                    if angle:
                        # Return only those in the same direction...
                        returning = [i for i in returning if (
                                    outlier.centroid[0] - i[0] <= outlier.centroid[0] - x and outlier.centroid[1] - i[
                                1] <= outlier.centroid[1] - y)]

                return returning
            visited = getNeighbors(start[0], start[1], angle=False) + [start]
            queue = getNeighbors(start[0], start[1], angle=False)
            found = False
            tested = 0
            while queue and not found:
                current = queue.pop(0)
                for x, y in getNeighbors(current[0], current[1], angle=True):
                    tested += 1
                    if not (x, y) in visited:
                        visited.append((x, y))
                        queue.append((x, y))
                        if self.tile_map_dict[(x, y)] == None:
                            if not any([self.tile_map_dict[neighbor] != None for neighbor in getNeighbors(x, y, only_adjacent=False, angle=False)]):
                                result = (x, y)
                                found = True
                                break

            x, y = result
            if self.geometry == "square"    : tile_x, tile_y = (x + 0.5) * self.stepSize, (y + 0.5) * self.stepSize
            elif self.geometry == "hexagon" : tile_x, tile_y = ((x + 0.5) * (self.stepSize*0.5)), y * (self.stepSize*0.86)

            self.tile_coordinates.append((tile_x, tile_y))
            self.regions.append(Region((tile_x, tile_y), self.number_of_regions, outlier.name))
            self.region_index_to_tile_index[self.number_of_regions] = self.number_of_regions
            self.tile_map_dict[(x, y)] = outlier.name
            self.region_to_tile_coordinate[self.number_of_regions] = (x, y)
            self.number_of_regions += 1



    # Converts to a tile map.
    def convertToTileMap(self, iterations_per_retry=5, cheate=False):
        self.getTileCoordinates()
        if len(self.tile_coordinates) != self.number_of_regions:
            print("Points and regions do not match!")
            return None
        if self.geometry == "hexagon": self.tile_coordinates = [(x, y * 0.866) for x, y in self.tile_coordinates]
        if cheate:
            self.region_index_to_tile_index = {i : i for i in range(self.number_of_regions)}
        else:
            R = self.number_of_regions
            cost_matrix = [
                [self.getDistanceSquared(self.tile_coordinates[iter_1], self.regions[iter_2].centroid) for iter_1 in
                 range(R)]
                for iter_2 in range(R)
            ]

            hungarian = Hungarian(cost_matrix)
            hungarian.calculate()
            self.tiles = hungarian.get_results()
            self.region_index_to_tile_index = {tile[0] : tile[1] for tile in self.tiles}

        while not any([tile[0] < self.stepSize for tile in self.tile_coordinates]):
            self.tile_coordinates = [[x - self.stepSize, y] for x, y in self.tile_coordinates]
        if self.geometry == "square":
            while not any([tile[1] < self.stepSize for tile in self.tile_coordinates]):
                self.tile_coordinates = [[x, y - self.stepSize] for x, y in self.tile_coordinates]
        elif self.geometry == "hexagon":
            while not any([tile[1] < self.stepSize * 0.866 for tile in self.tile_coordinates]):
                self.tile_coordinates = [[x, y - self.stepSize * 0.866] for x, y in self.tile_coordinates]

        self.region_to_tile_coordinate = {}
        if self.geometry == "square"    : self.tile_map_maxX = int(max([tile[0] for tile in self.tile_coordinates]) // self.stepSize + 2)
        elif self.geometry == "hexagon" : self.tile_map_maxX = int((max([tile[0] for tile in self.tile_coordinates])*2) // self.stepSize + 2)
        if self.geometry == "square"    : self.tile_map_maxY = int(max([tile[1] for tile in self.tile_coordinates]) // self.stepSize + 2)
        elif self.geometry == "hexagon" : self.tile_map_maxY = int(max([tile[1] for tile in self.tile_coordinates]) // (self.stepSize*0.866) + 2)
        self.tile_map_dict = {(x, y): None for x in
                              range(self.tile_map_maxX)
                              for y in
                              range(self.tile_map_maxY)}

        for region_index in range(self.number_of_regions):
            coordinate = self.tile_coordinates[self.region_index_to_tile_index[region_index]]

            if self.geometry == "square"    : coordinate = tuple(int(i / self.stepSize) for i in coordinate)
            elif self.geometry == "hexagon" :
                x, y = coordinate
                coordinate = (int((x + 0.5) / (self.stepSize*0.5)), int(y / (self.stepSize*0.86)))

            self.tile_map_dict[coordinate] = self.regions[region_index].name
            self.region_to_tile_coordinate[region_index] = coordinate

        
        if self.out_lier_regions:
            self.getOutLiers()

        if self.geometry == "hexagon":
            for region_index in range(self.number_of_regions):
                x, y = self.region_to_tile_coordinate[region_index]
                x = (x+0.5)*(self.stepSize/2)
                y = (y + 0.5) * self.stepSize * 0.866
                self.tile_coordinates[self.region_index_to_tile_index[region_index]] = [x, y]
        self.colors = [(255, 0, 0) for i in range(self.number_of_regions)]







    #Draws tile map.
    def drawTileMap(self, text=True):
        if self.region_index_to_tile_index is None:
            raise Exception("Map not converted to tile map!")
        for region_index in range(self.number_of_regions):
            tile_index = self.region_index_to_tile_index[region_index]

            if self.geometry == "square":
                X, Y = [int(i - self.stepSize / 2) for i in self.tile_coordinates[tile_index]]
                pg.draw.rect(screen, (215, 50, 50), (X, Y, self.stepSize + 1, self.stepSize + 1))
                pg.draw.rect(screen, (255, 255, 255), (X, Y, self.stepSize + 1, self.stepSize + 1), int(self.stepSize / 8))
            elif self.geometry == "hexagon":
                x, y = self.tile_coordinates[tile_index]
                X, Y = int(x), int(y)
                s = self.stepSize/2
                corner_points = [(x, y + s), (x + 0.866 * s, y + s/2), (x + 0.866 * s, y - s/2), (x, y - s), (x - 0.866 * s, y - s/2), (x - 0.866 * s, y + s/2)]
                #corner_points = [(x - s, y), (x - s/2, y + 0.866 * s), (x + s/2, y + 0.866 * s), (x + s, y), (x + s/2, y - 0.866 * s), (x - s/2, y - 0.866 * s)]
                corner_points = [(int(x), int(y)) for x, y in corner_points]
                pg.draw.polygon(screen, self.colors[region_index], corner_points)

            if text:
                myfont = pg.font.SysFont("Times New Roman", 10)

                region_name_text = myfont.render(self.regions[region_index].name, 1, (0, 0, 0))
                width, height = region_name_text.get_rect().width, region_name_text.get_rect().height
                if self.geometry == "square": text_position = (X + self.stepSize//2 - width//2, Y + self.stepSize//2 - height//2)
                elif self.geometry == "hexagon": text_position = (int( x - width / 2 ), int( y - height / 2 ))

                screen.blit(region_name_text, text_position)


    def getCost(self, distance_weight=1, adjacency_weight=1, angle_weight=1, roughness_weight=1):
        def getDistanceS(point_1, point_2):
            return (((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** 0.5) / self.stepSize

        # Distance cost
        distance_cost = 0
        for region_index in range(self.number_of_regions - self.number_of_outliers):
            region_centroid = self.regions[region_index].centroid
            tile_center = self.tile_coordinates[self.region_index_to_tile_index[region_index]]
            distanceS = getDistanceS(region_centroid, tile_center)
            distance_cost += distanceS

        # Adjacency cost
        adjacency_cost = 0
        adjacency_costs = []
        for region_index in range(self.number_of_regions - self.number_of_outliers):
            tile_center = self.tile_coordinates[self.region_index_to_tile_index[region_index]]
            score = []
            for neighbor_index in self.regions[region_index].neighbors:
                neighbor_position = self.tile_coordinates[self.region_index_to_tile_index[neighbor_index]]
                if getDistanceS(tile_center, neighbor_position) <= 1.1:
                    score.append(1)
                else:
                    score.append(0)
            score = sum(score) / len(score)
            adjacency_costs.append(score)
        adjacency_cost = sum(adjacency_costs) / len(adjacency_costs)

        # Relative orientation cost
        def getAngleDifference(new_point_1, new_point_2, old_point_1, old_point_2):
            if new_point_1[0] != new_point_2[0]:
                angle_1 = atan((new_point_2[1] - new_point_1[1]) / (new_point_2[0] - new_point_1[0]))
            else:
                angle_1 = atan((float("inf") * (new_point_2[1] - new_point_1[1])))

            if old_point_1[0] != old_point_2[0]:
                angle_2 = atan((old_point_2[1] - old_point_1[1]) / (old_point_2[0] - old_point_1[0]))
            else:
                angle_2 = atan((float("inf") * (old_point_2[1] - old_point_1[1])))

            return abs(angle_2 - angle_1)

        orientation_cost = 0
        orientation_costs = []
        for region_index in range(self.number_of_regions - self.number_of_outliers):
            orientation_errors = []
            region_old_point = self.regions[region_index].original_centroid
            region_new_point = self.tile_coordinates[self.region_index_to_tile_index[region_index]]
            for neighbor_index in self.regions[region_index].neighbors:
                neighbor_old_point = self.regions[neighbor_index].original_centroid
                neighbor_new_point = self.tile_coordinates[self.region_index_to_tile_index[neighbor_index]]

                angle_difference = getAngleDifference(region_new_point, neighbor_new_point, region_old_point, neighbor_old_point)
                orientation_errors.append(angle_difference)
            orientation_costs.append( sum(orientation_errors) / len(orientation_errors) )
        orientation_cost = sum(orientation_costs) / len(orientation_costs)

        #Roughness cost   ---- TO DO
        """roughness_cost = 0
        edges = 0
        for tile in map.tiles:
            edges += 4
            for a in [1, -1]:
                if (tile[0] + a, tile[1]) in map.tiles:
                    edges -= 1
                if (tile[0], tile[1] + a) in map.tiles:
                    edges -= 1
        P = 2 * (3.14159 * map.number_of_regions)**0.5"""
        roughness_cost = 0#(edges - P) / P

            

        total_cost = distance_cost * distance_weight + adjacency_cost * adjacency_weight + orientation_cost * angle_weight + roughness_cost * roughness_weight
        return total_cost
    
    def printDict(self):
        print("{")
        print('"geometry" : "{}",'.format(self.geometry))
        print('"regions" : ')
        print("   {")
        for region_index in range(self.number_of_regions - 1):
            print('      "{}" : {},'.format(self.regions[region_index].name, self.region_to_tile_coordinate[region_index]))
        print('      "{}" : {}'.format(self.regions[self.number_of_regions - 1].name, self.region_to_tile_coordinate[self.number_of_regions - 1]))
        print("   }")
        print("}")

    
def getMinimalCostMap(dict, border, number_of_maps, dictYNorth=True, geometry="square", distance_weight=1, adjacency_weight=1, angle_weight=1, roughness_weight=1):
    maps = [TileMap(dict=dict, border=border, dictYNorth=dictYNorth, geometry=geometry) for i in range(number_of_maps)]
    for map in maps:
        map.updateMap(iterations=150, k=4, noise=True)
        while not map.matchTilepoints():
            map.updateMap(iterations=150, k=4, noise=True)
        map.convertToTileMap()
    costs = {}
    for map_index in range(number_of_maps):
        costs[ maps[map_index].getCost(distance_weight=1, adjacency_weight=1, angle_weight=1, roughness_weight=1) ] = map_index
    minimal_cost = min(list(costs.keys()))
    return maps[costs[minimal_cost]]

