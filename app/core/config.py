import logging
import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    @property
    def OPENWEATHER_API_KEY(self) -> str:
        return os.getenv('OPEN_WEATHER_API_KEY')

    @property
    def GEOCODING_API_KEY(self) -> str:
        return os.getenv("GEOCODING_API_KEY")

    @property
    def OPENWEATHER__ARG__CNT(self) -> int:
        return int(os.getenv('OPENWEATHER__ARG__CNT'))

    @property
    def OPEN_WEATHER__ARG__LANG(self) -> str:
        return os.getenv('OPENWEATHER__ARG__LANG')

    @property
    def OPEN_WEATHER__URL__DOMAIN(self) -> str:
        return os.getenv('OPEN_WEATHER__URL__DOMAIN')

    @property
    def OPEN_WEATHER__URL__ENDPOINT(self) -> str:
        return os.getenv('OPEN_WEATHER__URL__ENDPOINT')

    @property
    def OPEN_WEATHER_VERSION(self) -> str:
        return os.getenv('OPEN_WEATHER_VERSION')

    @property
    def GEOCODING__URL__DOMAIN(self) -> str:
        return os.getenv('GEOCODING__URL__DOMAIN')

    @property
    def GEOCODING__URL__ENDPOINT(self) -> str:
        return os.getenv('GEOCODING__URL__ENDPOINT')

    @property
    def GEOCODING__ARG__COUNTRY(self) -> str:
        return os.getenv('GEOCODING__ARG__COUNTRY')

    @property
    def GEOCODING__VERSION(self) -> str:
        return os.getenv('GEOCODING__VERSION')


config = Config()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter("%(levelname)s: %(asctime)s  - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Config loaded")
