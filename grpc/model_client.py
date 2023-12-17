import grpc
import model_pb2
import model_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = model_pb2_grpc.ModelServiceStub(channel)
    
    # Lấy trạng thái hiện tại của mô hình
    status_response = stub.GetStatus(model_pb2.Empty())
    print("Trạng thái hiện tại của mô hình:", status_response.status)

    # Bắt đầu quá trình đào tạo
    train_response = stub.TrainModel(model_pb2.Empty())
    print("Phản hồi từ quá trình đào tạo:", train_response.message)

if __name__ == '__main__':
    run()
