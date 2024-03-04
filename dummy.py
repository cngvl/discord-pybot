import csv
from petrol_scrape import petrol_scrape, get_lat_long

coords = get_lat_long('$petty 3025')
print(coords)
