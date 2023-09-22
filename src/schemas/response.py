from pydantic import BaseModel
from typing import Optional

class Response (BaseModel):
  cod_respuesta:str
  message:Optional[str] = None
  data:Optional[dict]=None