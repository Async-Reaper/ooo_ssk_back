from sqlalchemy.ext.asyncio import AsyncSession,    create_async_engine
from sqlalchemy.orm         import DeclarativeMeta, sessionmaker, declarative_base
import config

engine = create_async_engine(config.DB_URL)

async_session_maker = sessionmaker(bind= engine, 
                                   class_= AsyncSession, 
                                   expire_on_commit= True)

Base: DeclarativeMeta = declarative_base()