from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  app_name: str = "User CRUD API"
  database_url: str = "sqlite:///./app.db"

  jwt_secret: str = "change-me"
  jwt_algorithm: str = "HS256"
  jwt_expire_minutes: int = 60

  model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
