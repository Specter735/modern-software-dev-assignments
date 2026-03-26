from typing import Optional

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import ActionItem
from ..schemas import ActionItemCreate, ActionItemRead, BulkCompleteRequest, SuccessEnvelope

router = APIRouter(prefix="/action-items", tags=["action_items"])


def _not_found(message: str) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={"ok": False, "error": {"code": "NOT_FOUND", "message": message}},
    )


@router.get("/", response_model=SuccessEnvelope[list[ActionItemRead]])
def list_items(
    completed: Optional[bool] = None, db: Session = Depends(get_db)
) -> SuccessEnvelope[list[ActionItemRead]]:
    stmt = select(ActionItem)
    if completed is not None:
        stmt = stmt.where(ActionItem.completed == completed)
    rows = db.execute(stmt).scalars().all()
    return SuccessEnvelope(data=[ActionItemRead.model_validate(row) for row in rows])


@router.post("/", response_model=SuccessEnvelope[ActionItemRead], status_code=201)
def create_item(
    payload: ActionItemCreate, db: Session = Depends(get_db)
) -> SuccessEnvelope[ActionItemRead]:
    item = ActionItem(description=payload.description, completed=False)
    db.add(item)
    db.flush()
    db.refresh(item)
    return SuccessEnvelope(data=ActionItemRead.model_validate(item))


@router.post("/bulk-complete", response_model=SuccessEnvelope[list[ActionItemRead]])
def bulk_complete(
    payload: BulkCompleteRequest, db: Session = Depends(get_db)
) -> SuccessEnvelope[list[ActionItemRead]] | JSONResponse:
    items = (
        db.execute(select(ActionItem).where(ActionItem.id.in_(payload.ids)))
        .scalars()
        .all()
    )
    found_ids = {item.id for item in items}
    missing = [i for i in payload.ids if i not in found_ids]
    if missing:
        return _not_found(f"Action items not found: {missing}")

    for item in items:
        item.completed = True
    db.flush()
    for item in items:
        db.refresh(item)
    return SuccessEnvelope(data=[ActionItemRead.model_validate(item) for item in items])


@router.put("/{item_id}/complete", response_model=SuccessEnvelope[ActionItemRead])
def complete_item(
    item_id: int, db: Session = Depends(get_db)
) -> SuccessEnvelope[ActionItemRead] | JSONResponse:
    item = db.get(ActionItem, item_id)
    if not item:
        return _not_found("Action item not found")
    item.completed = True
    db.add(item)
    db.flush()
    db.refresh(item)
    return SuccessEnvelope(data=ActionItemRead.model_validate(item))
