from fastapi import FastAPI
from fastapi.testclient import TestClient
from mylib.logic import wiki,summary

from main import app 

client = TestClient(app)

def test_check_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Wikipedia API! You can Call, Search or Wiki"}