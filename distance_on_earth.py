from geopy.distance import haversine_distance

# get the first pair of coordinates from the user
lat1 = float(input("Enter the latitude of the first point: "))
lon1 = float(input("Enter the longitude of the first point: "))

# get the second pair of coordinates from the user
lat2 = float(input("Enter the latitude of the second point: "))
lon2 = float(input("Enter the longitude of the second point: "))

# convert the coordinates to a format that can be used by the haversine_distance function
coord1 = (lat1, lon1)
coord2 = (lat2, lon2)

# calculate the distance in miles
distance_miles = haversine_distance(coord1, coord2).miles

# calculate the distance in kilometers
distance_km = haversine_distance(coord1, coord2).km

# print the results
print("Distance in miles: ", distance_miles)
print("Distance in kilometers: ", distance_km)
