from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    source: str
    lang: str
    time_limit: int


app = FastAPI()



@app.post("/compile/",response_model=Item)
async def create_item(item: Item):
    
    return item