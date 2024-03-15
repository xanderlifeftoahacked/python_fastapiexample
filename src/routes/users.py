from typing import Annotated
from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

from schemas import SUserAdd
from repository import UserRepository

router = APIRouter(prefix="/users")


@router.post("/add")
async def add_user(task: Annotated[SUserAdd, Depends()]):
    user_id = await UserRepository.add_one(task)

    return JSONResponse(status_code=200, content={"user_id": user_id})


@router.get("")
async def get_users():
    users = await UserRepository.get_all()
    return users
