from typing import Any, Optional

from core.repository import CityRepository
from core.service.yandex_api_service import YandexApiService


class WeatherService:
    """Сервис для работы с погодой"""

    def __init__(self) -> None:
        self._yandex_api_s = YandexApiService
        self._city_repository = CityRepository

    def get_city_weather(self, city: str) -> Optional[dict[str, Any]]:
        """Метод получает погоду города"""
