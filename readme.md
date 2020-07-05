# tile-maps
Generate Tile Maps

# Usage:
run:
python GUI.py

Use arrow keys and enter to choose app.

## Apps

### Draw Graph map...
In this app you draw a graph with an enclosing border. Nodes represent regions, and edges a connection between two regions.
Add node: Click mouse button (you will then be asked to name node, type name and press enter).
Add edge between nodes: Shift click mouse button on the two desired nodes.
Draw border: Ctrl click mouse button. Every click creates a new corner in border polygon.

When finished drawing, press space to start generating map.  


### Browse saved prev...
In this app you can browse and edit all existing tile maps.
WASD: Move around on screen.
1 and 2: Zoom.
Mouse: Select region(s).
Arrow keys: When selected regions, move them with arrow keys.
To enter editing mode, press "EDIT". When pressing "SAVE", current file gets overwritten with changes.


### Create Tile Map from GeoJSON file...
In this app you can choose a file to create a tile map from.
When starting app, you will through tkinter be asked to choose a file directory.
Creation can take up to a few minutes, depending on number of regions and map iterations.


# To create from file online:
run CreateFromURL.py
Enter URL and desired file name.


# Saved maps
In the folder venv\maps\final_maps are all the already created maps.
Under ..\final_maps\_countrymaps are maps of the world, of continents, the European Union...
Other than that, folders exist for almost every county. Most have admin_1 maps (of the larger regions in the country),
some also have admin_2 maps of smaller municipalities / correspondent.
