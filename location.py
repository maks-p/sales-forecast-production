import requests
import json
import re

from config import yelp_api_key, google_api_key

class Location:

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def make_api_call(self):
        host = 'https://api.yelp.com'
        path = '/v3/businesses/search'
        
        # Yelp Authorization Header with API Key
        headers = {
            'Authorization': 'Bearer {}'.format(yelp_api_key) 
        }

        url_params = {
            'term': self.name.replace(' ', '+'),
            'location': self.location.replace(' ', '+'),
            'limit': 10
            }

        url_params = url_params or {}
        url = '{}{}'.format(host, path)
        response = requests.get(url, headers=headers, params=url_params).json()

        return response

    def validate_business(self):
        response = self.make_api_call()
        
        # Set state to False in case no Yelp match found
        state = False
        possible_matches = []

        try:
            # Check search returns for match with business
            for i in range(len(response['businesses'])):

                # If match found:
                if response['businesses'][i]['name'] == self.name:
                    return response['businesses'][0]
                    state = True
        except:
            print('Venue not found, please enter a valid venue')

    def lat_long(self):
        r = self.validate_business()

        #return (response['businesses'][0])
        lat, long = r['coordinates']['latitude'], r['coordinates']['longitude']

        return lat, long

    def yelp_rating(self):
        r = self.validate_business()
        return r['rating']

    def yelp_review_count(self):
        r = self.validate_business()
        return r['review_count']

    def google_places_id(self):

        base_url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'

        pattern = re.compile(r'\s+')
        location_text = re.sub(pattern, '', self.location).replace(',', '%20')

        url = (base_url + 'input=' 
                    + self.name.replace(' ', '%20') + '%20'
                    + location_text + '%20' 
                    + '&inputtype=textquery&key=' + google_api_key)

        r = requests.get(url)
        response = r.json()
        
        return response['candidates'][0]['place_id']

    def google_rating(self):

        place_id = self.google_places_id()

        base_url = 'https://maps.googleapis.com/maps/api/place/details/json?'

        url = (base_url + 'place_id=' + place_id + '&fields=rating' + '&key=' + google_api_key)

        r = requests.get(url)
        response = r.json()

        return response['result']

    def google_reviews(self):

        place_id = self.google_places_id()

        base_url = 'https://maps.googleapis.com/maps/api/place/details/json?'

        url = (base_url + 'place_id=' + place_id + '&fields=review' + '&key=' + google_api_key)

        r = requests.get(url)
        response = r.json()

        return response['result']

    def google_lat_long(self):

        place_id = self.google_places_id()

        base_url = 'https://maps.googleapis.com/maps/api/place/details/json?'

        url = (base_url + 'place_id=' + place_id + '&fields=geometry' + '&key=' + google_api_key)

        r = requests.get(url)
        response = r.json()

        return response['result']['geometry']['location']



