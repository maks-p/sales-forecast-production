from location import Location
from weather import Weather

class Venue:

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.lat, self.long = Location(name, location).lat_long()
    
    def weather_dataframe(self, start_date, end_date):
        return Weather(self.lat, self.long).weather_df(start_date, end_date)

    def daily_weather(self, day):
        return Weather(self.lat, self.long).daily_weather(day)

    def yelp_rating(self):
        return Location(self.name, self.location).yelp_rating()

venue = Venue('Jupiter Disco', 'Brooklyn, NY')
print(venue.Location)