from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"yes dumb this is working"}