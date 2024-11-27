from fastapi import FastAPI

# 创建一个APP实例
app = FastAPI()


# 添加路径操作装饰器和路径操作函数
@app.get("/")
async def demo():
  return {"Hello": "World"}


if __name__ == "__main__":
  import uvicorn

  # 启动服务，注意APP前面的文件名称
  uvicorn.run(app='main:app', host="127.0.0.1", port=8010)