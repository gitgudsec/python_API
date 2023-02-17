from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()





@app.get("/")
def root():
    return {"message": "What's the word, ma POOP."}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}

