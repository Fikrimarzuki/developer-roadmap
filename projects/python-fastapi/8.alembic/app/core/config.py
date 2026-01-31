from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  app_name: str
  database_url: str

  jwt_secret: str
  jwt_algorithm: str
  jwt_expire_minutes: int

  model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
