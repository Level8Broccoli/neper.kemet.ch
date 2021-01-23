from fastapi import FastAPI

from routers import items

api = FastAPI()
api.include_router(items.router)


@api.get("/")
def get_root():
    return {"Version": "0.0.0"}
