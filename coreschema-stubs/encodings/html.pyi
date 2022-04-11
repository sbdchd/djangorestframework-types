from typing import Any

from coreschema import Array as Array
from coreschema import Boolean as Boolean
from coreschema import Enum as Enum
from coreschema import Integer as Integer
from coreschema import Number as Number
from coreschema import Object as Object
from coreschema import String as String

env: Any

def render_to_form(schema: Any) -> Any: ...
def determine_html_template(schema: Any) -> Any: ...
def get_textarea_value(schema: Any) -> Any: ...
def get_attrs(schema: Any) -> Any: ...
