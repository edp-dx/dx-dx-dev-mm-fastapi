"""Example of fastapi main file."""
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Returns Hello World."""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, item_count: Union[str, None] = None):
    """Returns numbers of items."""
    return {"item_id": item_id, "q": item_count}
