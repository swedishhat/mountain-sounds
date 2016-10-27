""" 
TODO
* Format output points into API-friendly list/dict/tuple
* Run points through API and collect results
* Do literally everything else
"""

import googlemaps
import math
import json
import sys

# Phone home to Google and get the okay to use the API
gmaps = googlemaps.Client(key='')

# Geocode a start and stop address, replacing empty strings with convenient defaults
start_address = input('Enter start address: [LAX] ')
if not start_address:
    start_address = '1 World Way, Los Angeles, CA 90045'    # LAX

end_address = input('Enter end address: [PHL] ')
if not end_address:
    end_address = '8000 Essington Ave, Philadelphia, PA 19153'  # PHL

start_geocode = gmaps.geocode(start_address)
end_geocode   = gmaps.geocode(end_address)

#print(start_geocode)
#print(end_geocode)


# Parse geocoded result and extract the latitudes and longitudes
start_lat = start_geocode[0]['geometry']['location']['lat']
start_lng = start_geocode[0]['geometry']['location']['lng']
end_lat= end_geocode[0]['geometry']['location']['lat']
end_lng= end_geocode[0]['geometry']['location']['lng']

#print(start_lat)
#print(start_lng)
#print(end_lat)
#print(end_lng)


# Define the sound file parameters
sound_len_sec  = 2
sound_sample_rate = 8000
num_samples = sound_sample_rate * sound_len_sec

#print(sound_len_sec)
#print(sound_sample_rate)
print('Total number of samples to be collected: ' + str(num_samples))


# Maximum number of values that the API can return for a given path
api_max_results = 512

# Calculate the number of results that should contain 512 samples
full_chunks = int(math.floor(num_samples / api_max_results))

# If the number of samples isn't a multiple of 512, calculate how many samples should be in the last result
last_chunk_samples = num_samples - (full_chunks * api_max_results)

# Calculate the longitudinal and latitudinal step size from start to end
lat_step = (end_lat - start_lat) / (num_samples - 1)
lng_step = (end_lng - start_lng) / (num_samples - 1)

#print(full_chunks)
#print(last_chunk_samples)
#print(lat_step)
#print(lng_step)


# Determine for the full data chunks what their start and end latitudes and longitudes should be.
# It's determined by step size so you could run into rounding issues here I think if the step is too small
# range(1, full_chunks + 1) guarantees it iterates over a 1-indexed list, incremented by 1, up to and including the last chunk
paths = []
for chunk in range(1, full_chunks + 1):
    start_offset = (chunk - 1) * api_max_results 
    end_offset   = (chunk * api_max_results) - 1

    chunk_start_lat = (start_offset * lat_step) + start_lat
    chunk_start_lng = (start_offset * lng_step) + start_lng

    chunk_end_lat = (end_offset * lat_step) + start_lat
    chunk_end_lng= (end_offset * lng_step) + start_lng
    
    #{'lat': 32.0733865, 'lng': -81.1057464}
    paths.append ([{'lat': chunk_start_lat, 'lng': chunk_start_lng}, {'lat': chunk_end_lat, 'lng': chunk_end_lng}])

print('Collecting '+ str(api_max_results) + ' samples for each of the following coordinate pairs:')
elevations = []
for path in paths:
    print(path)
    elevations.append(gmaps.elevation_along_path(path, 512))

paths[-1][1]['lat'] + lat_step

print('Collecting '+ str(last_chunk_samples)+ ' samples for the final coordinate pair:')
print(paths[-1])

#sys.exit()
# Flatten the elevations list
flat_elevations_json = [item for sublist in elevations for item in sublist]
with open('elevations.json', 'w') as elev_file:
    json.dump(flat_elevations_json, elev_file, sort_keys=True, indent=4)
    elev_file.close()

# Parse the JSON to just get the float values of the elevations list
flat_elevations = flat_elevations_json[:]['elevation']
print(flat_elevations)