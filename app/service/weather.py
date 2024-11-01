import requests

from .geocoding import Geocoder
from ..core.config import config, logger


class WeatherService:
    def __init__(self):
        self.api_key = config.OPENWEATHER_API_KEY
        self.weather_map_url = f"https://{config.OPEN_WEATHER__URL__DOMAIN}/data/{config.OPEN_WEATHER_VERSION}/{config.OPEN_WEATHER__URL__ENDPOINT}?" + "lat={lat}&lon={lon}&appid={api_key}&lang=ru&cnt=6"

        self.geocoder = Geocoder()

    def get_weather_by_city(self, city_name: str) -> dict:
        logger.info(f"Getting weather for {city_name}")

        geo_lat_lon = self.geocoder.geocode(city_name)
        if not geo_lat_lon:
            return {"error": "Город не найден"}

        res = requests.get(self.weather_map_url.format(lat=geo_lat_lon[0]['latitude'], lon=geo_lat_lon[0]['longitude'], api_key=self.api_key))

        if res.status_code == 200:
            logger.info(f"Successfully fetched weather for {city_name}")

            return res.json()

        logger.warning(f"Failed to fetch weather for {city_name}")

        return {"error": "Ошибка погодного сервера"}
