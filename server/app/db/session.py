from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

from app.core.config import settings 

engine = create_engine(
    settings.DATABASE_URL,
    echo=True
    #tells the sqlalchemy to print all the raw SQL to print 
    # int the terminal 
)

SessionLocal = sessionmaker(
    bind = engine,
    autocommit = False,
    autoflush=False
)

