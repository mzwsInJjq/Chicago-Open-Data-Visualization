# Chicago-Open-Data-Visualization

This repository contains a single Python script that visualizes Chicago open data. The script loads geographic data for the Chicago city boundary and street center lines, processes the data, and generates a map that shows both layers. The resulting map is saved as a PDF file.

## Data Sources

- **Chicago Building Footprints (current):**  
  https://data.cityofchicago.org/Buildings/Building-Footprints-current-/hz9b-7nh8

- **Chicago City Boundary:**  
  https://data.cityofchicago.org/Facilities-Geographic-Boundaries/City_Boundary/qqq8-j68g/about_data

- **Chicago Transportation (Street Center Lines):**  
  https://data.cityofchicago.org/Transportation/transportation/pr57-gg9e

## Requirements

- Python 3.7 or later
- pandas
- geopandas
- matplotlib

Install the required Python packages with:

    pip install pandas geopandas matplotlib

## Usage

The main script (`chicago.py`) performs the following operations:

1. Loads the Chicago city boundary from a GeoJSON file.
2. Loads the street center lines from a GeoJSON file.
3. Clips the street layer to only include data within the city boundary.
4. Plots the Chicago map with the city boundary and street center lines.
5. Saves the map to a PDF file (`chicago-scl.pdf`).

To run the script, execute:

    python chicago.py

## Notes

- Adjust the file paths in `chicago.py` as necessary to match the location of your downloaded data files.
- The building footprints data is currently commented out. Uncomment and adjust if needed.
