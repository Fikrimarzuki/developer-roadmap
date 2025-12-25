from sqlalchemy import text
from sqlmodel import Session


def list_order_summaries(session: Session, user_id: int | None = None):
    if user_id is None:
        q = text("SELECT * FROM v_order_summary ORDER BY order_id DESC")
        rows = session.execute(q).mappings().all()
    else:
        q = text(
            "SELECT * FROM v_order_summary WHERE user_id = :uid ORDER BY order_id DESC"
        )
        rows = session.execute(q, {"uid": user_id}).mappings().all()

    return [dict(r) for r in rows]
