from typing import Tuple, Type, Union

def force_bytes(string: Union[str, bytes]) -> bytes: ...
def force_text(string: Union[str, bytes]) -> str: ...

text_types: Tuple[Type[str]]
numeric_types: Tuple[Type[float], Type[int]]
