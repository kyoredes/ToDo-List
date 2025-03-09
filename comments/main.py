from fastapi import FastAPI
from comments.app.routers import router
import logging
from redis.asyncio import Redis

logging.basicConfig(level=logging.INFO)

app = FastAPI(debug=True)

app.include_router(router)
