from typing import List
from sqlalchemy import select

import database as db
from schemas import STask, STaskAdd, SUser, SUserAdd
from mycrypt import verify_password, get_password_hash


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


class UserRepository:
    @classmethod
    async def add_one(cls, data: SUserAdd) -> int:
        async with db.new_session() as session:
            dict_data = data.model_dump()
            password = dict_data.pop('password')
            dict_data['password_hash'] = get_password_hash(password)
            user = db.UsersTable(**dict_data)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id

    @ classmethod
    async def get_all(cls) -> List[SUser]:
        async with db.new_session() as session:
            result = await session.execute(select(db.UsersTable))
            users = result.scalars().all()
            user_schemas = [SUser.model_validate(
                user_model.__dict__) for user_model in users]
            return user_schemas
