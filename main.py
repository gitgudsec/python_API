from fastapi import FastAPI

app = FastAPI()

# this is called a path operation - decorator + function

# decorator @app.get("/"): this is what takes it from simply being a function to an API
# we use app (from line 3) and then specify to use a GET method, we can use others too - POST etc
# we also specify the path ("/"), which in this case refers to the root path

# function root(): note that we use a dictionary, but fastAPI automatically converts this to JSON

@app.get("/")
def root():
    return {"message": "What's the word, ma POOP."}

# let's create a new path operation
# this one will go and fetch social media posts

def get_posts():
    # here is our logic for retrieving posts - add later
    