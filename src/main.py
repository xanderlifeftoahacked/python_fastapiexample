from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

from routes.tasks import router as task_router
from routes.users import router as user_router
import database as db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.delete_tables()
    await db.create_tables()
    print("INIT DB")
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
app.include_router(user_router)


@app.exception_handler(ValidationError)
async def value_error_exception_handler(request: Request, exc: ValidationError):
    return PlainTextResponse(str(exc), status_code=400)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    return PlainTextResponse(str(exc), status_code=400)


@app.exception_handler(IntegrityError)
async def data_exists_exception_handler(request, exc: IntegrityError):
    return PlainTextResponse(str(exc), status_code=400)
