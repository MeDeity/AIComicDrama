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
    assert data["status"] == "pending"

