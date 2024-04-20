from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import LabelOut, LabelIn
from app.api import db_manager

labels = APIRouter()

@labels.post('/', response_model=LabelOut, status_code=201)
async def create_label(payload: LabelIn):
    label_id = await db_manager.add_label(payload)

    response = {
        'id': label_id,
        **payload.dict()
    }

    return response


@labels.get('/', response_model=List[LabelOut])
async def get_labels():
    return await db_manager.get_all_label()


@labels.get('/{id}/', response_model=LabelOut)
async def get_label(id: int):
    company = await db_manager.get_label(id)
    if not company:
        raise HTTPException(status_code=404, detail="Label not found")
    return company


@labels.delete('/{id}/', response_model=None)
async def delete_label(id: int):
    company = await db_manager.get_label(id)
    if not company:
        raise HTTPException(status_code=404, detail="Label not found")
    return await db_manager.delete_label(id)