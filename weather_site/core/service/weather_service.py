import logging
from typing import Any, Optional

from django.core.cache import cache

from core.exceptions import ExternalApiError, TokenIsNotValid, WeatherError
from core.repository import CityRepository
from core.service.yandex_api_service import YandexApiService

logger = logging.getLogger(__name__)


class WeatherService:
    """Сервис для работы с погодой"""

    def __init__(self) -> None:
        self._yandex_api_s = YandexApiService()
        self._city_repository = CityRepository()

    def get_city_weather(self, city_name: str) -> Optional[dict[str, Any]]:
        """Метод получает погоду города"""
        logger.debug(
            f"Попытка "
            f"получить данные "
            f"о погоде "
            f"в городе {city_name}"
        )
        cached_weather = cache.get(city_name)
        if cached_weather:
            logger.debug("Информация о погоде найдена в кэш-хранилище")
            return cached_weather
        city = self._city_repository.filter_city_by_name(city_name)
        if not city:
            logger.debug(f"Город {city_name} не был найден")
            return None
        try:
            weather = self._yandex_api_s.get_weather_info(
                latitude=city.latitude, longitude=city.longitude
            )
            logger.debug("Погода получена от яндекса и записана в кеш")
            cache.set(city_name, weather, timeout=1800)
            return weather
        except (ExternalApiError, TokenIsNotValid) as e:
            raise WeatherError from e
