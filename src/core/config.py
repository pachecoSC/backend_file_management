from pydantic import BaseModel

class Settings(BaseModel):
  API_V1_STR: str = '/api/v1'

  class Config:
    case_sensitive = True

settings = Settings()