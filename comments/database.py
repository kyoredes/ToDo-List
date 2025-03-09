from comments.config import settings
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)
from asyncio import current_task


class DbConfig:
    def __init__(self, url: str, echo: bool = True):
        self.async_engine = create_async_engine(
            settings.DATABASE_URL_FASTAPI,
            echo=settings.DEBUG,
            connect_args={"check_same_thread": False},
        )
        self.session_factory = async_sessionmaker(
            bind=self.async_engine,
            expire_on_commit=False,
            autocommit=False,
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory, scopefunc=current_task
        )
        return session

    async def scoped_session_dependency(self):
        session = self.get_scoped_session()
        yield session
        await session.close()


dbconfig = DbConfig(url=settings.DATABASE_URL_FASTAPI, echo=settings.DEBUG)
