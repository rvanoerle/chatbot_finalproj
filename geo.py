import requests

API_KEY = "AIzaSyCvU0JErsRxyWhxcxY8RqYRtpMM9U4enCE"


def find_add(address):
    params = {
        'key': API_KEY,
        'address': address
    }
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url,params=params).json()
    response.keys()

    if response['status'] == 'OK':
        geo = response['results'][0]['geometry']
        lat = geo['location']['lat']
        long = geo['location']['lng']
        loc = '{lat},{long}'
        return loc.format(lat=lat,long=long)

