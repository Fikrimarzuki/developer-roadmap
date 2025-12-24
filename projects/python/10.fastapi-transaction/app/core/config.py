from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  app_name: str = "Orders API"
  database_url: str = "sqlite:///./app.db"

  jwt_secret: str
  jwt_algorithm: str = "HS256"
  access_token_minutes: int = 15
  refresh_token_days: int = 7

  debug: bool = False

  model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()

