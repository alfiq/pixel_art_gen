"""API and Integration tests for PixelForge.

Purpose:
    Verify that the FastAPI web server correctly integrates the core generation logic
    with the filesystem and serves assets to the frontend.

Dependencies:
    - fastapi.testclient
    - main (app instance)
    - os
"""
import os
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root() -> None:
    """Verify that the home page serves HTML correctly.
    
    Rationale:
        The dashboard is the primary entry point for users.
    Process:
        Request '/' and check Content-Type and keyword presence.
    Inputs:
        GET /.
    Expectations:
        200 OK, 'text/html', and contains 'PixelForge'.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "PixelForge" in response.text

def test_generate_endpoint() -> None:
    """Verify that the /generate endpoint returns valid sprite metadata.
    
    Rationale:
        The generator API is the core link between the logic and the UI.
    Process:
        Perform a GET request with specific dimensions and check the JSON payload.
    Inputs:
        Width=16, Height=16, Scale=2.
    Expectations:
        200 OK, returns 'image_url' and 'palette' (3 ramps), and file exists.
    """
    response = client.get("/generate?width=16&height=16&scale=2")
    assert response.status_code == 200
    
    data = response.json()
    assert "image_url" in data
    assert "palette" in data
    assert len(data["palette"]) == 3 
    
    image_path = data["image_url"].replace("/output/", "output/")
    assert os.path.exists(image_path)
