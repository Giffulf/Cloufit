from fastapi import APIRouter

from ...service.weather import WeatherService

weather_router = APIRouter()

weather_service = WeatherService()


@weather_router.get("/weather/{city}")
async def get_weather(city: str):
    return weather_service.get_weather_by_city(city)
