from fastapi import FastAPI

from routers import items

app = FastAPI()
app.include_router(items.router)


@app.get("/")
def get_root():
    return {"Version": "0.0.0"}
