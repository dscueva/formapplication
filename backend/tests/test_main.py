# backend/tests/test_main.py

from unittest.mock import patch
from app.main import app
from app.models import FormData

def test_submit_form_with_mocked_send_form_data(client):
    with patch('app.main.send_form_data') as mock_send_form_data:
        # Define the mock return value
        mock_send_form_data.return_value = {
            "success": True,
            "message": "Form processed successfully."
        }

        # Sample form data
        form_data = {
            "name": "Alice",
            "email": "alice@example.com",
            "message": "Hello!"
        }

        # Make a POST request to the /submit-form endpoint
        response = client.post("/submit-form", json=form_data)

        # Assert the response status code
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

        # Assert the response JSON
        assert response.json() == {
            "status": "success",
            "data": {
                "success": True,
                "message": "Form processed successfully."
            }
        }, f"Unexpected response JSON: {response.json()}"

        # Ensure that send_form_data was called once with the correct FormData
        mock_send_form_data.assert_called_once()
        mock_send_form_data.assert_called_with(FormData(**form_data))
