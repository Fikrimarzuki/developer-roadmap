from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Orders API Advanced"
    database_url: str = (
        "postgresql+psycopg2://postgres:postgresql123@localhost:5432/orders_db"
    )

    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"
    access_token_minutes: int = 15
    refresh_token_days: int = 7

    debug: bool = False

    # Email
    mail_username: str = "mail"
    mail_password: str = "pass"
    mail_from: str = "no-reply@example.com"
    mail_server: str = "smtp.gmail.com"
    mail_port: int = 587
    mail_tls: bool = True
    mail_ssl: bool = False

    # Google OAuth
    google_client_id: str = ""
    google_client_secret: str = ""
    google_redirect_uri: str = "http://localhost:8000/auth/google/callback"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
