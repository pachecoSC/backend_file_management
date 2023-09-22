import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from  src.api.api_v1.api import api_router
from src.core.config import settings

app = FastAPI(title='conversor de archivos', openapi_url=f'{settings.API_V1_STR}/openapi.json')

app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get('/')
async def root():
  return 'Welcome RmSystem'

def serve():
    """Serve the web application."""
    uvicorn.run(app, port=8001)

if __name__ == "__main__":
    serve()