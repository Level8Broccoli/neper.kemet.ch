from fastapi import FastAPI
from routes import items
from config import PROJECT_NAME

app = FastAPI(title=f'{PROJECT_NAME} API')
app.include_router(items.router)


@app.get('/', tags=['root'])
async def index():
    return {'status': 'online'}
