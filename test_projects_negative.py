import pytest

@pytest.mark.parametrize("payload", [
    {},  # пустое тело
    {"name": ""},  # пустое имя
    {"name": None},  # null-значение
])
def test_post_task_negative(client, payload):
    r = client.create_task(payload)
    assert r.status_code in (400, 422)
    data = r.json()
    assert data["result"] == "error"
