# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from typing import List
from openapi_server.models.article import Article


class BaseShopApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseShopApi.subclasses = BaseShopApi.subclasses + (cls,)
    async def articles_get(
        self,
    ) -> List[Article]:
        """Alle Artikel werden zurückgegeben"""
        ...
