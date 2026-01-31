from datetime import datetime, timedelta

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlmodel import Session, select

from app.core.database import engine
from app.core.email import send_order_email
from app.models.order import Order
from app.models.user import User

scheduler = AsyncIOScheduler()


async def auto_cancel_stale_orders_job():
    now = datetime.utcnow()
    cutoff = now - timedelta(hours=24)

    # session manual
    with Session(engine) as session:
        stmt = select(Order).where(
            Order.status == "pending",
            Order.created_at < cutoff,
        )
        orders = session.exec(stmt).all()

        if not orders:
            return

        for order in orders:
            order.status = "cancelled"
            session.add(order)

            user = session.get(User, order.user_id)
            if user and user.email:
                subject = f"Order #{order.id} Cancelled"
                body = f"<p>Your order #{order.id} has been automatically cancelled due to inactivity.</p>"

                await send_order_email(user.email, subject, body)

        session.commit()


def start_scheduler():
    # jalan perhari jam 02:00 UTC
    trigger = CronTrigger(hour=2, minute=0)
    scheduler.add_job(auto_cancel_stale_orders_job, trigger)
    scheduler.start()


def shutdown_scheduler():
    scheduler.shutdown(wait=False)
