from fastapi import FastAPI
from pydantic import BaseModel
import hashlib

import base64
import os

app = FastAPI()

# Create an API endpoint using the FastAPI framework that accepts a JSON payload in a POST request
# generate a Pydantic model
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class TextPayload(BaseModel):
    text: str

@app.post("/checksum/")
def get_checksum(payload: TextPayload):
    checksum = hashlib.md5(payload.text.encode()).hexdigest()
    return {"checksum": checksum}

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return item
