def test_post_task_positive(client, unique_name):
    payload = {"name": unique_name}
    r = client.create_task(payload)
    assert r.status_code in (200, 201), f"Не создалась задача: {r.status_code} {r.text}"
    data = r.json()
    assert data["result"] == "ok"


def test_get_task_positive(client, created_task):
    task_id = created_task["id"]
    r = client.get_task(task_id)
    assert r.status_code == 200
    data = r.json()
    assert data["result"] == "ok"
    assert data["task"]["id"] == task_id


def test_put_task_positive(client, created_task):
    task_id = created_task["id"]
    new_name = created_task["name"] + "_updated"
    payload = {"name": new_name}
    r = client.update_task(task_id, payload)
    assert r.status_code in (200, 201)
    data = r.json()
    assert data["result"] == "ok"
