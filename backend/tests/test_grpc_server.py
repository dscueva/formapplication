# backend/tests/test_grpc_server.py

import pytest
import grpc
from concurrent import futures
from app.grpc_server import FormProcessorServicer
from app import form_processor_pb2
from app import form_processor_pb2_grpc

@pytest.fixture(scope="module")
def grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicer = FormProcessorServicer()
    form_processor_pb2_grpc.add_FormProcessorServicer_to_server(servicer, server)
    port = server.add_insecure_port('[::]:0')  # Bind to a free port
    server.start()
    yield port  # Provide the port to the test
    server.stop(0)

@pytest.fixture
def grpc_stub(grpc_server):
    port = grpc_server
    channel = grpc.insecure_channel(f'localhost:{port}')
    stub = form_processor_pb2_grpc.FormProcessorStub(channel)
    yield stub
    channel.close()

def test_process_form_success(grpc_stub):
    # Create a sample form request with a valid email
    request = form_processor_pb2.FormData(
        name="Alice",
        email="alice@example.com",
        message="Hello!"
    )

    # Call the ProcessForm method
    response = grpc_stub.ProcessForm(request)

    # Assert the response
    assert response.success == True
    assert response.message == "Form processed successfully."

def test_process_form_invalid_email(grpc_stub):
    # Create a sample form request with an invalid email
    request = form_processor_pb2.FormData(
        name="Bob",
        email="invalid-email",
        message="Hi!"
    )

    # Call the ProcessForm method
    response = grpc_stub.ProcessForm(request)

    # Assert the response
    assert response.success == False
    assert response.message == "Invalid email address."
