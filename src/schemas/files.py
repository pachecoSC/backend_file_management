from typing import Optional
from pydantic import BaseModel,EmailStr

class File(BaseModel):
    name_file: Optional[str] = None
    content: str

class  ListaFile(BaseModel):
    lista: list = None