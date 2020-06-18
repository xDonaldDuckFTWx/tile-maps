# tile-maps
Generate Tile Maps

Usage:
If using with current main file:
Press spacebar to update map. Use arrow keys to shift grid.
When the tile points turn from green to red, press enter.


Otherwise:

map = TileMap(dict = {"name_1": {"coordinates" : [x, y], "neighbors" : [name_2, ...], ...., border=[(x1, y1), (x2, y2), ...]}

(see Countries.py for examples of how a dict looks. "coordinates" is the coordinate of the region centroid.)

if there are any landmasses not connected to main:
    map.addOutlier(closest_to_id, name)       where closest_to_id should point to the region closest to the outlier. The id is the region's position in the map dict.


map.updateMap()
map.getTileCoordinates()
map.convertToTileMap()



OBS:
When working with maps with lots of regions, you can do

map.convertToTileMap(cheate=True)

in order to quickly preview the geometrical shape of the map. What this does is remove the assignment step of the algorithm, which means that the tiles won't have the right region assigned to them. When dealing with outliers, this will make them behave strangely.
