from fastapi.templating import Jinja2Templates
from fastapi import Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.routing import APIRouter
from src.config.database import conn
from pymongo import MongoClient
from pathlib import Path
from bson import ObjectId
from src.config.settings import templates
from src.auth.jwt import verify_token
from datetime import datetime
router = APIRouter()

# GET CREATE PAGE
@router.get("/notes/create", response_class=HTMLResponse)
async def create_url(
    request: Request,
    current_user=Depends(verify_token)
):
    return templates.TemplateResponse(
        name="create_note.html",
        request=request,
        context={"user":current_user}
    )

#POST CREATE PAGE
@router.post("/notes/create",response_class=RedirectResponse)
def create_note(request: Request, current_user=Depends(verify_token)):
    form = request
    tags = form.get("tags").split(",") if form.get("tags") else []
    note = {
        "title": form.get("title"),
        "content": form.get("content"),
        "tags": tags,
        "uid": str(current_user.get("_id")),
        "date_created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    conn.notes.insert_one(note)
    return RedirectResponse(url="/notes", status_code=303)

#GET ALL NOTES
@router.get("/notes", response_class=HTMLResponse)
async def notes_url(request: Request,current_user=Depends(verify_token)):
    notes = list(conn.notes.find({"uid": str(current_user.get("_id"))}))
    return templates.TemplateResponse(
        name="notes.html",
        request=request,
        context={"notes": notes,"user":current_user}
    )

#GET INDIVISUAL NOTE
@router.get("/note/{id}", response_class=HTMLResponse)
async def note_url(request: Request, id: str,current_user=Depends(verify_token)):
    print(current_user)
    note = conn.notes.find_one({"_id": ObjectId(id), "uid": str(current_user.get("_id"))})
    if not note:
        return JSONResponse(content={"current_user": str(current_user.get("_id"))}, status_code=404)
    return templates.TemplateResponse(
        name="indivisual_note.html",
        request=request,
        context={"note": note, "user": current_user}
    )

#UPDATE

#DELETE