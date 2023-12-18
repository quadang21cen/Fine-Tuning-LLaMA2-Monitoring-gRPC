import grpc
import model_pb2
import model_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = model_pb2_grpc.ModelServiceStub(channel)
    
    # get status of model
    status_response = stub.GetStatus(model_pb2.Empty())
    print("Model Status:", status_response.status)

    # training
    train_response = stub.TrainModel(model_pb2.Empty())
    print("respond from training:", train_response.message)

if __name__ == '__main__':
    run()
