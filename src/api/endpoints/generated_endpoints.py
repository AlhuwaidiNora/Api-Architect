from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import logging

# Set up logging
logging.basicConfig(filename='api_architect.log', level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

# Example model
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None

# Example in-memory database
items_db = []

@router.get("/items/", response_model=List[Item])
async def get_items():
    """Get all items"""
    logger.info("Fetching all items")
    return items_db

@router.post("/items/", response_model=Item)
async def create_item(item: Item):
    """Create a new item"""
    logger.info(f"Creating new item: {item}")
    item.id = len(items_db) + 1
    items_db.append(item)
    return item

@router.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Get a specific item by ID"""
    logger.info(f"Fetching item with ID: {item_id}")
    if item_id <= 0 or item_id > len(items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id - 1]
