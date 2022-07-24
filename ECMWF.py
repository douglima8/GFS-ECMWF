#-----------------------------------------------------------------------------------------------------------

# Required modules
from datetime import datetime        # Basic Dates and time types
import os                            # Miscellaneous operating system interfaces
import requests                      # HTTP library for Python
import time as t                     # Time access and conversion                                          
#-----------------------------------------------------------------------------------------------------------

print('---------------------------------------')
print('ECMWF Download (NOMADS) - Script started.')
print('---------------------------------------')

# Start the time counter
start_time = t.time()  

#-----------------------------------------------------------------------------------------------------------

# Download directory
dir = "DATA"; os.makedirs(dir, exist_ok=True)

# Desired date (last 10 days only!): Format - 'YYYYMMDD'
date = datetime.today().strftime('%Y%m%d')

# Desired run: '00' or '06' or '12' or '18'
hour_run = '00'


# Desired forecast hours
hour_ini = 0  # Init time  
hour_end = 120 # End time
hour_int = 3  # Interval
        
# Download loop
for hour in range(hour_ini, hour_end + 1, hour_int):
    print('\n---------------------')
    print('Downloading ECMWF File:')
    print('Date: ' + date)
    print('Run: ' + hour_run)
    print('Forecast Hour: f' + str(hour).zfill(3))
    
    #-----------------------------------------------------------------------------------------------------------

    # Link (select "grib filter" and check "Show the URL only for web programming" to verify the URL's):
    # https://nomads.ncep.noaa.gov/


    url = 'https://data.ecmwf.int/forecasts/'+date+'/'+hour_run+'z/0p4-beta/oper/'+date+''+hour_run+'0000-'+str(hour)+'h-oper-fc.grib2'
    file_name = ''+date+''+hour_run+'0000-'+str(hour)+'h-oper-fc.grib2'
        
        
    # Print the file name
    print("File name: ", file_name)
    # Sends a GET request to the specified url
    myfile = requests.get(url)

    # Download the file
    open(dir + '//' + file_name, 'wb').write(myfile.content)

#-----------------------------------------------------------------------------------------------------------

# End the time counter
print('\nTotal Processing Time:', round((t.time() - start_time),2), 'seconds.') 
    
    
    
    