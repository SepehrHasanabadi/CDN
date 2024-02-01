import json
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_create_user(mocker):
    mocker.patch(
        "app.api.v1.crud.file.update_or_create_file_in_db",
        return_value={
            "id": 1,
            "minify_ram_consumption": "1 B",
            "minify_duration": "1 ms",
            "path": "/",
            "size": "1 KB",
            "type": "css",
            "user_id": 1,
        },
    )

    file_content = b"Mocked file content"

    form_data = {
        "file": ("test_file.css", file_content),
        "minify": "false",
    }
    response = client.post("/cache-file/", data=form_data)
    expected_response = {
        "minify_ram_consumption": "1 B",
        "minify_duration": "1 ms",
        "path": "/",
        "size": "1 KB",
        "type": "css",
    }
    assert response.status_code, 200
    assert response.json(), json.dumps(expected_response)
