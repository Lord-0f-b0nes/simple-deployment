from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_get_tasks():
    client = app.test_client()
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_add_task():
    client = app.test_client()
    response = client.post("/tasks", json={"title": "New task"})
    assert response.status_code == 201
    assert response.get_json()["title"] == "New task"


def test_add_task_missing_title():
    client = app.test_client()
    response = client.post("/tasks", json={})
    assert response.status_code == 400
