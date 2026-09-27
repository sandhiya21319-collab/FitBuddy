from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from .ai_service import generate_workout_plan
from .database import (
    add_user,
    get_user,
    get_all_users,
    update_user_plan
)

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@router.post("/generate", response_class=HTMLResponse)
async def generate_plan(
    request: Request,
    name: str = Form(...),
    user_id: str = Form(...),
    age: int = Form(...),
    weight: float = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...)
):
    workout_plan = generate_workout_plan(
        name=name,
        age=age,
        weight=weight,
        goal=goal,
        intensity=intensity
    )

    add_user(
        name=name,
        user_id=user_id,
        age=age,
        weight=weight,
        goal=goal,
        intensity=intensity,
        original_plan=workout_plan
    )

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "name": name,
            "user_id": user_id,
            "age": age,
            "weight": weight,
            "goal": goal,
            "intensity": intensity,
            "workout_plan": workout_plan
        }
    )


@router.get("/feedback", response_class=HTMLResponse)
async def feedback_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="feedback.html",
        context={}
    )


@router.post("/feedback", response_class=HTMLResponse)
async def submit_feedback(
    request: Request,
    user_id: str = Form(...),
    feedback: str = Form(...)
):
    user = get_user(user_id)

    if not user:
        return templates.TemplateResponse(
            request=request,
            name="error.html",
            context={"error": "User ID not found."}
        )

    old_plan = user["original_plan"] or ""

    updated_plan = old_plan + "\n\nFeedback: " + feedback

    update_user_plan(
        user_id=user_id,
        updated_plan=updated_plan
    )

    return templates.TemplateResponse(
        request=request,
        name="feedback.html",
        context={"success": True}
    )


@router.get("/all-users", response_class=HTMLResponse)
async def all_users(request: Request):
    users = get_all_users()

    return templates.TemplateResponse(
        request=request,
        name="all_users.html",
        context={"users": users}
    )