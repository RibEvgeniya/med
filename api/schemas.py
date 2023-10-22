import datetime

from pydantic import BaseModel, EmailStr
from typing import Optional
from pydantic import UUID4, BaseModel, EmailStr, Field, validator





class ShowModel(BaseModel):
    class Config:
        orm_mode = True


class ClientBase(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    phone: str
    email: EmailStr
    birth_date: datetime.date  ## !!!!????


class ClientCreate(ClientBase):
    password: str


class ClientShow(ClientBase):
    id: int
    is_active: bool


##   is_active: bool


class ClientUpdate(BaseModel):
    first_name: str | None
    middle_name: str | None
    last_name: str | None
    phone: str | None
    password: str | None




