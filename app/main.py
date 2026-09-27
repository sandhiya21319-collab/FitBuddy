from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .database import init_db
from .routes import router


BASE_DIR = Path(__file__).resolve().parent


app = FastAPI(
    title="FitBuddy - AI Workout Generator",
    description="AI-powered personalized fitness plan generator",
    version="1.0.0"
)


# Static files
app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)


# HTML templates
templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


# Make templates available to routes.py
app.state.templates = templates


# Routes
app.include_router(router)


@app.on_event("startup")
def startup_event():
    init_db()