from pydantic import BaseModel
from typing import List, Optional

class LabelIn(BaseModel):
    name: str
    phone: str
    count_artists: int
    county: str


class LabelOut(LabelIn):
    id: int
