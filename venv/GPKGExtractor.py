from geopackage import GeoPackage

fp = r"maps/geopackage_maps/gadm36_AFG.gpkg"
with GeoPackage(fp) as gpkg:
    # List all Tables
    for table in gpkg.tables:
        print(table)

    for row in table:
        print(row)