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
        context={"notes": await notes_DB.find({"uid": str(current_user.get("_id"))}).to_list(length=None),"user":current_user}
    )


#CREATE NOTE
@router.get("/notes/create", response_class=HTMLResponse)
async def create_note_get(
    request: Request,
    current_user=Depends(verify_token)
):
    note = {
        "title": "Title",
        "content": "Content",
        "tags": ["Tag"],
        "uid": str(current_user.get("_id")),
        "date_created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    newNote = await notes_DB.insert_one(note)
    id = newNote.inserted_id
    return RedirectResponse(url=f"/note/{id}",status_code=303)


#READ NOTE
@router.get("/note/{id}", response_class=HTMLResponse)
async def read_note(request: Request, id: str,current_user=Depends(verify_token)):
    note = await notes_DB.find_one({"_id": ObjectId(id), "uid": str(current_user.get("_id"))})
    if not note:
        return JSONResponse(content={"current_user": str(current_user.get("_id"))}, status_code=404)
    return templates.TemplateResponse(
        name="indivisual_note.html",
        request=request,
        context={"note": note, "user": current_user}
    )

#UPDATE

@router.put("/note/{id}",response_class=RedirectResponse)
async def update_note(
    request: Request,
    id: str,
    current_user=Depends(verify_token)
):
    # 1. Parse JSON body manually since we use Request
    try:
        body = await request.json()
        content = body.get("content")
        title = body.get("title")
        if content is None:
            raise HTTPException(status_code=400, detail="Content is required")
        if title is None:
            raise HTTPException(status_code=400, detail="Content is required")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid JSON")

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
    newvalues = {"$set": {"content": content,"title":title}}
    await notes_DB.update_one({"_id": obj_id}, newvalues)

    return RedirectResponse(url=f"/note/{id}", status_code=303)

#DELETE
@router.delete("/note/{id}",response_class=JSONResponse)
async def create_note_post(id:str,current_user=Depends(verify_token)):
    if current_user:
        await notes_DB.delete_one({"_id": ObjectId(id)})
    return {"success":True}
