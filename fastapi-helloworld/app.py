from fastapi import FastAPI
from helloworld import helloworld

app = FastAPI()

app.include_router(helloworld)
