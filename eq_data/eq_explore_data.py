from pathlib import Path
import json 

# Read data as a string and convert to a python project
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents) # Convert it to string represtation as a python object


# Create a more readable version of the data file
# path = Path('eq_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)


# Examine all earthquakes in the dataset
all_eq_dicts = all_eq_data['features']

mags = []
for eq_dict in all_eq_dicts:  # Make an empty list then loop through the list
    mag = eq_dict['properties']['mag'] # Store magnitude in the variable mag and append list 
    mags.append(mag)
print(mags[:10])