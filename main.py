from fastapi import APIRouter

from routes import login, users, private
from core.config import settings

router = APIRouter()
router.include_router(login.router)
router.include_router(users.router)

if settings.ENVIRONMENT == "local":
    router.include_router(private.router)