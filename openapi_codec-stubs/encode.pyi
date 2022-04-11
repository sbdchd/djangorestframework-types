from typing import Any

from openapi_codec.utils import get_encoding as get_encoding
from openapi_codec.utils import get_links_from_document as get_links_from_document
from openapi_codec.utils import get_location as get_location
from openapi_codec.utils import get_method as get_method

def generate_swagger_object(document: Any) -> Any: ...
