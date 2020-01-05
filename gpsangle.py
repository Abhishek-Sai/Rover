import math

#coordinates1
lat1 = 53.32055
lon1 = -1.72972
#coordinates2
lat2 =  53.31861
lon2 =  -1.69972
dlon = lon2-lon1
#use haversine formula
deltaY = math.sin(dlon) * math.cos(lat2)

deltaX = math.cos(lat1)*math.sin(lat2)-math.sin(lat1)*math.cos(lat2)*math.cos(dlon)

#convert to degrees
bearing = (math.atan2(deltaY, deltaX))* (180/math.pi)

#normalize to compass headings
bearing = (bearing + 180) % 360

print ('bearing: ', bearing)
print ('deltaY: ', deltaY)
print ('deltaX: ', deltaX)