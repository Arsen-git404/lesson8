import uuid
import pytest
from api import YougileClient


@pytest.fixture(scope="session")
def client() -> YougileClient:
    return YougileClient()


@pytest.fixture(scope="function")
def unique_name() -> str:
    return f"autotest-{uuid.uuid4().hex[:8]}"


@pytest.fixture(scope="function")
def created_task(client, unique_name):
    """Создаёт задачу и возвращает её данные"""
    payload = {"name": unique_name}
    r = client.create_task(payload)
    assert r.status_code in (200, 201), f"Не создалась задача: {r.status_code} {r.text}"
    data = r.json()
    yield data
