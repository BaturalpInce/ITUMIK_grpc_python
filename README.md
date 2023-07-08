# Description
This project uses gRPC and contain a gRPC server and client. The purpose is to allow users to request to gRPC server and retreive the needed data. The protobuf format is used on this backend.

The proto file provided in this code contain Chair, Desk, Floor, Library, DeskDataRequest, DeskDataResponse, FloorDataRequest, FloorDataResponse messages. Proto file also contain FloorDataService and DeskDataService which manage the requests and responses using the message types stated previously.

When a request arrive to the gRPC server, it will respond with the according data taken from MongoDB using regular expressions.

# How to Run
Clone the repo.
Create .env file on root folder with this template and fill necessary values:
```
DB_USERNAME = your_username
DB_PASSWORD = your_password
DB_NAME = your_db_name
DB_COLLECTION_NAME = your_db_collection_name
```

On one shell run gRPC server with:
```
python server.py
```
# Using Postman
After opening the server code, you can send gRPC requests from Postman to test.

Example query to retrieve all chairs for spesified floor and desk:
```json
{
    "query": "Floor00/Desk01"
}
```

Example output:
```json
{
    "desks": {
        "VALUES": [
            {
                "chairId": "Chair001",
                "isOccupied": false
            },
            {
                "chairId": "Chair002",
                "isOccupied": true
            },
            {
                "chairId": "Chair003",
                "isOccupied": true
            },
            {
                "chairId": "Chair004",
                "isOccupied": false
            }
        ],
        "TOPIC": "Floor00/Desk01"
    }
}
```

Example query to retreive all desks for spesified floor: 
```json
{
    "floorId": "Floor00"
}
```

Example output:
The output is very long however I will display the format you receive for a floor containing only 2 desks:
```json
{
    "floors": {
        "desks": [
            {
                "VALUES": [
                    {
                        "chairId": "Chair001",
                        "isOccupied": false
                    },
                    {
                        "chairId": "Chair002",
                        "isOccupied": true
                    },
                    {
                        "chairId": "Chair003",
                        "isOccupied": true
                    },
                    {
                        "chairId": "Chair004",
                        "isOccupied": false
                    }
                ],
                "TOPIC": "Floor00/Desk01"
            },
            {
                "VALUES": [
                    {
                        "chairId": "Chair005",
                        "isOccupied": false
                    },
                    {
                        "chairId": "Chair006",
                        "isOccupied": false
                    },
                    {
                        "chairId": "Chair007",
                        "isOccupied": false
                    },
                    {
                        "chairId": "Chair008",
                        "isOccupied": false
                    }
                ],
                "TOPIC": "Floor00/Desk02"
            }
        ]
    }
}
```

# Using Terminal
You can run the client code with "python client.py" and execute the 2 sample queries (same with the ones on Postman explanation).

The resulting output will be same but note that if isOccupied field does not exist on terminal output it is because the isOccupied field value is false and by default gRPC does not display false field values in the response.

# If you want to change Proto file
If any change to library.proto file has been made use this line to compile the changes.
```python
python -m grpc_tools.protoc -I lib/protos --python_out=. --pyi_out=. --grpc_python_out=. lib/protos/library.proto
```