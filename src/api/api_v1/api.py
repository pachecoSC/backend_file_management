from fastapi import APIRouter

from src.api.api_v1.endpoints import filemanagement

api_router = APIRouter()

api_router.include_router(filemanagement.router,prefix='/filesmanagement',tags=['filesmanagement'])