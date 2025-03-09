from fastapi import APIRouter, Depends, HTTPException
from comments.app.schemas import RequestBody, CommentResponse
from comments.app import crud
from comments.database import dbconfig
from sqlalchemy.ext.asyncio import AsyncSession
from comments.external_backend import fetch_task
from comments.config import settings
from .models.comment_models import Comment
import logging
from comments.redis import get_redis
import json
from redis.asyncio import Redis
from fastapi.encoders import jsonable_encoder

logger = logging.getLogger(__name__)
BASE_BACKEND_URL = settings.BASE_BACKEND_URL

router = APIRouter(prefix="/comments", tags=["comments"])


@router.get("/tasks/{task_id}/")
async def get_comments_by_task_view(
    task_id: int,
    db: AsyncSession = Depends(dbconfig.scoped_session_dependency),
    redis_client: Redis = Depends(get_redis),
):
    cache_key = f"task:{task_id}:comments"
    cached_data = await redis_client.get(cache_key)
    if cached_data:
        logging.info(f"=======CACHED DATA: {cached_data}=========")
        return json.loads(cached_data)

    comments = await crud.get_comments_by_task(db=db, task_id=task_id)
    comments_list = jsonable_encoder(comments)
    await redis_client.setex(cache_key, 340, json.dumps(comments_list))
    return comments


@router.get("/{comment_id}/", response_model=CommentResponse)
async def get_comment_view(
    comment_id: int, db: AsyncSession = Depends(dbconfig.scoped_session_dependency)
):
    comment = await crud.get_comment(db=db, comment_id=comment_id)
    return comment


@router.post("/", response_model=CommentResponse)
async def create_comment_view(
    request_body: RequestBody,
    db: AsyncSession = Depends(dbconfig.scoped_session_dependency),
    redis_client: Redis = Depends(get_redis),
):
    task_id = await fetch_task(
        task_id=request_body.comment.task_id,
        username=request_body.login_data.username,
        password=request_body.login_data.password,
    )

    if task_id:
        cache_key = f"task:{task_id}:comments"
        new_comment = await crud.create_comment(comment=request_body.comment, db=db)
        await redis_client.setex(cache_key, 340, json.dumps(new_comment))
        return new_comment

    raise HTTPException(status_code=404, detail="Task does not exist")


@router.put("/{comment_id}/", response_model=CommentResponse)
async def update_comment_view(
    comment_id: int,
    request_body: RequestBody,
    db: AsyncSession = Depends(dbconfig.scoped_session_dependency),
    redis_client: Redis = Depends(get_redis),
):
    logging.info("=======UPDATE COMMENT VIEW STARTED=========")
    updated_comment = await crud.update_comment(
        comment_id=comment_id, comment=request_body.comment, db=db
    )

    if updated_comment:
        logging.info(f"=======UPDATED COMMENT VIEW: {updated_comment}=========")
        cache_key = f"comments:{comment_id}"
        new_comment_list = jsonable_encoder(updated_comment)
        await redis_client.setex(cache_key, 340, json.dumps(new_comment_list))
        return updated_comment

    raise HTTPException(status_code=404, detail="Comment does not exist")


@router.delete("/{comment_id}/")
async def delete_comment_view(
    comment_id: int,
    db: AsyncSession = Depends(dbconfig.scoped_session_dependency),
    redis_client: Redis = Depends(get_redis),
):
    deleted_comment = await crud.delete_comment(comment_id=comment_id, db=db)
    if deleted_comment:
        cache_key = f"comments:{comment_id}"
        await redis_client.delete(cache_key)
        return {"message": "Comment deleted successfully"}
    raise HTTPException(status_code=404, detail="Comment does not exist")
