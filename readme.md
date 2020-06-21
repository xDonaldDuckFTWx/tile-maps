# tile-maps
Generate Tile Maps

Usage:
If using with current main file:
Press spacebar to update map. Use arrow keys to shift grid.
When the tile points turn from green to red, press enter.


Otherwise:

map = TileMap(
  dict = {
    "regions" : {"name_1": {"coordinates" : [x, y], "neighbors" : [name_2, ...], ...., border=[(x1, y1), (x2, y2), ...]}},
    "outliers" : {"outlier_1" : {"coordinates" : [x, y], "closest_to" : "name_1"}, ....}     #closest_to refers to region closest to outlier
  }
  border = [(x, y), (x2, y2), (x3, y3), ...]     #corner points of border polygon
  )

see Countries.py for examples of how a dict looks. "coordinates" is the coordinate of the region centroid.

map.updateMap()
map.getTileCoordinates()
map.convertToTileMap()




When working with maps with lots of regions, you can do

map.convertToTileMap(cheate=True)

in order to quickly preview the geometrical shape of the map. What this does is remove the assignment step of the algorithm, which means that the tiles won't have the right region assigned to them. When dealing with outliers, this will make them behave strangely.

To print out dict for map, press 9.



To view preset maps:
Run DrawSavedMap.py
with:
drawSavedMap(saved_map, transformchange=0, text=bool)

Key shortcuts: WASD moves screen, 1,2 zooms, mouse and arrow keys edits maps, spacebar prints edited map.
