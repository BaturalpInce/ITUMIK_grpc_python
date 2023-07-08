from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Chair(_message.Message):
    __slots__ = ["chairId", "isOccupied"]
    CHAIRID_FIELD_NUMBER: _ClassVar[int]
    ISOCCUPIED_FIELD_NUMBER: _ClassVar[int]
    chairId: str
    isOccupied: bool
    def __init__(self, chairId: _Optional[str] = ..., isOccupied: bool = ...) -> None: ...

class Desk(_message.Message):
    __slots__ = ["TOPIC", "VALUES"]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    TOPIC: str
    VALUES: _containers.RepeatedCompositeFieldContainer[Chair]
    def __init__(self, TOPIC: _Optional[str] = ..., VALUES: _Optional[_Iterable[_Union[Chair, _Mapping]]] = ...) -> None: ...

class Library(_message.Message):
    __slots__ = ["floors"]
    FLOORS_FIELD_NUMBER: _ClassVar[int]
    floors: _containers.RepeatedCompositeFieldContainer[Floor]
    def __init__(self, floors: _Optional[_Iterable[_Union[Floor, _Mapping]]] = ...) -> None: ...

class Floor(_message.Message):
    __slots__ = ["floorId", "desks"]
    FLOORID_FIELD_NUMBER: _ClassVar[int]
    DESKS_FIELD_NUMBER: _ClassVar[int]
    floorId: str
    desks: _containers.RepeatedCompositeFieldContainer[Desk]
    def __init__(self, floorId: _Optional[str] = ..., desks: _Optional[_Iterable[_Union[Desk, _Mapping]]] = ...) -> None: ...

class FloorDataRequest(_message.Message):
    __slots__ = ["floorId"]
    FLOORID_FIELD_NUMBER: _ClassVar[int]
    floorId: str
    def __init__(self, floorId: _Optional[str] = ...) -> None: ...

class FloorDataResponse(_message.Message):
    __slots__ = ["floors"]
    FLOORS_FIELD_NUMBER: _ClassVar[int]
    floors: Floor
    def __init__(self, floors: _Optional[_Union[Floor, _Mapping]] = ...) -> None: ...

class DeskDataRequest(_message.Message):
    __slots__ = ["query"]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: str
    def __init__(self, query: _Optional[str] = ...) -> None: ...

class DeskDataResponse(_message.Message):
    __slots__ = ["desks"]
    DESKS_FIELD_NUMBER: _ClassVar[int]
    desks: Desk
    def __init__(self, desks: _Optional[_Union[Desk, _Mapping]] = ...) -> None: ...
