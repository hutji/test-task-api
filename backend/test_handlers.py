import pytest
from aiohttp import web

from .handlers import hash_string, healthcheck


@pytest.mark.asyncio
async def test_healthcheck(aiohttp_client):
    app = web.Application()
    app.router.add_get("/healthcheck", healthcheck)
    client = await aiohttp_client(app)
    response = await client.get("/healthcheck")
    assert response.status == 200
    assert await response.json() == {}


@pytest.mark.asyncio
async def test_hash_string_is_valid(aiohttp_client):
    app = web.Application()
    app.router.add_post("/hash", hash_string)
    client = await aiohttp_client(app)
    data = {"string": "test_string"}
    response = await client.post("/hash", json=data)
    assert response.status == 200
    assert "hash_string" in await response.json()


@pytest.mark.asyncio
async def test_hash_string_invalid_json(aiohttp_client):
    app = web.Application()
    app.router.add_post("/hash", hash_string)
    client = await aiohttp_client(app)
    invalid_json = {"invalid_key": "invalid_value"}
    response = await client.post(
        "/hash", json=invalid_json, headers={"Content-Type": "application/json"}
    )
    assert response.status == 400
    assert "validated_errors" in await response.json()


@pytest.mark.asyncio
async def test_hash_string_missing_field(aiohttp_client):
    app = web.Application()
    app.router.add_post("/hash", hash_string)
    client = await aiohttp_client(app)
    data = {}
    response = await client.post("/hash", json=data)
    assert response.status == 400
    assert "validated_errors" in await response.json()
