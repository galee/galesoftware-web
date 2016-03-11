cat ukpostcodes.csv |  awk '{print $1}' | sed 's/.*,//' | sort -k1 | uniq | wc -l
=2978 unique post code areas.



cat ukpostcodes.csv |  awk '{print $1}' | sed 's/.*,//' | sort -k1 | uniq > ukpostcodeareas.txt
cat ukpostcodes.csv | cut -d"," -f 2 > ukpostcodes.txt

cat population_per_postcode.csv  | awk 'FS="," {print $2, $1}' | sort -n -k1 | more

# to start osrm
cd /Users/ed/Documents/routing/osrm-backend/build
./osrm-routed great-britain-latest.osrm
str = "http://localhost:5000/viaroute?loc=%s,%s&loc=%s,%s" % (orig_lat, orig_lon, dest_lat, dest_lon)
str = "http://localhost:5000/nearest?loc=%s,%s" % (orig_lat, orig_lon)
str = "http://localhost:5000/nearest?loc=%s,%s" % (dest_lat, dest_lon)


import requests
import random
import json
from geopy.distance import great_circle

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input


population = [line.rstrip() for line in open('population_per_postcode.csv')]
population_cumulatives = [[int(i.split(",")[1]), i.split(",")[0]] for i in population]
population_total = sum([int(i.split(",")[1]) for i in population])
count = total = 0

pop_list = []
for x in population_cumulatives:
    for y in range(x[0]):
        pop_list.append(x[1])

sample_population = random.sample(pop_list, 1000000)
sample_population.sort()
postcodes = [line.rstrip() for line in open('ukpostcodes.csv')]

prev_samp = ""
for samp in sample_population:
    if samp != prev_samp:
        s = [p for p in postcodes if p.split(",")[1].startswith(samp)]
        print samp

    prev_samp = samp


postcodes = [line.rstrip() for line in open('ukpostcodes.csv')]
s = [p for p in postcodes if p.split(",")[1].startswith("SA3 4AH")]
s1 = [p for p in postcodes if p.split(",")[1].startswith("EX39 4JF")]

sample_postcodes = random.sample(postcodes, 1)
sample_postcodes1 = random.sample(postcodes, 1)
for orig in s:
  orig_list = orig.split(",")
  orig_pcode = orig_list[1]
  orig_lat = orig_list[2]
  orig_lon = orig_list[3]
  for dest in s1:
    dest_list = dest.split(",")
    dest_pcode = dest_list[1]
    dest_lat = dest_list[2]
    dest_lon = dest_list[3]
    # str1 = "http://localhost:5000/viaroute?loc=51.57362382135124,-4.0020799636840&loc=51.51552216695712,-0.3215127885341"
    # graphhopper implementation
    str = "http://localhost:8989/route?point=%s%%2C%s&point=%s%%2C%s&locale=en-GB&vehicle=car&weighting=fastest&elevation=false&instructions=false&points_encoded=false" % (orig_lat, orig_lon, dest_lat, dest_lon)

    # str = "http://localhost:8989/route?point=%s%%2C%s&point=%s%%2C%s&locale=en-GB&vehicle=car&weighting=fastest&elevation=false&instructions=false" % (orig_lat, orig_lon, dest_lat, dest_lon)
    # osrm implementation
    # str = "http://localhost:5000/viaroute?loc=%s,%s&loc=%s,%s" % (orig_lat, orig_lon, dest_lat, dest_lon)
    print str
    print "%s to %s" % (orig_pcode, dest_pcode)
    print(great_circle((orig_lat, orig_lon), (dest_lat, dest_lon)).miles)
    x = requests.get(str)
        json.load(x)
    print x.text
    # print "%s %s %d" % (orig_pcode, dest_pcode, x.json()['route_summary']['total_distance'] / 1000 / 1.6)
