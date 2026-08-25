from fastapi import FastAPI

from app.core.config import settings


app = FastAPI(
    title="ShopIt",
    version="0.1.0",
    debug=settings.debug,
)


@app.get("/")
def root():
    return {"message": "ShopIt API is running"}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "environment": settings.environment,
    }