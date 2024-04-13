# Dockerfile
FROM node:18

# Pythonのインストール
RUN apt-get update && apt-get install -y python3 python3-pip

# 作業ディレクトリの設定
WORKDIR /app

# Slidevのインストール
RUN npm install -g @slidev/cli@latest
RUN npm install -D playwright-chromium
RUN npx playwright install-deps

# Pythonスクリプトのコピー
COPY run_slidev.py .

# スライドディレクトリの作成
RUN mkdir slides