FROM alpine:3.13

# 安装 Python 和 pip 以及构建工具
RUN apk add --no-cache python3 py3-pip gcc musl-dev python3-dev \
    libffi-dev openssl-dev pkgconfig \
    && pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple \
    && pip config set global.trusted-host mirrors.cloud.tencent.com \
    && pip install --upgrade pip

# 拷贝当前项目到/app目录下
COPY . /app

# 设定当前的工作目录
WORKDIR /app

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 安装 cryptography
RUN pip install --no-cache-dir cryptography

# 暴露端口
EXPOSE 80

# 启动应用
CMD ["python3", "run.py", "0.0.0.0", "80"]