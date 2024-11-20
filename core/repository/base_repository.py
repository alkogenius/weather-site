from abc import ABC, abstractmethod
from typing import Any, List

from cfgv import Optional
from django.db import models


class AbstractRepository(ABC):
    """Абстрактный класс репозитория"""

    @abstractmethod
    def get_by_id(self, pk: int) -> Optional[models.Model]:
        """Получение объекта по ID"""
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[models.Model]:
        """Получение всех объектов"""
        raise NotImplementedError

    @abstractmethod
    def create(self, **kwargs: dict[str, Any]) -> models.Model:
        """Создание объекта"""
        raise NotImplementedError

    @abstractmethod
    def update(
        self, pk: int, **kwargs: dict[str, Any]
    ) -> Optional[models.Model]:
        """Обновление объекта по ID"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, pk: int) -> bool:
        """Удаление объекта по ID"""
        raise NotImplementedError
