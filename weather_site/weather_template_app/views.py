import logging
from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from core import exceptions, service

logger = logging.getLogger(__name__)


class WeatherInfoView(View):
    """Представление информации о погоде"""

    template_name = "index.html"
    weather_service = service.WeatherService()

    def get_context(self, city_name: str = None) -> dict[str, Any]:
        """Метод собирает контекст для шаблона"""
        context = {}
        if not city_name or city_name == "":
            context["error"] = "Введите название города"
        try:
            weather = self.weather_service.get_city_weather(
                city_name=city_name
            )
            if weather:
                weather["city"] = city_name
                context["weather"] = weather
            else:
                context["error"] = "Город по вашему " "запросу не найден"
        except exceptions.WeatherError as e:
            logger.exception(
                f"При попытке получить"
                f" информацию о погоде"
                f" произошла ошибка. \n"
                f"Ошибка - {e}"
            )
            context["error"] = (
                "Не удалось получить данные о погоде. Попробуйте позже."
            )
        return context

    def get(self, request: HttpRequest) -> HttpResponse:
        """Метод для обработки GET-запросов."""
        return render(
            request, self.template_name, {"error": "Введите название города."}
        )

    @csrf_exempt
    def post(self, request: HttpRequest) -> HttpResponse:
        """Метод для обработки POST-запросов."""
        city = request.POST.get("city", "").strip()
        context = self.get_context(city_name=city)
        return render(request, self.template_name, context)
