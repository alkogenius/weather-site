class TokenIsNotValid(Exception):
    """Исключение при невалидном токене"""

    pass


class ExternalApiError(Exception):
    """Исключение при работе со сторонними ресурсами"""

    pass


class WeatherError(Exception):
    """Исключение при получении погоды"""

    pass
