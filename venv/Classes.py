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
    def __init__(self, closest_to_id, name):
        self.closest_to_id = closest_to_id
        self.name = name

class Map:
    def __init__(self, dict=None, border=[], dictYNorth=True, dictCoordinatesGPS=True):
        self.number_of_regions = 0
        self.regions = []
        self.out_lier_regions = []
        self.region_index_to_tile_index = None
        if dictYNorth:
            self.border = border
        else:
            self.border = list([(x, 0-y) for x, y in border])

        if dict is not None:
            for key in dict.keys():
                x, y = dict[key]["coordinates"]
                if not dictYNorth: y = 0-y
                self.addRegion((x, y))
                self.regions[-1].name = key[:10]
            for key in dict.keys():
                for neighbor in dict[key]["neighbors"]:
                    self.addConnection(list(dict.keys()).index(key), list(dict.keys()).index(neighbor))

            if dictCoordinatesGPS:
                self.transformGPStoFlat()

            # Standardize coordinates so that all are in ([0, WIDTH], [0, HEIGHT])
            allX = [region.centroid[0] for region in self.regions] + [border_point[0] for border_point in self.border]
            allY = [region.centroid[1] for region in self.regions] + [border_point[1] for border_point in self.border]
            maxX, maxY, minX, minY = max(allX), max(allY), min(allX), min(allY)

            border_size = 25
            drawing_width = WIDTH - 2 * border_size
            drawing_height = HEIGHT - 2 * border_size

            transform_value = min(drawing_width / (maxX - minX), drawing_height / (maxY - minY))

            shiftX = 0 - minX
            shiftY = 0 - minY
            midX = (maxX - minX) // 2
            midY = (maxY - minY) // 2

            for region in self.regions:
                x, y = region.centroid
                region.centroid = ((x + shiftX) * transform_value + border_size + midX,
                                   (y + shiftY) * transform_value + border_size + midY)

            for point_index in range(len(self.border)):
                x, y = self.border[point_index]
                self.border[point_index] =  ((x + shiftX) * transform_value + border_size,
                                            (y + shiftY) * transform_value + border_size)

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
            new_coordinates.append((x, y))

        self.border = new_coordinates

    def standardize(self):
        allX = [region.centroid[0] for region in self.regions] + [border_point[0] for border_point in self.border]
        allY = [region.centroid[1] for region in self.regions] + [border_point[1] for border_point in self.border]
        maxX, maxY, minX, minY = max(allX), max(allY), min(allX), min(allY)

        border_size = 25
        drawing_width = WIDTH - 2 * border_size
        drawing_height = HEIGHT - 2 * border_size

        transform_value = min(drawing_width / (maxX - minX), drawing_height / (maxY - minY))

        shiftX = 0 - minX
        shiftY = 0 - minY
        midX = (WIDTH + minX - maxX) / 2
        midY = (HEIGHT - maxY + minY) / 2

   #     midX = (maxX - minX) // 2
    #    midY = (maxY - minY) // 2

        for region in self.regions:
            x, y = region.centroid
            region.centroid =   ((x + shiftX) * transform_value + midX,
                                (y + shiftY) * transform_value + border_size)

        for point_index in range(len(self.border)):
            x, y = self.border[point_index].copy()
            self.border[point_index] =  ((x + shiftX) * transform_value + midX,
                                        (y + shiftY) * transform_value + border_size)
    
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
    
    def addOutlierRegion(self, closest_to_id, name=""):
        self.out_lier_regions.append(Outlier(closest_to_id, name))

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
        if self.geometry == "hexagon": self.region_area = 0.65
        self.stepSize = (self.area / (self.number_of_regions * self.region_area)) ** 0.5

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

#            new = self.addVectors([self.addVectors([self.regions[i].centroid for i in region.neighbors]),
 #                 [s * q for q in self.addVectors([self.getUji(region.centroid, self.regions[i].centroid) for i in region.neighbors])]])
  #          new[0], new[1] = int((1 / region.number_of_neighbors) * new[0]), int((1 / region.number_of_neighbors) * new[1])
   #         print(new)

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
                y += self.stepSize * 0.866
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
        if not succes: print("Not succesful...")

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
            # bfs utill found
            start = self.tile_coordinates[self.region_index_to_tile_index[outlier.closest_to_id]]
            def getNeighbors(x, y):
                s = self.stepSize
                returning = [(x + self.stepSize, y), (x - self.stepSize, y), (x, y + self.stepSize), (x, y - self.stepSize), (x + s, y + s), (x + s, y - s), (x - s, y + s), (x - s, y - s)]
                returning = [i for i in returning if (i[0] > 0 and i[0] < WIDTH and i[1] > 0 and i[1] < HEIGHT)]
                return returning
            visited = getNeighbors(start[0], start[1]) + [start]
            queue = getNeighbors(start[0], start[1])
            found = False
            tested = 0
            while queue and not found:
                current = queue.pop(0)
                for x, y in getNeighbors(current[0], current[1]):
                    tested += 1
                    if not (x, y) in visited:
                        visited.append((x, y))
                        queue.append((x, y))
                        if not (x, y) in self.tile_coordinates:
                            if not any([neighbor in self.tile_coordinates for neighbor in getNeighbors(x, y)]):
                                result = (x, y)
                                found = True
                                break
            self.tile_coordinates.append((x, y))
            self.regions.append(Region((x, y), self.number_of_regions, outlier.name))
            self.region_index_to_tile_index[self.number_of_regions] = self.number_of_regions
            self.number_of_regions += 1



    # Converts to a tile map.
    def convertToTileMap(self, iterations_per_retry=5, cheate=False):
        self.getTileCoordinates()
        if len(self.tile_coordinates) != self.number_of_regions:
            print("Points and regions do not match!")
            return None
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

        if self.out_lier_regions:
            self.getOutLiers()

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
                s = self.stepSize/2
                corner_points = [(x, y + s), (x + 0.866 * s, y + s/2), (x + 0.866 * s, y - s/2), (x, y - s), (x - 0.866 * s, y - s/2), (x - 0.866 * s, y + s/2)]
                #corner_points = [(x - s, y), (x - s/2, y + 0.866 * s), (x + s/2, y + 0.866 * s), (x + s, y), (x + s/2, y - 0.866 * s), (x - s/2, y - 0.866 * s)]
                corner_points = [(int(x), int(y)) for x, y in corner_points]
                pg.draw.polygon(screen, (215, 50, 50), corner_points)

            if text:
                myfont = pg.font.SysFont("Times New Roman", 10)

                region_name_text = myfont.render(self.regions[region_index].name, 1, (0, 0, 0))
                width, height = region_name_text.get_rect().width, region_name_text.get_rect().height
                text_position = (X + self.stepSize//2 - width//2, Y + self.stepSize//2 - height//2)

                screen.blit(region_name_text, text_position)

    
        

