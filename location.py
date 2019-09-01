import requests
import json

from config import yelp_api_key

def make_api_call(name, location):
    host = 'https://api.yelp.com'
    path = '/v3/businesses/search'
    
    # Yelp Authorization Header with API Key
    headers = {
        'Authorization': 'Bearer {}'.format(yelp_api_key) 
    }

    url_params = {
        'term': name.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': 10
        }

    url_params = url_params or {}
    url = '{}{}'.format(host, path)
    response = requests.get(url, headers=headers, params=url_params).json()

    return response

def validate_business(name, location):
    response = make_api_call(name, location)
    
    # Set state to False in case no Yelp match found
    state = False
    possible_matches = []

    try:
        # Check search returns for match with business
        for i in range(len(response['businesses'])):

            # If match found:
            if response['businesses'][i]['name'] == name:
                return response
                state = True
    except:
        pass

    # If no match, show user potential matches
    if not state:
        if len(possible_matches) > 0:
            print('Exact match not found, please input one of the following venues: \n')
            for possible_match in possible_matches:
                print(possible_match)
        else:
            print('No matches found, please enter a proper venue name.')
    else:
        # If no exact match, append all search returns to list
        possible_matches.append(response['businesses'][i]['name'])

def get_lat_long(name, location):
    response = validate_business(name, location)

    # Local variables to help navigate JSON return
    response_ = response['businesses'][0]
    name_ = response_['name']
    print(f'Weather Location: {name_}')

    #return (response['businesses'][0])
    lat, long = response_['coordinates']['latitude'], response_['coordinates']['longitude']

    return lat, long




