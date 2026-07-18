from app.models import *
# this script helps to load all models before sqlalchemy runs 
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass