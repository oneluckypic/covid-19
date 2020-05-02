# covid-19 repository

To make a local copy of this repository run the following two commands:

```bash
git clone git@github.com:oneluckypic/covid-19.git

cd covid-19

On Windows:

update_data.bat

On Mac:

./update_data.sh

```

# Resources

## 3Blue1Brown

[Exponential growth and epidemics](https://www.youtube.com/watch?v=Kas0tIxDvrg)

[Simulating epidemics](https://www.youtube.com/watch?v=gxAaO2rsdIs)

## GIS
|Title|Author|Notes
|-----|------|-----
|[Map it with Python! Intro to GIS and Python mapping modules](https://www.youtube.com/watch?v=wsSEKm-rU6U)|Christy Heaton|[code](https://github.com/christyheaton/mapitwithpython), epsg.io, matplotlib, geopandas (uses shapely), folium w/ leaflet.js, rise (python slides), Nearmap, Stamen, mapbox, Map Time Seattle!
|[Geospatial data analysis and visualization in Python](https://www.youtube.com/watch?v=Yd5oEIBFQ_E)|Halfdan Rump|osmnx (by Geoff Boeing), geopandas, folium

#### Random Software
 * vega (for plotting)
 * color brewer (color advice for cartography)
 * [Chris Roach Github](https://github.com/croach)
 * Plotly!  (Can do interative maps)

Python Geospatial Libraries
 * geopandas - Working with spatial data is fun again!
 * shapely - For geometry handling
 * rtree - For efficiently querying spatial data
 * pyshp - for reading and writing shapefiles (in pure Python)
 * fiona - for making it easy to read/write geospatial data formats
 * ogr/gdal - for reading, writeing and transforming goespatial data formats
 * geopy - for geolocating and things like that
 * pysal - spatial ecenometrics, exploratory spatial and spatio-temporal data analysis, spatial clustering (and more)
 * descartes - for plotting geometries in matplotlib

# NYC Data
[Zip Code Population Data](https://data.cityofnewyork.us/City-Government/Demographic-Statistics-By-Zip-Code/kku6-nxdu )
[Zip Code Shapefiles](https://data.cityofnewyork.us/Business/Zip-Code-Boundaries/i8iw-xf4u)

# Learning Geospatial Analysis

* [Canadian Geospatial Information System Documentary](https://www.youtube.com/watch?v=3VLGvWEuZxI&feature=youtu.be)
* [1967 Urban Expansion](https://www.youtube.com/watch?v=xj8DQ7IQ8_o)
* GIS GUIs (open source)
  * Quantum GIS (QGIS)
  * Geographic Resources Analysis Support System (GRASS)
* Elevation Data
  * Digital Elevation Model (DEM)
  * First in 1986 from French space agency (Centre National d'etudes Spatiales (CNES))
  * February 2000 Space Shuttle Endeavor conducted the Shuttle Radar Topography Mission (SRTM), which collected elevation data of over 80% of the Earth's surface using a special radar antenna configuration that allowed a single pass.
  * 2009 the joint US and Japanese mission using the Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER) sensor aborad NASA's Terra satellite.  Captured 99% of the Earth's surface but has proven to have minor data issues.
  * SRTM remains the gold standard.
  * TerraSAR-X and TanDEM-X launched by Germany collected WorldDEM that was released on April 15, 2014.  Dataset has a relative accuracy of 2 meters and an absolute accuracy of 4 meters.
 * How to Lie with Maps, Mark Monmonier
 * ISO-19115(-1)(-2)(-3) define standards for geospatial metadata
 * The Open Geospatial Consortium (OGC), which created the Catalog Service for the Web (CSW), is used to manage metadata. The pycsw Python library implements the CSW standard.
 * A datum is a model of the Earth's surface that's used to match the location of features on the Earth to a coordinate system. One common datum is called WGS 84 and is used by GPS.
 * A dissolve operation creates a single polygon out of adjacent polygons.
 * ray casting algorithm - The most common and efficient algorithm to detect whether a point is inside a polygon.



