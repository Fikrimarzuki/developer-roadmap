from sqlmodel import Session
from sqlalchemy import text


def list_order_summaries(session: Session, user_id: int | None = None):
    if user_id is None:
        q = text("SELECT * FROM v_order_summary ORDER BY order_id DESC")
        rows = session.exec(q).all()
    else:
        q = text(
            "SELECT * FROM v_order_summary WHERE user_id = :uid ORDER BY order_id DESC"
        )
        rows = session.exec(q, {"uid": user_id}).all()

    return [dict(r._mapping) for r in rows]
