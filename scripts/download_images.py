#! /usr/bin/env python

import schedule
import time
import geopy
import numpy as np
from geopy.distance import VincentyDistance
import google_streetview.api

lat=[]
long=[]
centerLat = 40.732922
centerLong = -73.881198
bearing = 0
distances = []
count = 4000
mile_radius = 2.5

for i in np.arange(2.5,58.0,0.5):
        distances.append(i/0.62137119)

for i in distances:
        while(bearing <= 360):
                origin = geopy.Point(centerLat, centerLong)
                destination = VincentyDistance(kilometers=i).destination(origin, bearing)
                lat.append(destination.latitude)
                long.append(destination.longitude)
                bearing = bearing + 0.18
        
        coordinates = tuple(zip(lat,long))
        
        params = [{
                'size': '600x300', # max 640x640 pixels
                'location': '46.414382,10.013988',
                'heading': '151.78',
                'pitch': '-0.76',
                'key': ''
                }]
        
        for coord in coordinates:
                thelat = coord[0]
                thelong = coord[1]
                params[0]['location']=str(thelat)+','+str(thelong)
                results = google_streetview.api.results(params)
                
                # Download images to directory 'downloads'
                results.download_links('New_York/' +str(mile_radius)+'_mile_radius/'+str(count))
                count = count+1
        
        mile_radius = mile_radius+0.5
        count = count+2000
        
        #sleep till next day
        time.sleep(100000)
                



