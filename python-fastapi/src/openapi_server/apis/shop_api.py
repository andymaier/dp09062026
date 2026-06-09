# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.shop_api_base import BaseShopApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from typing import List
from openapi_server.models.article import Article


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/articles",
    responses={
        200: {"model": List[Article], "description": "OK"},
    },
    tags=["Shop"],
    summary="Gebe alle Artikel zurück",
    response_model_by_alias=True,
)
async def articles_get(
) -> List[Article]:
    """Alle Artikel werden zurückgegeben"""
    if not BaseShopApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseShopApi.subclasses[0]().articles_get()
