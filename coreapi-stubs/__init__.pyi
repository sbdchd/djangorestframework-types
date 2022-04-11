from typing import NamedTuple

from coreschema.schemas import Schema

class Fields: ...

class Field(NamedTuple):
    name: str
    required: bool
    location: str
    schema: Schema

class Document: ...
class Link: ...
class Client: ...
