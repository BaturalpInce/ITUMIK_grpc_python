import grpc
import library_pb2
import library_pb2_grpc
from concurrent import futures
from lib.controller import APIController

mongo_controller = APIController()

class LibraryClientService(library_pb2_grpc.FloorDataServiceServicer):
    # display list of desks specified by a floor
    def GetFloorData(self, request, context):
        #print("Got request " + str(request) + " " + str(request.floorId))
        pattern = f'^{request.floorId}'
        documents = list(mongo_controller.mongo_client.collection.find({"TOPIC": {"$regex": pattern}}))
        if documents:
            floor = library_pb2.Floor()
            floor.floorId = request.floorId
            listOfDesks = []
            for i in range(len(documents)):
                #print(documents[i])
                #print(i)
                desk = library_pb2.Desk()
                desk.TOPIC = documents[i].get("TOPIC")
                toAssignChairs = documents[i].get("VALUES")
                listOfChairs = []
                for field, value in toAssignChairs.items():
                    chair = library_pb2.Chair()
                    chair.chairId = field
                    chair.isOccupied = bool(value)
                    listOfChairs.append(chair)
                desk.VALUES.extend(listOfChairs)
                listOfDesks.append(desk)
            floor.desks.extend(listOfDesks)
            return library_pb2.FloorDataResponse(floors=floor)
        else:
            return library_pb2.FloorDataResponse(floors=[])

class DeskClientService(library_pb2_grpc.DeskDataServiceServicer):
    # display list of chairs spesified by a Floor and desk combination
    def GetDeskData(self, request, context):
        #print("Got request " + str(request) + " " + str(request.query))
        document = list(mongo_controller.mongo_client.collection.find({"TOPIC": {"$regex": request.query}}))
        #print(document)
        if document[0]:
            desk = library_pb2.Desk()
            desk.TOPIC = request.query
            iterateOver = document[0].get("VALUES")
            #print(iterateOver)
            listOfChair = []
            for field, value in iterateOver.items():
                chair = library_pb2.Chair()
                chair.chairId = field
                # default grpc behaviour -> if value is false it will not return anything
                # else if value is true it will appear like isOccupied: true
                chair.isOccupied = value
                listOfChair.append(chair)
            desk.VALUES.extend(listOfChair)
            return library_pb2.DeskDataResponse(desks=desk)
        else:
            return library_pb2.DeskDataResponse(desks=[])
  
def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    library_pb2_grpc.add_FloorDataServiceServicer_to_server(LibraryClientService(), server)
    library_pb2_grpc.add_DeskDataServiceServicer_to_server(DeskClientService(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC starting")
    server.start()
    server.wait_for_termination()
server()

channel = grpc.insecure_channel('localhost:50051')
stub = library_pb2_grpc.RouteGuideStub(channel)