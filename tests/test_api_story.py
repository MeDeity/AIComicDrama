from fastapi.testclient import TestClient

from ai_comic_drama.app.main import app


client = TestClient(app)


def test_submit_story_returns_task_id():
    response = client.post(
        "/api/v1/story/",
        json={"content": "从前有座山"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "task_id" in data
    assert data["status"] == "success"
    assert data["video_url"]


def test_get_task_status_returns_same_task():
    response = client.post(
        "/api/v1/story/",
        json={"content": "从前有座山"},
    )
    data = response.json()
    task_id = data["task_id"]
    status_response = client.get(f"/api/v1/story/{task_id}")
    assert status_response.status_code == 200
    status_data = status_response.json()
    assert status_data["task_id"] == task_id
    assert status_data["status"] == "success"
    assert status_data["video_url"]
