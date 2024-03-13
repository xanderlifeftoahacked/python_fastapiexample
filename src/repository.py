from typing import List
from sqlalchemy import select

import database as db
from schemas import STask, STaskAdd


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with db.new_session() as session:
            task = db.TaskTable(**data.model_dump())
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_all(cls) -> List[STask]:
        async with db.new_session() as session:
            result = await session.execute(select(db.TaskTable))
            tasks = result.scalars().all()
            task_schemas = [STask.model_validate(
                task_model.__dict__) for task_model in tasks]
            return task_schemas
