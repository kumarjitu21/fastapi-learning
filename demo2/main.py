from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    """Class Representing an Item"""    
    name: str
    price: float
    is_offer: Union[bool, None] = None

    def __init__(self, name, price, is_offer):
        self.name = name
        self.price = price
        self.is_offer = is_offer

@app.get("/")
async def main_route():
    """ Main route to print hello world """
    return {"message": "Hello world, welcome to my world!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    """Get Item by passing item_id"""
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
async def add_item(item_id: int, item: Item):
    """Adding Item by item_id"""
    return {"item_name": item.name, "item_id": item_id}
