from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
  return {"message": "hello from fastapi"}

@app.get("/ping")
def ping():
  return {"pong": True}

@app.get("/hello/{name}")
def hello(name):
  return {"hello": name}

@app.get("/search")
def search(q=None):
  return {"q": q}

