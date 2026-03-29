from __future__ import annotations

from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException

from .. import db

router = APIRouter(prefix="/notes", tags=["notes"])

# TODO 4 New Endpoint to Retrieve All Notes
@router.get("")
def get_all_notes() -> List[Dict[str, Any]]:
    """Retrieve all notes from the database."""
    try:
        if hasattr(db, "list_notes"):
            rows = db.list_notes()
        else:
            # akan fallback jika fungsi db.list_notes belum ada di db.py
            conn = db.get_conn()
            cursor = conn.cursor()
            cursor.execute("SELECT id, content, created_at FROM notes ORDER BY created_at DESC")
            rows = cursor.fetchall()
            
        return [
            {"id": row["id"], "content": row["content"], "created_at": row["created_at"]}
            for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("")
def create_note(payload: Dict[str, Any]) -> Dict[str, Any]:
    content = str(payload.get("content", "")).strip()
    if not content:
        raise HTTPException(status_code=400, detail="content is required")
    note_id = db.insert_note(content)
    note = db.get_note(note_id)
    return {
        "id": note["id"],
        "content": note["content"],
        "created_at": note["created_at"],
    }

@router.get("/{note_id}")
def get_single_note(note_id: int) -> Dict[str, Any]:
    row = db.get_note(note_id)
    if row is None:
        raise HTTPException(status_code=404, detail="note not found")
    return {"id": row["id"], "content": row["content"], "created_at": row["created_at"]}