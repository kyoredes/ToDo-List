from httpx import AsyncClient, ConnectError
from comments.config import settings
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
import logging
from comments.database import DbConfig

dbconfig = DbConfig(url=settings.DATABASE_URL_FASTAPI, echo=settings.DEBUG)

logger = logging.getLogger(__name__)

BASE_BACKEND_URL = settings.BASE_BACKEND_URL
BACKEND_LOGIN_URL = settings.BACKEND_LOGIN_URL


async def backend_connection():
    logging.info("===========BACKEND CONNECTION STARTED==========")
    async with AsyncClient() as client:
        logging.info("========ASYNC WITH BACKEBD CONN=========")
        try:
            response = await client.get(settings.BASE_BACKEND_URL)
            logging.info(f"=======RESPONSE {response}=========")
        except HTTPException:
            return False
        if response.status_code == 200:
            return True
        return False


async def get_jwt_token(db: AsyncSession, username: str, password: str):
    async with AsyncClient() as client:
        json_data = {"username": username, "password": password}
        response = await client.post(
            f"{BASE_BACKEND_URL}{BACKEND_LOGIN_URL}", json=json_data
        )
        if response.status_code == 200:
            return response.json()["access"]


async def fetch_task(
    task_id: int,
    username: str,
    password: str,
    db: AsyncSession = Depends(dbconfig.scoped_session_dependency),
):
    logging.info("========FETCHING TASK START=============")
    if not await backend_connection():
        logging.info("=========BACKEND IS NOT CONNECTED=========")
        return False
    async with AsyncClient() as client:
        logging.info("======ASYNC WITH FETCH TASK STARTED=========")
        logging.info(f"=======USERNAME: {username} PASSWORD: {password}=========")

        jwt_token = await get_jwt_token(db=db, username=username, password=password)
        logging.info(f"=======JWT TOKEN: {jwt_token}=========")

        headers = {"Authorization": f"Bearer {jwt_token}"}
        response = await client.get(
            f"{BASE_BACKEND_URL}/tasks/{task_id}/", headers=headers
        )
        if response.status_code == 200:
            return response.json()
    return False
