from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    openai_api_key: str
    database_url: str = "postgresql://user:password@localhost:5432/resume_analyzer"
    redis_url: str = "redis://localhost:6379"
    cors_origins: str = "http://localhost:3000"
    
    class Config:
        env_file = ".env"
    
    @property
    def cors_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.cors_origins.split(",")]

settings = Settings()
