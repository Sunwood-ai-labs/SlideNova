# app.py
import streamlit as st
import os
import subprocess

def main():
    st.title("Markdown to Slidev")

    # マークダウンファイルの内容を入力するテキストエリア
    markdown_text = st.text_area("Enter your markdown content here:", height=400)

    # スライドを生成するボタン
    if st.button("Generate Slides"):
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
            st.image(f"slides/out/{slide}")

        # 一時ファイルを削除
        os.remove("temp.md")

if __name__ == "__main__":
    main()