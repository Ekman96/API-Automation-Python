import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get(endpoint: str):
    return requests.get(f"{BASE_URL}{endpoint}")

def post(endpoint: str, payload: dict):
    return requests.post(f"{BASE_URL}{endpoint}", json=payload)

def put(endpoint: str, payload: dict):
    return requests.put(f"{BASE_URL}{endpoint}", json=payload)

def delete(endpoint: str):
    return requests.delete(f"{BASE_URL}{endpoint}")
