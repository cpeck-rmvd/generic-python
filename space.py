from astroquery.vizier import Vizier
import astropy.coordinates as coord
import astropy.units as u
import numpy as np
from skyfield import api

# Get distance between two arbitrary planets

def get_distance_between_planets(planet1, planet2):
    ts = api.load.timescale()
    p1 = getattr(api, planet1)()
    p2 = getattr(api, planet2)()
    t = ts.now()
    distance = p1.at(t).distance_to(p2)
    return distance.au

planet1 = input("Enter the first planet: ")
planet2 = input("Enter the second planet: ")

print(f"Current distance between {planet1} and {planet2} is: {get_distance_between_planets(planet1, planet2)} AU")

# Find how many stars are within X light years of earth

def get_closer_stars(distance):
    # Set the maximum distance
    max_distance = distance * u.lightyear
    # Search for stars within the maximum distance
    v = Vizier(columns=["*"], column_filters={"Plx": "<" + str(distance)})
    result = v.query_constraints(catalog="I/311/hip2", parallax=f"< {distance}")
    # Return the number of stars found
    return len(result[0])

distance = float(input("Enter the maximum distance in light years: "))
closer_stars = get_closer_stars(distance)

print(f"Number of stars closer than {distance} light years: {closer_stars}")

# Get max volume of any triangle acheived by connecting 3 arbitrary planets

def get_max_triangle_area(planet1, planet2, planet3):
    ts = api.load.timescale()
    p1 = getattr(api, planet1)().at(ts.now())
    p2 = getattr(api, planet2)().at(ts.now())
    p3 = getattr(api, planet3)().at(ts.now())
    r1 = np.array([p1.position.km])
    r2 = np.array([p2.position.km])
    r3 = np.array([p3.position.km])
    # Using Heron's formula to calculate the area of triangle
    a = np.linalg.norm(r2 - r3)
    b = np.linalg.norm(r1 - r3)
    c = np.linalg.norm(r1 - r2)
    s = (a + b + c) / 2.0
    area = np.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

planet1 = input("Enter the first planet: ")
planet2 = input("Enter the second planet: ")
planet3 = input("Enter the third planet: ")

print(f"Maximum possible area of triangle drawn between {planet1}, {planet2} and {planet3} is: {get_max_triangle_area(planet1, planet2, planet3)} square kilometers")
