from location import Location
from weather import Weather

class Venue:

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.loc = Location(name, location)
    
    def weather_dataframe(self, start_date, end_date):
        lat, long = self.loc.lat_long()
        return Weather(lat, long).weather_df(start_date, end_date)

    def daily_weather(self, day):
        lat, long = self.loc.lat_long()
        return Weather(lat, long).daily_weather(day)

venue = Venue('Jupiter Disco', 'Brooklyn, NY')

print(venue.loc.yelp_review_count())