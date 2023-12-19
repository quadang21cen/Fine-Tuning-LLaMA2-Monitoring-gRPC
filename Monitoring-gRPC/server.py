import grpc
from concurrent import futures
import llama2_pb2
import llama2_pb2_grpc
from until import to_base64


class LLamaService(llama2_pb2_grpc.LLamaServiceServicer):
    
    def UploadImage(self, request, context):
        image = request.image

        to_base64.image_to_base64(image)

        return llama2_pb2.StatusResponse(status="Image uploaded successfully")

    def GetStatus(self, request, context):


        return llama2_pb2.StatusResponse(status="Model is training/validating")

    def Predict(self, request, context):
        image_content = request.input

        return llama2_pb2.PredictionResponse(result="Prediction result")

    def ExportModel(self, request, context):
        format = request.format


        return llama2_pb2.StatusResponse(status="Model exported successfully")

    def CreateDataset(self, request, context):
        dataset_name = request.dataset

        return llama2_pb2.StatusResponse(status="Dataset created successfully")

    def ViewLogs(self, request, context):
        logs = "Logs content"
        
        return llama2_pb2.LogResponse(logs=logs)

    def DownloadCheckpoint(self, request, context):

        checkpoint_content = b"Checkpoint content"


        return llama2_pb2.FileResponse(file_content=checkpoint_content)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    llama2_pb2_grpc.add_LLamaServiceServicer_to_server(LLamaService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
