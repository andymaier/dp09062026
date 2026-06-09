# coding: utf-8

from fastapi.testclient import TestClient


from typing import List  # noqa: F401
from openapi_server.models.article import Article  # noqa: F401


def test_articles_get(client: TestClient):
    """Test case for articles_get

    Gebe alle Artikel zurück
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/articles",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

