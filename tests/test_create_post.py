from utils.api_client import post

def test_create_post():
    payload = {
        "title": "QA Automation Post",
        "body": "Created via API automation test",
        "userId": 1
    }

    response = post("/posts", payload)

    assert response.status_code == 201
    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
