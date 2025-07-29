# References: 1.2. System Architecture & Implementation Plan
# References: 1.3. Technology Choices & Rationale (SQLAlchemy 2.0 Async)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from .config import settings

# Create an asynchronous engine to connect to the PostgreSQL database
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Create a sessionmaker to generate new database sessions
# expire_on_commit=False prevents detached instance errors in FastAPI
AsyncSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession, expire_on_commit=False
)

# A base class for our declarative ORM models
Base = declarative_base()
