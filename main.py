from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.routes.home import router as Home_Router
from src.auth.router import router as Auth_Router
from src.routes.about import router as About_Router
from src.routes.dashboard import router as Dashboard_Router

app=FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(Home_Router)
app.include_router(Auth_Router)
app.include_router(About_Router)
app.include_router(Dashboard_Router)

