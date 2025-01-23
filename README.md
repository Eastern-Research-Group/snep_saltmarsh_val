# snep_saltmarsh

In support of the Environmental Protection Agency (EPA), the Great Lakes Environmental Center’s (GLEC) subcontractor, Eastern Research Group, Inc. (ERG), used the Sea Level Affecting Marshes Model (SLAMM) to examine how three salt marshes in Southeast New England protect surrounding communities from projected sea level rise and storm surge. 

This repository houses the code used for SLAMM modeling and for the evaluation analysis.

### Notebooks
1. Process data for SLAMM modeling
    - `process_dem.ipynb`
    - `process_dams.ipynb`
    - `process_nwi.ipynb`
    - `process_slosh.ipynb`
    - `process_impervious_surface.ipynb`
    - `salt_elevation.ipynb`
    - `sea_level_rise.ipynb`
2. Polygonize SLAMM output so it's ready for analysis
    - `polygonize_slamm_output.ipynb`
3. Inundation analysis
    - `intersect_pop.ipynb`
    - `intersect_properties.ipynb`
    - `intersect_roads.ipynb`
    - `fants_roads.ipynb`
4. Create maps of results
    - `create_veg_maps.ipynb`
    - `create_flood_maps.ipynb`
    - `create_cranberry_maps.ipynb`

### Excel workbooks
Workbook used to calculate traffic delay costs for road inundation:
- `roads_affected.xlsx`

Workbooks to calculate estimated damages and severity of inundation to land and residences:
- `cc1_homes_affect_fract_econ.xlsx`
- `ma2_homes_affect_fract_econ.xlsx`
- `ri2_homes_flooded_all_econ.xlsx`

### Data Sources for SLAMM modeling
| Model input | Marsh |  Data Name | Data Source | 
| ------------- | ------------- | ------------- | ------------- | 
| Digital elevation model | MA-2 and CC-1 | Bare earth Lidar DEM | [MassGIS](https://www.mass.gov/info-details/massgis-data-lidar-dem-and-shaded-relief) |
| Digital elevation model | RI-2 | Topobathymetric Elevation Model of New England | [U. S. Geological Survey](https://www.usgs.gov/special-topics/coastal-national-elevation-database-applications-project/science/hurricane-sandy-0) |
| Wetlands Classification | All marshes | National Wetlands Inventory | [U.S. Fish and Wildlife](https://www.fws.gov/program/national-wetlands-inventory/data-download) |
| Impervious Surfaces | RI-2| RI Impervious Surface | [RIGIS](https://www.rigis.org/maps/ce2cb6f8f7b045fe800cdd4e281dfb64/explore) |
| Impervious Surfaces | MA-2 and CC-1 | MA Impervious Surface | [Massachusetts Executive Office of Energy and Environmental Affairs](https://hub.arcgis.com/maps/1b2efe6d7b144fcf82376692d3de304b/explore) |
| Storm Surge  | All marshes | The Sea Lake and Overland Surges from Hurricanes (SLOSH) model | [NOAA](https://www.nhc.noaa.gov/nationalsurge/) |

### Data Sources for Inundation Analysis

| Data analyzed | Data Name | Data Source | 
| -------------| ------------- | ------------- | 
| Population | MA 2020 Census Data | [MassGIS](https://www.mass.gov/info-details/massgis-data-2020-us-census) | 
| Population | U.S. Census Data | [ESRI Federal Data](https://hub.arcgis.com/datasets/d795eaa6ee7a40bdb2efeb2d001bf823_0/about)| 
| Roads | MA 2020 U.S. Census Tiger Roads | [MassGIS](https://www.mass.gov/info-details/massgis-data-2020-us-census-tiger-roads) | 
| Roads | RIDOT Roads (2016) | [RIGIS](https://www.rigis.org/datasets/edc::ridot-roads-2016/about) |
| Properties | Property Tax Parcels | [MassGIS](https://www.mass.gov/info-details/massgis-data-property-tax-parcels) | 
| Properties | Town of Barrington Property Tax Parcels | [Town on Barrington](https://next.axisgis.com/BarringtonRI/) | 