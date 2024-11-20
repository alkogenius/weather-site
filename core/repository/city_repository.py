from core.models import City
from core.repository import DjangoORMRepository


class CityRepository(DjangoORMRepository):
    """Репозиторий модели городов"""

    def __init__(self) -> None:
        super().__init__(City)

    def filter_city_by_name(self, name) -> City:
        return self.model.objects.filter(city_name__iexact=name).first()
