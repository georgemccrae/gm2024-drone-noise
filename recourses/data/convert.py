
import geopandas as gpd

# Load the shapefile
gdf = gpd.read_file("/Users/georgemccrae/Desktop/shp/bethygsmall_CONTOURING_NOISE_MAP.shp")

# Save as GeoJSON
gdf.to_file("/Users/georgemccrae/Desktop/shp/bethygsmall_CONTOURING_NOISE_MAP.geojson", driver='GeoJSON')
