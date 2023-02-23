from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optionaltopnal;

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    id: int

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "numbchuc Skillz", "content": "Pretty good with a bow", "id": 69}]

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_post(post: Post):
    print(post.dict())
    print(post)
    return {"data": "Chapstick"}