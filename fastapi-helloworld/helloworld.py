from fastapi import APIRouter

helloworld = APIRouter()


@helloworld.get("/")
async def demo():
  return {"Hello": "World"}
