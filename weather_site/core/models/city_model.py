from django.db import models


class City(models.Model):
    """Модель городов"""

    city_name = models.CharField(
        max_length=255, verbose_name="Название города"
    )
    latitude = models.FloatField(verbose_name="Географическая широта")
    longitude = models.FloatField(verbose_name="Географическая долгота")

    def __str__(self) -> str:
        return (
            f"Город {self.city_name} "
            f"с координатами "
            f"- {self.latitude}, "
            f"{self.longitude}"
        )

    class Meta:
        ordering = ["city_name"]
        db_table = "cities"
        verbose_name = "Город"
        verbose_name_plural = "Города"
