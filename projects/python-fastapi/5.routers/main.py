from fastapi import FastAPI
from users_router import router as users_router

app = FastAPI(title="User CRUD (JSON DB)")

app.include_router(users_router)

