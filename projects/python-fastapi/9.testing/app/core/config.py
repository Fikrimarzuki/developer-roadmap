from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  app_name: str
  database_url: str

  jwt_secret: str
  jwt_algorithm: str
  access_token_minutes: int
  refresh_token_days: int
  debug: bool = False

  class Config:
    env_file = ".env"

settings = Settings()

