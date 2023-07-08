import grpc

import library_pb2
import library_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = library_pb2_grpc.FloorDataServiceStub(channel)        
        response = stub.GetFloorData(library_pb2.FloorDataRequest(floorId="Floor00"))
        print(response)

        print("*************")
        
        stub2 = library_pb2_grpc.DeskDataServiceStub(channel)
        response2 = stub2.GetDeskData(library_pb2.DeskDataRequest(query="Floor00/Desk01"))
        print(response2)

run()