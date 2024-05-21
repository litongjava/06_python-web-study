# 创建解析器
import argparse

import uvicorn

from app import app

parser = argparse.ArgumentParser(description="这是一个命令行参数解析示例")

# 添加参数
parser.add_argument('-a', '--bind_addr', type=str, required=False, default="0.0.0.0", help="ip地址")
parser.add_argument('-p', '--port', type=int, required=False, default=80, help="端口")
# 解析参数
args = parser.parse_args()
# 保存参数到单例对象中
from cmd_args import CmdArgs
cmd_args = CmdArgs()
cmd_args.set_args(args)
if __name__ == "__main__":
  import server

  server.register_Hanlder(app)
  uvicorn.run(app, host=args.bind_addr, port=args.port, workers=1)
