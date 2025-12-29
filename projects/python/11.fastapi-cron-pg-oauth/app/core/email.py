from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import EmailStr, SecretStr
from app.core.config import settings

mail_config = ConnectionConfig(
    MAIL_USERNAME=settings.mail_username,
    MAIL_PASSWORD=SecretStr(settings.mail_password),
    MAIL_FROM=settings.mail_from,
    MAIL_PORT=settings.mail_port,
    MAIL_SERVER=settings.mail_server,
    MAIL_STARTTLS=settings.mail_tls,
    MAIL_SSL_TLS=settings.mail_ssl,
    USE_CREDENTIALS=bool(settings.mail_username),
    SUPPRESS_SEND=True,
)

fast_mail = FastMail(mail_config)


async def send_order_email(to: EmailStr, subject: str, body: str) -> None:
    message = MessageSchema(
        subject=subject,
        recipients=[to], # type: ignore[list-item]
        body=body,
        subtype=MessageType.html,
    )
    await fast_mail.send_message(message)
