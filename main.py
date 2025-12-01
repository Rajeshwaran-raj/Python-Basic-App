from typing import Dict, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="In-memory FastAPI CRUD",
    version="0.1.0",
    description="Simple in-memory CRUD API using FastAPI 0.99.x",
)


class ItemBase(BaseModel):
    name: str
    description: str = ""


class Item(ItemBase):
    id: int


# In-memory storage with some hard-coded values
ITEMS: Dict[int, Item] = {
    1: Item(id=1, name="Sample Item 1", description="First hard-coded item"),
    2: Item(id=2, name="Sample Item 2", description="Second hard-coded item"),
}
NEXT_ID: int = 3


@app.get("/items", response_model=List[Item])
def list_items() -> List[Item]:
    """List all items"""
    return list(ITEMS.values())


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemBase) -> Item:
    """Create a new item"""
    global NEXT_ID
    item_id = NEXT_ID
    NEXT_ID += 1

    new_item = Item(id=item_id, **item.dict())
    ITEMS[item_id] = new_item
    return new_item


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    """Retrieve a single item"""
    item = ITEMS.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_update: ItemBase) -> Item:
    """Update an existing item"""
    existing = ITEMS.get(item_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Item not found.")

    updated = existing.copy(update=item_update.dict(exclude_unset=True))
    ITEMS[item_id] = updated
    return updated


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item"""
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="Item not found.")

    del ITEMS[item_id]
    return {"message": "Item deleted."}
