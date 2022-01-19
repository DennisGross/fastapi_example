from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name : str
    price: float
    brand : Optional[str] = None

first_item = Item(name="Lol", price =3)
inventory = {
    1 : first_item
}

@app.get("/")
def get_home():
    return {"Data": "Hello World"}

@app.get("/get-item/{item_id}")
def get_item(item_id : int = Path(None,description="The ID of the item you like to view.",lt=2)):
    return inventory[item_id]



@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item already exists."}
    inventory[item_id] = item
    return inventory[item_id]
