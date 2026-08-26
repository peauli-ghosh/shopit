from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings


@asynccontextmanager
async def lifespan(application: FastAPI):
    print("ShopIt API starting...")
    yield
    print("ShopIt API shutting down...")


def create_application() -> FastAPI:
    application = FastAPI(
        title="ShopIt",
        version="0.1.0",
        description=(
            "AI-powered shopping platform for product discovery, "
            "search, comparison, recommendations, and purchasing."
        ),
        debug=settings.debug,
        lifespan=lifespan,
    )

    application.include_router(api_router)

    return application


app = create_application()
