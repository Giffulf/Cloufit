from fastapi import APIRouter, HTTPException

from ...service.weather import WeatherService

from ...core.config import logger

weather_router = APIRouter()

weather_service = WeatherService()


@weather_router.get("/weather/{city}")
async def get_weather(city: str):
    try:
        return weather_service.get_weather_by_city(city)
    except Exception as e:
        logger.error(e)
        return HTTPException(status_code=500, detail="Something went wrong")
