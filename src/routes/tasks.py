from typing import Annotated, List

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse, PlainTextResponse

from repository import TaskRepository
from schemas import STask, STaskAdd

router = APIRouter(prefix="/tasks")


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]):
    task_id = await TaskRepository.add_one(task)

    return JSONResponse(status_code=200, content={"task_id": task_id})


@router.post("/multiple")
async def add_tasks(tasks: List[STaskAdd]):
    task_ids = []
    for task in tasks:
        task_id = await TaskRepository.add_one(task)
        task_ids.append(task_id)

    return {"task_ids": task_ids}


@router.get("")
async def get_tasks():
    tasks = await TaskRepository.get_all()
    return tasks
