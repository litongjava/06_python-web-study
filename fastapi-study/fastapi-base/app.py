from fastapi import FastAPI
from demo01 import demo01

app = FastAPI()

app.include_router(demo01)