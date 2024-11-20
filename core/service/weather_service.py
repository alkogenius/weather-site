from typing import Any, Optional

from django.core.cache import cache

from core.exceptions import ExternalApiError, TokenIsNotValid, WeatherError
from core.repository import CityRepository
from core.service.yandex_api_service import YandexApiService


class WeatherService:
    """Сервис для работы с погодой"""

    def __init__(self) -> None:
        self._yandex_api_s = YandexApiService
        self._city_repository = CityRepository

    def get_city_weather(self, city_name: str) -> Optional[dict[str, Any]]:
        """Метод получает погоду города"""
        cached_weather = cache.get(city_name)
        if cached_weather:
            return cached_weather
        city = self._city_repository.filter_city_by_name(city_name)
        if city:
            return None
        try:
            weather = self._yandex_api_s.get_weather_info(
                latitude=city.latitude, longitude=city.longitude
            )
            cache.set(city_name, weather, timeout=1800)
            return weather
        except (ExternalApiError, TokenIsNotValid) as e:
            raise WeatherError from e
