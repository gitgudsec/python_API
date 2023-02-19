from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str

    # we can also assign default values from the go
    # note if you assign a default value it is n o longer required
    published: bool = True

    # if we want a value to be optional, but if   user does not provide it defaults to 0
    # note: special library we need to import for this one
    rating: Optional[int] = None


@app.get("/")
def root():
    return {"data": my_posts}

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "numbchuc Skillz", "content": "Pretty good with a bow", "id": 69}]



@app.post("/posts")
def create_posts(new_post: Post):
  
    my_posts.append(post.dict())
    return {"data": "new post"}


    

# create functionality to persiste - ie save - the data
# for now we will simply store it in memory - start up top line 26
# later when we are ready we will integrate with SQL
# Note when saving to SQL it will automatically assign an ID for every post saved
# However since we are saving to a variable, we need to create
