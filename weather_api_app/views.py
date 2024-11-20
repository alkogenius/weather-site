import logging

from drf_spectacular.utils import (
    OpenApiParameter,
    extend_schema,
    extend_schema_view,
)
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from core import exceptions, service
from weather_api_app import serializers

logger = logging.getLogger(__name__)


@extend_schema(tags=["Weather Info"])
@extend_schema_view(
    get=extend_schema(
        summary="Предоставление информации о погоде",
        description="Эндпоинт получает в параметре "
        "строки название города и "
        "возвращает погоду в городе",
        parameters=[
            OpenApiParameter(
                name="city",
                location=OpenApiParameter.QUERY,
                description="Название города",
                required=True,
                type=str,
            )
        ],
    )
)
class WeatherInfoAPIView(generics.GenericAPIView):
    """Представление информации о погоде"""

    weather_service = service.WeatherService()
    serializer_class = serializers.WeatherSerializer

    def get(self, request: Request) -> Response:
        """Метод обработки GET-запроса"""
        city_name = request.query_params.get("city")
        try:
            weather = self.weather_service.get_city_weather(
                city_name=city_name
            )
            if weather:
                weather["city"] = city_name
                weather_response = self.get_serializer(weather)
                return Response(weather_response.data)
            return Response(status=404, data={"detail": "City was not found"})
        except exceptions.WeatherError as e:
            logger.exception(
                f"При попытке получить"
                f" информацию о погоде"
                f" произошла ошибка. \n"
                f"Ошибка - {e}"
            )
            return Response(
                status=500,
                data={"detail": "Some problems " "with getting weather"},
            )
