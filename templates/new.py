from math import *

lat1 = 12.894768413796779
long1 = 77.67579272389412

lat2 = 12.894628861194764
long2 = 77.6757887005806
# lat2 = 12.89495960400344
# long2 = 77.67527505755424




bearing = atan2(sin(long2-long1)*cos(lat2), cos(lat1)*sin(lat2)-sin(lat1)*cos(lat2)*cos(long2-long1))
bearing = degrees(bearing)
bearing = (bearing + 360) % 360
print(bearing)