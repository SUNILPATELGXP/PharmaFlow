from fastapi import FastAPI

from app.core.config import settings
from app.api.router import api_router

app = FastAPI(title = settings.APP_NAME, version = settings.APP_VERSION, 
              description=("Modular Pharma Management""built with Python and Fastapi"),
              debug = settings.DEBUG
              )


app.include_router(api_router, prefix=settings.API_V1_PREFIX)

# root API
@app.get("/", tags=["System"])
def root():
    return {
        "message" : "Welcome to PharmaFlow API",
        "application" : settings.APP_NAME,
        "version" : settings.APP_VERSION,
        "status" : "running"
    }

# Health Check API
@app.get("/health", tags=["System"])
def health_check():
    return {
        "status": "healthy",
        "application": settings.APP_NAME
    }