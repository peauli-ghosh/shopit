from fastapi import APIRouter

from app.db.postgres import get_connection
from app.db.redis import get_redis


api_router = APIRouter()


@api_router.get("/")
def root():
    return {"message": "ShopIt API is running"}


@api_router.get("/health")
def health():
    postgres_status = "ok"
    redis_status = "ok"

    try:
        conn = get_connection()
        conn.close()
    except Exception:
        postgres_status = "error"

    try:
        redis_client = get_redis()
        redis_client.ping()
        redis_client.close()
    except Exception:
        redis_status = "error"

    overall_status = (
        "healthy"
        if postgres_status == "ok" and redis_status == "ok"
        else "unhealthy"
    )

    return {
        "status": overall_status,
        "services": {
            "postgres": postgres_status,
            "redis": redis_status,
        },
    }
