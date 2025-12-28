from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
from app.core.config import settings

mail_config = ConnectionConfig(
    MAIL_USERNAME=settings.mail_username,
    MAIL_PASSOWRD=settings.mail_password,
    MAIL_FROM=settings.mail_from,
    MAIL_PORT=settings.mail_port,
    MAIL_SERVER=settings.mail_server,
    MAIL_STARTTLS=settings.mail_tls,
    MAIL_SSL_TLS=settings.mail_ssl,
    USE_CREDENTIALS=True,
)

fast_mail = FastMail(mail_config)


async def send_order_email(to: EmailStr, subject: str, body: str) -> None:
    message = MessageSchema(subject=subject, recipients=[to], body=body, subtype="html")
    await fast_mail.send_message(message)
