from location import get_lat_long
from weather import Weather

start_date = '2019-08-01'
end_date = '2019-08-30'

class Venue:

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.lat, self.long = get_lat_long(name, location)
    
    def weather(self):
        return Weather(self.lat, self.long).weather_df(start_date, end_date)

jupiter = Venue('Jupiter Disco', 'Brooklyn, NY')
print(jupiter.name)
print(jupiter.location)
print(jupiter.lat, ',', jupiter.long)
print(jupiter.weather())