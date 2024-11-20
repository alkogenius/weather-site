from typing import List, Optional, Type

from django.db import models

from core.repository.base_repository import AbstractRepository


class DjangoORMRepository(AbstractRepository):
    def __init__(self, model: Type[models.Model]):
        self.model = model

    def get_by_id(self, pk: int) -> Optional[models.Model]:
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return None

    def get_all(self) -> List[models.Model]:
        return list(self.model.objects.all())

    def create(self, **kwargs) -> models.Model:
        return self.model.objects.create(**kwargs)

    def update(self, pk: int, **kwargs) -> Optional[models.Model]:
        obj = self.get_by_id(pk)
        if obj:
            for key, value in kwargs.items():
                setattr(obj, key, value)
            obj.save()
            return obj
        return None

    def delete(self, pk: int) -> bool:
        obj = self.get_by_id(pk)
        if obj:
            obj.delete()
            return True
        return False
