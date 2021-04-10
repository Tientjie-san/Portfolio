import datetime
from typing import List, Optional

from pydantic import BaseModel


class BaseAdmin(BaseModel):
    login: str


class CreateAdmin(BaseAdmin):
    password: str


class ResponseAdmin(BaseAdmin):
    admin_id: int

    class Config:
        orm_mode = True


class Image(BaseModel):
    image_name: str
    image_url: str
    thumbnail: bool

    class Config:
        orm_mode = True


class Social(BaseModel):

    social_name: str
    social_link: str

    class Config:
        orm_mode = True


class Tag(BaseModel):
    tag: str
    category: str

    class Config:
        orm_mode = True


class ShortDescription(BaseModel):
    short: str

    class Config:
        orm_mode = True


class CompleteDescription(BaseModel):
    html: str

    class Config:
        orm_mode = True


class BaseProject(BaseModel):
    project_title: str
    date_start: datetime.date
    date_end: Optional[datetime.date] = None
    tags: List[Tag]


class ShortProject(BaseProject):
    short_description: ShortDescription

    class Config:
        orm_mode = True


class CompleteProject(BaseProject):
    description: CompleteDescription
    live_link: str
    github_link: str

    class Config:
        orm_mode = True


class CreateUser(BaseModel):
    user_title: str
    first_name: str
    last_name: str
    birth_date: datetime.date
    phone_number: str
    user_email: str
    about_me: str
    profile_picture: Optional[str] = None
    living_place: str


class User(BaseModel):
    user_title: str
    first_name: str
    last_name: str
    birth_date: datetime.date
    phone_number: str
    user_email: str
    about_me: str
    profile_picture: Optional[str] = None
    living_place: str
