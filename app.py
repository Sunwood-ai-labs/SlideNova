# app.py
import streamlit as st
import os
import subprocess
import zipfile
import shutil
import base64

def load_markdown(file_path):
    with open(file_path, encoding="utf8") as f:
        return f.read()


def display_front_page():
    html_front = load_markdown('docs/page_front.md')
    st.markdown(f"{html_front}", unsafe_allow_html=True)

def main():
    display_front_page()

    # マークダウンファイルの内容を入力するテキストエリア
    markdown_text = st.text_area("Enter your markdown content here:", height=400)

    # スライドを生成するボタン
    if st.button("Generate Slides"):
        # slides/outフォルダを綺麗にする
        if os.path.exists("slides/out"):
            shutil.rmtree("slides/out")
        os.makedirs("slides/out")

        # 一時ファイルにマークダウンの内容を書き込む
        with open("temp.md", "w") as f:
            f.write(markdown_text)

        # slidevコマンドを実行してスライドを生成
        subprocess.run(["npx", "slidev", "export", "temp.md", "--format", "png", "--output", "slides/out/", "--dark", "-t"])

        # 生成されたスライドを表示
        slides = []
        for filename in os.listdir("slides/out"):
            if filename.endswith(".png"):
                slides.append(filename)
        slides.sort()

        for slide in slides:
            # 画像を表示
            st.image(f"slides/out/{slide}")
            
            # 画像をダウンロードするリンクを表示
            with open(f"slides/out/{slide}", "rb") as f:
                img_bytes = f.read()
                b64 = base64.b64encode(img_bytes).decode()
                href = f'<a href="data:image/png;base64,{b64}" download="{slide}">Download {slide}</a>'
                st.markdown(href, unsafe_allow_html=True)

        # スライドをZIPファイルに圧縮
        zip_filename = "slides.zip"
        with zipfile.ZipFile(zip_filename, "w") as zip_file:
            for slide in slides:
                zip_file.write(f"slides/out/{slide}", slide)

        # ZIPファイルをダウンロードするリンクを表示
        with open(zip_filename, "rb") as f:
            bytes = f.read()
            b64 = base64.b64encode(bytes).decode()
            href = f'<a href="data:application/zip;base64,{b64}" download="{zip_filename}">Download All Slides</a>'
            st.markdown(href, unsafe_allow_html=True)

        # 一時ファイルとZIPファイルを削除
        os.remove("temp.md")
        os.remove(zip_filename)

if __name__ == "__main__":
    main()