#pip install googlemaps
#pip install prettyprint

import googlemaps
import prettyprint
import time

API_KEY = 'AIzaSyCMXY-PMl-ricsgom1FlGIU5EWG-diN6HM'

gmaps = googlemaps.Client(key = API_KEY)

cds = '49.884928,-119.487200'

def find_places(coords):

    places_result = gmaps.places_nearby(location = coords, radius = '40000',open_now = False,type = 'electronics_store')

    time.sleep(3)

    count = 0
    my_result = ''
    for place in places_result['results']:
        if count==5:
            break
        count = count + 1
        my_place_id = place['place_id']
        my_fields = ['name','vicinity']
        place_details = gmaps.place(place_id = my_place_id,fields = my_fields)
        name = str(place_details['result'].get('name'))
        address = str(place_details['result'].get('vicinity'))
        str1 = "\nStore name: {fname}, Address:{add}".format(fname = name,add = address)
        my_result = my_result + str1
    
    return my_result + "\n\nWould you like to discuss a product or a service?\n\n"
        
        




