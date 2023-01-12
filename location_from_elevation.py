import requests

def get_coordinates(elevation):
    api_key = 'YOUR_API_KEY'
    search_url = 'https://api.open-elevation.com/api/v1/lookup'

    params = {
        'elevation': elevation
    }

    headers = {
        'Authorization': 'Token ' + api_key
    }

    response = requests.get(search_url, params=params, headers=headers)
    data = response.json()

    if 'results' in data:
        return data['results'][0]['latitude'], data['results'][0]['longitude']
    else:
        return None

elevation = input("Enter the desired elevation in meters: ")
coordinates = get_coordinates(elevation)

if coordinates:
    print("Coordinates found:", coordinates)
else:
    print("No coordinates found.")
