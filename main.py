from fastapi import FastAPI

app = FastAPI()

# this is called a path operation
# decorator @app.get("/")
# function root():

@app.get("/")
def root():
    return {"message": "Hello World"}

# note that we use a dictionary, but fastAPI automatically converts this to JSON