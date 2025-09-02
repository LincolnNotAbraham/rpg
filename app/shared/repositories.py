from typing import Generic, Type, TypeVar
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel

from app.shared.database.postgrescon import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel) 


class BaseRepository(Generic[ModelType, CreateSchemaType]):

    def __init__(self, model: Type[ModelType], db: AsyncSession):
