# backend/app/grpc_server.py

import grpc
from concurrent import futures
import time
import re
from . import form_processor_pb2
from . import form_processor_pb2_grpc

def is_valid_email(email: str) -> bool:
    # Simple regex for email validation
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email) is not None

class FormProcessorServicer(form_processor_pb2_grpc.FormProcessorServicer):
    def ProcessForm(self, request, context):
        # Validate email
        if not is_valid_email(request.email):
            return form_processor_pb2.FormResponse(success=False, message="Invalid email address.")
        
        # Process the form
        print(f"Received form data: Name={request.name}, Email={request.email}, Message={request.message}")
        return form_processor_pb2.FormResponse(success=True, message="Form processed successfully.")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    form_processor_pb2_grpc.add_FormProcessorServicer_to_server(FormProcessorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server started on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
