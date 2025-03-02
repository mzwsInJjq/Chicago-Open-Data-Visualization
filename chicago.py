# Chicago Building Footprints (current)
# https://data.cityofchicago.org/Buildings/Building-Footprints-current-/hz9b-7nh8

# Chicago City_Boundary
# https://data.cityofchicago.org/Facilities-Geographic-Boundaries/City_Boundary/qqq8-j68g/about_data

# Chicago Transportation
# https://data.cityofchicago.org/Transportation/transportation/pr57-gg9e

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

city_boundary = gpd.read_file(r"C:\Users\Chen\Downloads\City_Boundary_20250302.geojson")
street_center_lines = gpd.read_file(r"C:\Users\Chen\Downloads\transportation_20250302.geojson")
street_center_lines = gpd.overlay(street_center_lines, city_boundary, how='intersection')
# building_footprints = gpd.read_file(r"C:\Users\Chen\Downloads\buildings_20250302.csv")

fig, ax = plt.subplots(figsize=(20, 10))
ax.axis('off')
city_boundary.plot(ax=ax, color='b', label='City Boundary', alpha=0.5)
street_center_lines.plot(ax=ax, color='k', label='Street Center Lines', linewidth=0.3)
plt.savefig('chicago-scl.pdf', format='pdf', bbox_inches='tight')
# building_footprints.plot(ax=ax, color='k', label='Building Footprints', alpha=0.75)
# plt.savefig('chicago-scl-bf.pdf', format='pdf', bbox_inches='tight')