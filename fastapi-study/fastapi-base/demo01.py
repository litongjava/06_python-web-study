from fastapi import APIRouter

demo01 = APIRouter()


# @demo01.get("/")
# async def demo():
#   return {"Hello": "World"}

demo01.get("/echo")
async def getEchoApi():
  return {"echo": "echo"}

# 注意，这里text将是函数定义的参数名
demo01.get("/echo/{text}")
# 通过定义参数类型可以让fastapi进行默认的参数检查
async def getEchoApi(text: str):
  return {"echo": text}
