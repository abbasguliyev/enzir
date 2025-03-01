from fastapi import FastAPI
from auth.router import router as auth_router
from mesvere.router import router as mesvere_router

app = FastAPI()

app.include_router(auth_router, prefix="/api/v1/auth")
app.include_router(mesvere_router, prefix="/api/v1/mesvere")

@app.get('/')
async def home():
    return {'message': 'Welcome'}