from fastapi import FastAPI, Request
from routes import items
from config import PROJECT_NAME, BACKEND_URL_PREFIX

app = FastAPI(title=f'{PROJECT_NAME} API', root_path=BACKEND_URL_PREFIX)
app.include_router(items.router)


@app.get('/', tags=['root'])
async def index(request: Request):
    return {'status': 'online', 'version': '2'}
