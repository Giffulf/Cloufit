import requests

from .geocoding import Geocoder
from ..core.config import OPEN_WEATHER_MAP_API_KEY


class WeatherService:
    def __init__(self):
        self.api_key = OPEN_WEATHER_MAP_API_KEY
        self.weather_map_url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&lang=ru"

        self.geocoder = Geocoder()

    def get_weather_by_city(self, city_name: str) -> dict:
        geo_lat_lon = self.geocoder.geocode(city_name)
        if not geo_lat_lon:
            return {"error": "Город не найден"}

        res = requests.get(self.weather_map_url.format(lat=geo_lat_lon[0]['latitude'], lon=geo_lat_lon[0]['longitude'], api_key=self.api_key))

        if res.status_code == 200:
            return res.json()
        return {"error": "Ошибка погодного сервера"}
