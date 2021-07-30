# 基于的基础镜像

FROM python:3.7.3

# 维护者信息

MAINTAINER name  z@163.com

# 设置当前文件夹是工作目录
WORKDIR .

# 代码添加到当前文件夹
ADD . .

# 安装支持

RUN pip install -r requirements.txt

CMD ["python", "-u", "./main.py"]
