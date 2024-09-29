import grpc
from concurrent import futures
import time

from . import form_processor_pb2
from . import form_processor_pb2_grpc

class FormProcessorServicer(form_processor_pb2_grpc.FormProcessorServicer):
    def ProcessForm(self, request, context):
        # we can modify this to store somewhere
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
