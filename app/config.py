# References: 1.3. Technology Choices & Rationale (Pydantic for validation)
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Pydantic model for managing application settings.
    It automatically reads environment variables from the .env file.
    """
    DATABASE_URL: str
    REDIS_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"

# Create a single, reusable instance of the settings
settings = Settings()
