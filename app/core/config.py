import os

from dotenv import load_dotenv

load_dotenv()

OPEN_WEATHER_MAP_API_KEY = os.getenv("OPEN_WEATHER_MAP_API_KEY")
GEOCODING_API_KEY = os.getenv("GEOCODING_API_KEY")
