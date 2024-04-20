from app.api.models import LabelIn, LabelOut
from app.api.db import labels, database


async def add_label(payload: LabelIn):
    query = labels.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_label():
    query = labels.select()
    return await database.fetch_all(query=query)


async def get_label(id):
    query = labels.select().where(labels.c.id == id)
    return await database.fetch_one(query=query)


async def delete_label(id: int):
    query = labels.delete().where(labels.c.id == id)
    return await database.execute(query=query)

