import requests

from ..core.config import config, logger


class Geocoder:
    def __init__(self):
        self.api_key = config.GEOCODING_API_KEY

        self.api_url = f"https://{config.GEOCODING__URL__DOMAIN}/{config.GEOCODING__VERSION}/{config.GEOCODING__URL__ENDPOINT}?country={config.GEOCODING__ARG__COUNTRY}&city="

        self.headers = {
            'X-Api-Key': self.api_key
        }

    def geocode(self, city: str) -> dict:
        logger.info(f"Geocoding {city}")

        res = requests.get(self.api_url + city, headers=self.headers)
        if len(res.json()):
            logger.info(f"Successfully geocoded {city}")
            return res.json()

        logger.warning(f"Failed to geocode {city}")
        return {}
