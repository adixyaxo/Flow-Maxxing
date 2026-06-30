from fastapi.templating import Jinja2Templates
from fastapi import Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter
from src.config.database import conn, notes_DB
from pymongo import MongoClient
from pathlib import Path
from bson import ObjectId
from src.config.settings import templates
from src.auth.jwt import verify_token
from datetime import datetime
router = APIRouter()


#GET ALL NOTES
@router.get("/notes", response_class=HTMLResponse)
async def notes_url(request: Request,current_user=Depends(verify_token)):
    return templates.TemplateResponse(
        name="notes.html",
        request=request,
        context={"notes": list(notes_DB.find({"uid": str(current_user.get("_id"))})),"user":current_user}
    )


# GET CREATE PAGE
@router.get("/notes/create", response_class=HTMLResponse)
async def create_note_get(
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
async def create_note_post(request: Request, current_user=Depends(verify_token)):
    note = {
        "title": request.get("title"),
        "content": request.get("content"),
        "tags": request.get("tags").split(",") if request.get("tags") else [],
        "uid": str(current_user.get("_id")),
        "date_created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    notes_DB.insert_one(note)
    return RedirectResponse(url="/notes", status_code=303)


#READ NOTE
@router.get("/note/{id}", response_class=HTMLResponse)
async def read_note(request: Request, id: str,current_user=Depends(verify_token)):
    print(current_user)
    note = notes_DB.find_one({"_id": ObjectId(id), "uid": str(current_user.get("_id"))})
    if not note:
        return JSONResponse(content={"current_user": str(current_user.get("_id"))}, status_code=404)
    return templates.TemplateResponse(
        name="indivisual_note.html",
        request=request,
        context={"note": note, "user": current_user}
    )

#UPDATE

@router.put("/note/{id}")
async def update_note(
    request: Request,
    id: str,
    current_user=Depends(verify_token)
):
    # 1. Parse JSON body manually since we use Request
    try:
        body = await request.json()
        content = body.get("content")
        if content is None:
            raise HTTPException(status_code=400, detail="Content is required")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    print(current_user)

    # Ensure id is a valid ObjectId
    try:
        obj_id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    # 2. Async Database Check (Use await with Motor)
    # Verify ownership and existence
    note = await notes_DB.find_one({
        "_id": obj_id,
        "uid": str(current_user.get("_id"))
    })

    if not note:
        # Return JSON instead of redirect on error to avoid browser loops
        raise HTTPException(status_code=404, detail="Note not found or unauthorized")

    # 3. Async Database Update
    newvalues = {"$set": {"content": content}}
    await notes_DB.update_one({"_id": obj_id}, newvalues)

    # 4. Fix Redirect URL (Format the string correctly)
    # Use f-string to inject the actual ID
    return RedirectResponse(url=f"/note/{id}", status_code=303)
#DELETE