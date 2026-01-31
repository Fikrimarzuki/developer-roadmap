import sys

import psycopg2
from sqlalchemy.engine.url import make_url

from app.core.config import settings


def ensure_database():
    db_url = settings.database_url
    if not db_url:
        print("DATABASE_URL is not set in environment", file=sys.stderr)
        sys.exit(1)

    url = make_url(db_url)

    target_db = url.database
    user = url.username or "postgres"
    password = url.password or ""
    host = url.host or "localhost"
    port = url.port or 5432

    # psycopg2 does NOT use "+psycopg2" in the scheme, ignore driver part
    admin_dsn = (
        f"dbname=postgres user={user} password={password} " f"host={host} port={port}"
    )

    print(f"Connecting to server {host}:{port} as {user} ...")
    conn = psycopg2.connect(admin_dsn)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s;", (target_db,))
    exists = cur.fetchone() is not None

    if exists:
        print(f"Database '{target_db}' already exists. Skipping CREATE.")
    else:
        print(f"Creating database '{target_db}' ...")

        cur.execute(f'CREATE DATABASE "{target_db}";')
        print("Database created.")

    cur.close()
    conn.close()


if __name__ == "__main__":
    ensure_database()
