from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import CommentCreate, CommentResponse, CommentUpdate
from .models.comment_models import Comment
from sqlalchemy import select
import logging


async def create_comment(db: AsyncSession, comment: CommentCreate):
    new_comment = Comment(**comment.model_dump())
    db.add(new_comment)
    await db.commit()
    return new_comment


async def get_comment(db: AsyncSession, comment_id: int):
    res = await db.execute(select(Comment).where(Comment.id == comment_id))
    return res.scalars().first()


async def get_comments_by_task(db: AsyncSession, task_id: int):
    res = await db.execute(select(Comment).where(Comment.task_id == task_id))
    return res.scalars().all()


async def update_comment(db: AsyncSession, comment_id: int, comment: CommentUpdate):
    existing_comment = await db.get(Comment, comment_id)
    if existing_comment:
        existing_comment.text = comment.text
        await db.commit()
        return existing_comment


async def delete_comment(db: AsyncSession, comment_id: int):
    comment = await db.get(Comment, comment_id)
    logging.info(f"=======DELETING COMMENT: {comment}=========")
    if comment:
        logging.info("=====COMMENT EXISTS=============")
        await db.delete(comment)
        await db.commit()
        return True
    return False
