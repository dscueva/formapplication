import grpc
from . import form_processor_pb2
from . import form_processor_pb2_grpc

def send_form_data(form):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = form_processor_pb2_grpc.FormProcessorStub(channel)
        form_data = form_processor_pb2.FormData(
            name=form.name,
            email=form.email,
            message=form.message
        )
        response = stub.ProcessForm(form_data)
        return {"success": response.success, "message": response.message}
