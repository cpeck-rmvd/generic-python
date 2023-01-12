import requests
from PIL import Image
from io import BytesIO

def search_image(query):
    api_key = 'YOUR_API_KEY'
    search_url = 'https://www.googleapis.com/customsearch/v1'

    params = {
        'q': query,
        'key': api_key,
        'cx': 'YOUR_CUSTOM_SEARCH_ENGINE_ID'
    }

    response = requests.get(search_url, params=params)
    data = response.json()

    if 'items' in data:
        return data['items'][0]['link']
    else:
        return None

query = input("Enter your image search query: ")
image_url = search_image(query)

if image_url:
    image_data = requests.get(image_url)
    image = Image.open(BytesIO(image_data.content))
    image.show()
else:
    print("No image found.")
