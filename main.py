from mylib.logic import wiki, summary
from fastapi import FastAPI
import uvicorn
import json

app = FastAPI()

@app.get("/")
async def root():
    """ Base API Definition """
    return {"message":"Wikipedia API! You can Call, Search or Wiki"}

@app.get("/search/{value}")
async def search(value: str):
    """ Search a value in wikipedia """
    result = wiki(value,10)
    return {"Result":json.dumps(result)}

@app.get("/summary/{value}")
async def search_summary(value: str):
    """ Search a value in wikipedia """
    result = summary(value,3)
    return {"Result":json.dumps(result)}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')