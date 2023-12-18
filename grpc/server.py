import grpc
from concurrent import futures
import time
import model_pb2
import model_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class ModelService(model_pb2_grpc.ModelServiceServicer):
    def __init__(self):
        self.training_status = "Waiting"

    def GetStatus(self, request, context):
        return model_pb2.ModelStatus(status=self.training_status)

    def TrainModel(self, request, context):
        self.training_status = "prepare for training"
        # training
        
        

        # end
        return model_pb2.TrainResponse(message="training have started")
    

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    model_pb2_grpc.add_ModelServiceServicer_to_server(ModelService(), server)
    server.add_insecure_port(f'[::]:{port}')
    print("Server started, listening on " + port)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
