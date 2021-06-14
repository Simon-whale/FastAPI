from pydantic import BaseModel


class Item(BaseModel):
    id: str
    value: str
