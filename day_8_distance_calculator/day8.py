import requests
from math import sqrt, cos, pi


class DistanceCalculator:
    def __init__(self, address):
        self.address = address

    @staticmethod
    def get_current_location():
        url = 'http://ipinfo.io/json'
        request = requests.get(url)
        if request.status_code != 200:
            return f'Could not connect with ip api'

        data = request.json()
        lat, lng = data['loc'].split(',')

        return float(lat), float(lng)

    def get_coordinates(self):
        headers = {
            'x-rapidapi-key': '0f062f447cmsha3201cd01ee5606p1bb261jsn1f348c5fe246',
            'x-rapidapi-host': 'trueway-geocoding.p.rapidapi.com'
        }
        url = "https://trueway-geocoding.p.rapidapi.com/Geocode"
        querystring = {"address": self.address, "lang": 'en'}

        request = requests.get(url, headers=headers, params=querystring)
        if request.status_code != 200:
            return f'Could not connect'

        data = request.json()
        location = data['results'][0]['location']

        return float(location['lat']),  float(location['lng'])

    def count_distance(self):
        dest_lat, dest_lng = self.get_coordinates()
        user_lat, user_lng = self.get_current_location()
        return sqrt((user_lat-dest_lat)**2 + (cos(dest_lat*pi/180)*(user_lng-dest_lng))**2)*40075.704/260

    @property
    def distance(self):
        return self.count_distance()


def main():
    address = input("Please provide address: \n")
    location = DistanceCalculator(address)
    print(f' Your distance to {address} equals {round(location.distance, 2)} km')


if __name__ == '__main__':
    main()