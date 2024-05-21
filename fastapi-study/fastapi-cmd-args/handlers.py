from fastapi import APIRouter

from cmd_args import CmdArgs

index_router = APIRouter()


@index_router.get("/")
async def demo():
  return {"Hello": "World"}


@index_router.get("/args")
async def args():
  # 从单例对象中获取
  cmd_args = CmdArgs()
  args = cmd_args.get_args()
  return args
