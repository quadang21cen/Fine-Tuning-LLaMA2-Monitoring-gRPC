import grpc
import llama2_pb2
import llama2_pb2_grpc

def upload_image():
    with open('path/to/your/image.jpg', 'rb') as image_file:
        image_content = image_file.read()
        image_content_base64 = image_content.encode('base64').decode('utf-8')

        channel = grpc.insecure_channel('localhost:50051')
        stub = llama2_pb2_grpc.LLamaServiceStub(channel)

        response = stub.UploadImage(llama2_pb2.ImageRequest(image_content=image_content_base64))
        print("UploadImage Response:", response.status)

def get_status():
    channel = grpc.insecure_channel('localhost:50051')
    stub = llama2_pb2_grpc.LLamaServiceStub(channel)

    response = stub.GetStatus(llama2_pb2.EmptyRequest())
    print("GetStatus Response:", response.status)

def predict():
    with open('path/to/your/image.jpg', 'rb') as image_file:
        image_content = image_file.read()
        image_content_base64 = image_content.encode('base64').decode('utf-8')

        channel = grpc.insecure_channel('localhost:50051')
        stub = llama2_pb2_grpc.LLamaServiceStub(channel)

        response = stub.Predict(llama2_pb2.PredictionRequest(image_content=image_content_base64))
        print("Predict Response:", response.result)

def export_model():
    channel = grpc.insecure_channel('localhost:50051')
    stub = llama2_pb2_grpc.LLamaServiceStub(channel)

    response = stub.ExportModel(llama2_pb2.ModelExportRequest(format="tensorflow"))
    print("ExportModel Response:", response.status)

def create_dataset():
    channel = grpc.insecure_channel('localhost:50051')
    stub = llama2_pb2_grpc.LLamaServiceStub(channel)

    response = stub.CreateDataset(llama2_pb2.DatasetRequest(dataset_name="my_dataset"))
    print("CreateDataset Response:", response.status)

def view_logs():
    channel = grpc.insecure_channel('localhost:50051')
    stub = llama2_pb2_grpc.LLamaServiceStub(channel)

    response = stub.ViewLogs(llama2_pb2.EmptyRequest())
    print("ViewLogs Response:", response.logs)

def download_checkpoint():
    channel = grpc.insecure_channel('localhost:50051')
    stub = llama2_pb2_grpc.LLamaServiceStub(channel)

    response = stub.DownloadCheckpoint(llama2_pb2.EmptyRequest())
    with open('checkpoint.tar.gz', 'wb') as checkpoint_file:
        checkpoint_file.write(response.file_content)
    print("DownloadCheckpoint Response: Checkpoint saved to checkpoint.tar.gz")

if __name__ == '__main__':
    upload_image()
    get_status()
    predict()
    export_model()
    create_dataset()
    view_logs()
    download_checkpoint()
