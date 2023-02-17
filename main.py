from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    # we can also assign default values from the go
    # note if you assign a default value it is no longer required
    published: bool = True

    # if we want a value to be optional, but if user does not provide it defaults to 0


@app.get("/")
def root():
    return {"message": "What's the word, ma POOP."}


@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.title)
    print(new_post.content)
    print(new_post.published)
    return {"data": "new post"}

