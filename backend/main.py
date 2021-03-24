from fastapi import FastAPI

from routers import item_router

app = FastAPI()
app.include_router(item_router.router)

@app.get("/")
def get_status():
    return {"Status": "online"}
