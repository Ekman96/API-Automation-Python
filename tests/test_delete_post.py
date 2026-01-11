from utils.api_client import delete

def test_delete_post():
    response = delete("/posts/1")
    assert response.status_code in [200, 204]
