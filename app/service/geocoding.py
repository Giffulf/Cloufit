import requests

from ..core.config import GEOCODING_API_KEY


class Geocoder:
    def __init__(self):
        self.api_key = GEOCODING_API_KEY

        self.api_url = "https://api.api-ninjas.com/v1/geocoding?country=RU&city="

        self.headers = {
            'X-Api-Key': self.api_key
        }

    def geocode(self, city: str) -> dict:
        res = requests.get(self.api_url + city, headers=self.headers)
        if len(res.json()):
            return res.json()
        return {}
