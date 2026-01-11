from utils.api_client import put

def test_update_post():
    payload = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated body text",
        "userId": 1
    }

    response = put("/posts/1", payload)

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == 1
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
