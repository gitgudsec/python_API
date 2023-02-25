from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


app = FastAPI()

class Post(BaseModel): 
    title: str
    content: str
    id: int

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "numbchuc Skillz", "content": "Pretty good with a bow", "id": 69}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/posts")
def get_posts():
    print ("Success")
    return {"data": my_posts}

@app.post("/posts")
def create_post(post: Post):
    # here it takes the values the JSON values I send it with POST request
    # and convert it to a dictionary
    post_dict = post.dict()
    # here it reassigns the id value a random number in a large range
    post_dict["id"] = randrange(0, 1000000)
    # now we take the new data field sent with POST, and we add it our my_posts list (of dictionaries)
    my_posts.append(post_dict)
    # this prints the newly added post to console
    print(post_dict)
    # this returns the new updated list to the sender of request - thus we respond with original "db" updated with the value they just provided
    return {"data": my_posts}    

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

# we can see here now if the user provides us with an ID, it will use that in URL to only load that
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(int(id))
    # If it could not find id it will execute the message
    if post == None:
        return("That id does not exist.")
    return {"post_detail": post}
    



