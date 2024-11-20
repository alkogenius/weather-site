import logging
import os
from typing import Any

from core.utils import ApiClient

logger = logging.getLogger(__name__)


class YandexApiService:
    """Класс для взаимодействия с API Яндекс. Погода"""

    def __init__(self) -> None:
        self.api_client = ApiClient(
            base_url=os.getenv("YANDEX_API_URL"),
        )
        self.__token = os.getenv("YANDEX_API_TOKEN")
        self.headers = {"X-Yandex-Weather-Key": self.__token}

    def get_weather_info(
        self, latitude: str, longitude: str
    ) -> dict[str, Any]:
        """Метод получает погоду по координатам"""
        params = {
            "lat": latitude,
            "lon": longitude,
            "lang": "ru_RU",
            "hours": False,
            "extra": False,
        }
        response = self.api_client.get(
            "/v2/forecast", params=params, headers=self.headers
        )
        info = response.get("info")
        fact = response.get("fact")
        return {
            "url": info.get("url"),
            "def_pressure_mm": info.get("def_pressure_mm"),
            "temp": fact.get("temp"),
            "wind_speed": fact.get("wind_speed"),
        }
