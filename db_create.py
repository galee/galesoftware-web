import json
import datetime
import random
from sets import Set
datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

d = {
    'vrm': 'x828hby',
    'date': datetime.datetime.utcnow().strftime("%Y%m%dZ"),
    'titles': ['BDFL', 'Developer'],
}
tit = []
tit.append('blah1')
tit.append('blah2')
d['titles'].extend(tit)
# d['titles'] = tit

print(json.dumps(d))

dt = datetime.datetime.utcnow()
gpxList = []
for x in range(0, 20000):
    gpxDT = dt + datetime.timedelta(seconds=x)
    gpxDT = gpxDT.strftime("%Y%m%dT%H%M%SZ")
    gpx = {}
    gpx['lat'] = "51.5878140"
    gpx['lon'] = "-3.9998060"
    gpx['t'] = gpxDT
    gpxList.append(gpx)

d['gpx'] = gpxList
print(json.dumps(d))



ignore_list = ['Q', 'I', 'J', 'Q', 'T', 'U', 'X']
ignore_list_area = ['I', 'J', 'Q']
vrm_prefix=[]
for j in range(ord('A'),ord('Y')):
    vrm_prefix.append(chr(j))

vrm_area = [x for x in vrm_prefix if x not in ignore_list]
vrm_sub_area = [x for x in vrm_prefix if x not in ignore_list_area]
yr = ['02','03','04','05','06','07','08','09','10','11','12','13','14','15']
yr.extend([x for x in range(51,65)])
vrm_list = []
vrm_set = Set([])
for i in range(0, 10000000):
    # print "%s%s%s %s%s%s" % (random.choice(vrm_area),
    #                     random.choice(vrm_sub_area),
    #                     random.choice(yr), random.choice(vrm_sub_area),
    #                     random.choice(vrm_sub_area), random.choice(vrm_sub_area))
    vrm_list.append((random.choice(vrm_area),random.choice(vrm_sub_area),random.choice(yr),random.choice(vrm_sub_area),random.choice(vrm_sub_area),random.choice(vrm_sub_area)))

for j in range(0, len(vrm_list) - 1):
    vrm_set.add(vrm_list[j])

print 'set length is %d' % len(vrm_set)
print ' '.join(vrm_area)
