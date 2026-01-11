import requests

def test_get_post_by_id():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    assert response.status_code == 200
    body = response.json()

    assert body["id"] == 1
    assert "userId" in body
    assert "title" in body
    assert "body" in body
