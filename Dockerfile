# Dockerfile
FROM node:18

USER root
RUN useradd -m -u 1001 user
WORKDIR /app
RUN chown -R user:user /app

# Pythonのインストール
RUN apt-get update && apt-get install -y python3 python3-pip

# 作業ディレクトリの設定
WORKDIR /app

RUN npm install -g @slidev/cli@latest
RUN npx playwright install-deps
RUN npx playwright install
RUN chown -R user:user /app
RUN chown -R user:user /usr/local/lib/node_modules/@slidev/
USER user

# Slidevのインストール
RUN npm install -D playwright-chromium

# スライドディレクトリの作成
RUN mkdir slides



USER user

RUN pip install streamlit --break-system-packages
ENV PATH="/home/user/.local/bin:${PATH}"

CMD ["python3", "-m", "streamlit", "run", "app.py"]