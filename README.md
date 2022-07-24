# GFS-ECMWF
## The easier way to download operational data from GFS and ECMWF.  


The operational data of models Global Forecast System (GFS) and European Centre for Medium-Range Weather Forecasts (ECMWF) is avaiable in sites, however, it is difficult to download all files at once.
For this, two scripts were created in Python, each one indicated for a particular model in question. Each file has its indications:

**1. Resolution (specific to the GFS model that contains resolutions of 025, 050, 1)**

**2. Inittial Hour** 

**3. Final Hour**

**4. Interval** 

In addition, the script for downloading the GFS model data has the possibility of clipping to a certain region of the globe from latitude and longitude:

### LAT LON ENTIRE COUNTRY ### 
min_lon = '-93.00'
max_lon = '-25.00'
min_lat = '-60.00'
max_lat = '18.00'

### LAT LON SOUTH REGION OF BRAZIL ### 
min_lon = '-90.00'
max_lon = '-83.00'
min_lat = '12.00'
max_lat = '17.00'
