from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    """Сериализатор информации о погоде"""

    city = serializers.CharField(
        max_length=100, help_text="Название " "города."
    )
    url = serializers.URLField(
        help_text="URL, содержащий " "более подробную " "информацию о погоде."
    )
    def_pressure_mm = serializers.IntegerField(
        help_text="Атмосферное " "давление в мм рт. ст.", min_value=0
    )
    temp = serializers.IntegerField(
        help_text="Температура воздуха" " в градусах Цельсия."
    )
    wind_speed = serializers.FloatField(
        help_text="Скорость ветра в м/с.", min_value=0.0
    )
