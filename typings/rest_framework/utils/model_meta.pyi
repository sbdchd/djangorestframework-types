from typing import Any, Dict, NamedTuple, Optional, Type

from django.db.models import Model
from django.db.models.fields import Field
from django.db.models.fields.related import RelatedField

class RelationInfo(NamedTuple):
    model_field: Optional[RelatedField[Any, Any]]
    related_model: Type[Model]
    to_many: bool
    to_field: str
    has_through_model: bool
    reverse: bool

class FieldInfo(NamedTuple):
    pk: Field[Any, Any]
    fields: Dict[str, Field[Any, Any]]
    forward_relations: Dict[str, RelationInfo]
    reverse_relations: Dict[str, RelationInfo]
    fields_and_pk: Dict[str, Field[Any, Any]]
    relations: Dict[str, RelationInfo]

def get_field_info(model: Type[Model]) -> FieldInfo: ...
def is_abstract_model(model: Type[Model]) -> bool: ...
