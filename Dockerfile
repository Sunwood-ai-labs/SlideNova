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
RUN npm install @slidev/theme-seriph

COPY --chown=user:user . /app
RUN yes | npx slidev export slides/demo.md --format png --output slides/out/ --dark
RUN npm install


RUN pip3 install streamlit --break-system-packages
ENV PATH="/home/user/.local/bin:${PATH}"
USER root
RUN pip3 install streamlit --break-system-packages
RUN chmod 777 -R /app
RUN chmod 777 -R /usr/local/lib/node_modules/@slidev/
USER node
RUN npx playwright install 

CMD ["python3", "-m", "streamlit", "run", "app.py"]