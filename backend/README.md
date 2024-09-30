# Form Application

**Form Application** is a demo project to process forms. It leverages **FastAPI** for handling HTTP requests and **gRPC** for efficient inter-service communication. This project is set up using a virtual environment to ensure dependency isolation and ease of development.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Running the Application](#running-the-application)
  - [1. Activate the Virtual Environment](#1-activate-the-virtual-environment)
  - [2. Terminal 1: Start the FastAPI Server](#2-terminal-1-start-the-fastapi-server)
  - [3. Terminal 2: Start the gRPC Server](#3-terminal-2-start-the-grpc-server)
  - [4. Terminal 3: Interact with the API using `curl`](#4-terminal-3-interact-with-the-api-using-curl)
- [Testing the API](#testing-the-api)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Features

- **FastAPI Backend:** Handles HTTP requests for form submissions with automatic data validation and interactive API documentation.
- **gRPC Integration:** Efficiently processes form data using gRPC for inter-service communication.
- **Virtual Environment:** Ensures isolated and manageable project dependencies.
- **Separate Server Processes:** FastAPI and gRPC servers run independently for modularity and ease of debugging.
- **Interactive API Docs:** Accessible via Swagger UI for easy testing and exploration.

---

## Prerequisites

Before setting up the project, ensure you have the following installed on your system:

- **Python 3.7+**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package installer (comes bundled with Python)
- **Git**: For cloning the repository (optional)
- **Terminal Emulator**: Such as Terminal on macOS/Linux or PowerShell on Windows

---

## Installation

### 1. Clone the Repository

If you haven't already, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/project-backend.git
cd project-backend/backend
```

*Replace `https://github.com/yourusername/project-backend.git` with your actual repository URL.*

### 2. Create and Activate a Virtual Environment

It's best practice to use a virtual environment to manage project-specific dependencies.

```bash
# Navigate to the backend directory
cd backend

# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

*You should see `(venv)` prefixed in your terminal prompt, indicating that the virtual environment is active.*

### 3. Install Dependencies

With the virtual environment activated, install the required Python packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

*Ensure that `requirements.txt` contains the necessary dependencies:*

```
fastapi
uvicorn
grpcio
grpcio-tools
pydantic[email]
```

### 4. Generate gRPC Code

Generate the necessary gRPC Python files from the `.proto` definition:

```bash
python -m grpc_tools.protoc -I./proto --python_out=./app --grpc_python_out=./app ./proto/form_processor.proto
```

*This command generates `form_processor_pb2.py` and `form_processor_pb2_grpc.py` in the `app/` directory.*

---

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── grpc_client.py
│   ├── grpc_server.py
│   ├── form_processor_pb2.py
│   └── form_processor_pb2_grpc.py
├── proto/
│   └── form_processor.proto
├── requirements.txt
└── README.md
```

- **app/**: Contains the FastAPI and gRPC server implementations.
- **proto/**: Contains the Protocol Buffers definition for gRPC services.

---

## Running the Application

To effectively run and monitor both the **FastAPI** and **gRPC** servers, you'll use three separate terminal windows:

1. **Terminal 1:** FastAPI server
2. **Terminal 2:** gRPC server
3. **Terminal 3:** `curl` commands or other interactions

### 1. Activate the Virtual Environment

Ensure your virtual environment is activated in all relevant terminals.

```bash
cd /path/to/project-backend/backend
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate    # On Windows
```

### 2. Terminal 1: Start the FastAPI Server

In the first terminal window, run the FastAPI server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

**Expected Output:**

```
INFO:     Will watch for changes in these directories: ['/path/to/project-backend/backend/app']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [PID] using StatReload
```

*This server handles HTTP requests and provides interactive API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).*

### 3. Terminal 2: Start the gRPC Server

In the second terminal window, run the gRPC server:

```bash
python app/grpc_server.py
```

**Expected Output:**

```
gRPC server started on port 50051
```

*This server listens for gRPC requests on port `50051` and processes form data.*

### 4. Terminal 3: Interact with the API using `curl`

Use the third terminal to send `curl` commands to your FastAPI server for testing purposes.

**Example `curl` Command:**

```bash
curl -X POST "http://localhost:8000/submit-form" \
-H "Content-Type: application/json" \
-d '{"name":"Alice","email":"alice@example.com","message":"Hello!"}'
```

**Expected Response:**

```json
{
  "status": "success",
  "data": {
    "success": true,
    "message": "Form processed successfully."
  }
}
```

*Additionally, in Terminal 2 (gRPC Server), you should see:*

```
Received form data: Name=Alice, Email=alice@example.com, Message=Hello!
```

---

## Testing the API

Beyond using `curl`, you can leverage FastAPI's interactive API documentation to test your endpoints:

1. **Open Your Browser:**
   - Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

2. **Use Swagger UI:**
   - Locate the `POST /submit-form` endpoint.
   - Click "Try it out."
   - Input sample data and execute the request.
   - Observe the response directly in the browser.
   - Check Terminal 2 for corresponding gRPC server logs.

---

## Troubleshooting

### 1. **Module Import Errors (`ModuleNotFoundError: No module named 'form_processor_pb2'`):**

**Cause:** The gRPC Python files (`form_processor_pb2.py` and `form_processor_pb2_grpc.py`) are not correctly generated or imported.

**Solution:**

- **Ensure Relative Imports:**
  - Open `app/form_processor_pb2_grpc.py` and modify the import statement:
    ```python
    from . import form_processor_pb2 as form__processor__pb2
    ```
- **Verify Generated Files:**
  - Ensure both `form_processor_pb2.py` and `form_processor_pb2_grpc.py` exist in the `app/` directory.
- **Re-generate gRPC Code:**
  ```bash
  python -m grpc_tools.protoc -I./proto --python_out=./app --grpc_python_out=./app ./proto/form_processor.proto
  ```

### 2. **Protobuf Version Warning:**

```
UserWarning: Protobuf gencode version 5.27.2 is older than the runtime version 5.28.2 at form_processor.proto. Please avoid checked-in Protobuf gencode that can be obsolete.
```

**Solution:**

- **Upgrade `grpcio-tools`:**
  ```bash
  pip install --upgrade grpcio-tools
  ```
- **Re-generate gRPC Code:**
  ```bash
  python -m grpc_tools.protoc -I./proto --python_out=./app --grpc_python_out=./app ./proto/form_processor.proto
  ```

### 3. **Empty Reply from Server (`curl: (52) Empty reply from server`):**

**Cause:** The FastAPI server might not be running correctly or encountered a runtime error.

**Solution:**

- **Check FastAPI Server Logs:**
  - Ensure there are no errors in Terminal 1.
- **Verify Server is Running:**
  - Confirm that Uvicorn is active and listening on port `8000`.
- **Validate Endpoint URL and Payload:**
  - Ensure you're sending the request to `http://localhost:8000/submit-form` with the correct JSON payload.

### 4. **General Debugging Steps:**

- **Restart Servers:**
  - Stop and restart both FastAPI and gRPC servers.
- **Check Python Path:**
  - Ensure you're running scripts from the correct directory with the virtual environment activated.
- **Regenerate gRPC Code:**
  - If issues persist, delete and re-generate `form_processor_pb2.py` and `form_processor_pb2_grpc.py`.

---

## Future Enhancements

- **Frontend Development:**
  - Expand the frontend to include a user interface for form submissions using framework NextJS.

- **Database Integration:**
  - Integrate a database (e.g., PostgreSQL, SQLite) to store form submissions persistently.

- **Authentication & Authorization:**
  - Implement security measures to protect API endpoints and manage user access.

- **Logging & Monitoring:**
  - Enhance logging mechanisms and integrate monitoring tools for better observability.

- **Testing:**
  - Develop unit and integration tests to ensure application reliability and stability.

---

## License

[MIT](https://choosealicense.com/licenses/mit/)

*This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.*

---

## Acknowledgements

- **FastAPI:** [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- **gRPC:** [https://grpc.io/](https://grpc.io/)
- **Protocol Buffers:** [https://developers.google.com/protocol-buffers](https://developers.google.com/protocol-buffers)
- **Pydantic:** [https://pydantic-docs.helpmanual.io/](https://pydantic-docs.helpmanual.io/)

---

## Contact

For any questions or support, please contact [dscueva@gmail.com](mailto:dscueva@gmail.com).

---

🚀

---

